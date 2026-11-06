#!/usr/bin/env python3
"""Prepare per-language build inputs from the pandoc-flavoured sources.

Invariants:
- The sources (`zh/`, `en/`) have NO Markdown headings: titles are bold
  paragraphs ("**第一章 ...**", "**1.1 ...**"). Heading levels are derived
  from the numbering only, so a renamed chapter keeps working.
- Sources use pandoc grid tables and `{width=...}` image attributes, which
  mdBook (pulldown-cmark) cannot render. The `src/` output is therefore
  converted with `pandoc -t gfm`; the `md/` output keeps pandoc Markdown for
  the docx/PDF builds.
- `01-contents.md` is dropped: it is a hand-made TOC with print page numbers,
  which mdBook, docx and PDF all regenerate.
"""
import logging
import re
import shutil
import subprocess
import sys
from pathlib import Path

log = logging.getLogger("prepare")

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"01-contents.md"}
LANG = {
    "zh": {"refs": "参考文献", "chapter": r"第.+章 .+"},
    "en": {"refs": "References", "chapter": r"Chapter \d+: .+"},
}
NUM = r"\d+(?:\.\d+)+"
# Orphan from the original docx conversion: an empty bold run holding a line
# break. It renders as a literal "****"; drop it from the generated inputs
# (the sources stay untouched). Remove once the sources are cleaned up.
EMPTY_BOLD = "**\\**"


def promote(lang: str, name: str, text: str) -> tuple[str, int]:
    chapter = re.compile(rf"^\*\*({LANG[lang]['chapter']})\*\*$")
    bold_num = re.compile(rf"^\*\*({NUM}) (.+?)\*\*$")
    plain_num = re.compile(rf"^({NUM}) (\S.{{0,100}})$")
    out, count = [], 0
    for line in text.split("\n"):
        line = line.rstrip()
        if line == EMPTY_BOLD:
            continue
        if m := chapter.match(line):
            out.append(f"# {m[1]}")
        elif (m := bold_num.match(line)) or (m := plain_num.match(line)):
            out.append(f"{'#' * (m[1].count('.') + 1)} {m[1]} {m[2]}")
        else:
            out.append(line)
            continue
        count += 1
    text = "\n".join(out)

    if name.startswith("00-"):
        # Title block, then the Preface title glued to the last line by a bug in
        # the original docx conversion ("...**\\\n前言**").
        text = re.sub(r"\*\*\\\n(前言|Preface)\*\*", r"\n\n# \1", text)
        text = re.sub(r"\A\*\*(.+?)\*\*", r"# \1", text, count=1)
        count += 2
    elif name.startswith("07-"):
        text = f"# {LANG[lang]['refs']}\n\n{text}"
        count += 1
    elif name.startswith("08-"):
        text = f"# {text.lstrip()}"
        count += 1
    return text, count


CITE = re.compile(r"\\\[(\d+)\\\]")
REF_ENTRY = re.compile(r"^\\\[(\d+)\\\] (.+)$")
URL = re.compile(r"https?://\S+")
CITED_TITLE = {"zh": "本章参考文献", "en": "References cited in this chapter"}


def autolink(entry: str) -> str:
    # Sources escape `_` etc. for pandoc; inside `<...>` escapes are literal.
    return URL.sub(lambda m: "<" + re.sub(r"\\([\\_*\[\]#&~])", r"\1", m[0]) + ">", entry)


def parse_refs(text: str) -> dict[int, str]:
    refs = {}
    for line in text.split("\n"):
        if m := REF_ENTRY.match(line.strip()):
            refs[int(m[1])] = m[2]
    return refs


def link_citations(lang: str, name: str, text: str, refs: dict[int, str]) -> str:
    """Link `[N]` markers to a per-page reference list and append that list.

    mdBook renumbers real footnotes per page, which would break the global
    numbering the paper uses, so the numbered list is built by hand. Anchors
    carry the file prefix so concatenated docx/PDF input keeps ids unique.
    Markers inside grid tables are left alone: rewriting them would change the
    cell width and break the grid (they are linked later, in the HTML tables).
    """
    prefix = name.split("-")[0]
    cited: set[int] = set()

    def sub(m: re.Match) -> str:
        n = int(m[1])
        if n not in refs:
            log.warning("%s cites [%d] which is missing from the references", name, n)
            return m[0]
        cited.add(n)
        return f"[{m[0]}](#c{prefix}-ref-{n})"

    body = [
        l if l[:1] in "|+" else CITE.sub(sub, l) for l in text.split("\n")
    ]
    all_cited = cited | {int(n) for n in CITE.findall(text) if int(n) in refs}
    if not all_cited:
        return text
    tail = [f"## {CITED_TITLE[lang]}", ""]
    for n in sorted(all_cited):
        tail += [f"[]{{#c{prefix}-ref-{n}}}\\[{n}\\] {autolink(refs[n])}", ""]
    return "\n".join(body).rstrip("\n") + "\n\n" + "\n".join(tail)


def link_table_citations(name: str, gfm: str) -> str:
    prefix = name.split("-")[0]

    def table(m: re.Match) -> str:
        return re.sub(
            r"\[(\d+)\]", lambda c: f'<a href="#c{prefix}-ref-{c[1]}">[{c[1]}]</a>', m[0]
        )

    return re.sub(r"<table.*?</table>", table, gfm, flags=re.S)


EMPTY_STRONG = re.compile(r"\*\*(\s+)\*\*")
STRONG = re.compile(r"\*\*(?=\S)(.+?)(?<=\S)\*\*")


def strong_to_html(gfm: str) -> str:
    """Turn `**x**` into `<strong>x</strong>` for mdBook.

    CommonMark (pulldown-cmark) refuses to close `**` that follows CJK or
    full-width punctuation and precedes a letter or CJK character, e.g.
    `**发布单位：**Datawhale`, so such runs would render as literal asterisks.
    Fenced code blocks are left alone.
    """
    out, fenced = [], False
    for line in gfm.split("\n"):
        if line.lstrip().startswith("```"):
            fenced = not fenced
        if not fenced:
            line = EMPTY_STRONG.sub(r"\1", line)  # e.g. `**　**` in table cells
            line = STRONG.sub(r"<strong>\1</strong>", line)
        out.append(line)
    return "\n".join(out)


def to_gfm(text: str) -> str:
    # `-raw_html` is NOT used: complex tables must fall back to HTML tables.
    gfm = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "gfm", "--wrap=none"],
        input=text, capture_output=True, text=True, check=True,
    ).stdout
    return strong_to_html(gfm)


# Logos drawn in white; they get a dark backing in the build copies.
LIGHT_LOGOS = {"chuanbo-danao.png"}


def trim_logos(folder: Path) -> None:
    """Crop the transparent/white margins of the logo copies (originals stay
    untouched) so logos line up with their publisher names."""
    im = shutil.which("magick") or shutil.which("convert")  # IM7 / IM6 (Ubuntu)
    if not im:
        log.warning("ImageMagick not found: logos are used untrimmed")
        return
    for f in folder.glob("*"):
        if f.suffix in {".png", ".jpg"}:
            cmd = [im, str(f), "-fuzz", "8%", "-trim", "+repage"]
            if f.name in LIGHT_LOGOS:  # white artwork: invisible on white pages
                cmd += ["-bordercolor", "none", "-border", "14", "-background", "#2b2b2b", "-alpha", "remove"]
            subprocess.run(cmd + [str(f)], check=True)


def main(lang: str) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    work = ROOT / "build" / lang
    shutil.rmtree(work, ignore_errors=True)
    (work / "src").mkdir(parents=True)
    (work / "md").mkdir()
    shutil.copytree(ROOT / "media", work / "src" / "media")
    shutil.copytree(ROOT / "media", work / "md" / "media")
    for sub in ("src", "md"):
        shutil.copytree(ROOT / "logos", work / sub / "logos")
        trim_logos(work / sub / "logos")
    shutil.copy(ROOT / "book" / lang / "book.toml", work / "book.toml")
    shutil.copy(ROOT / "scripts" / "credits.css", work / "credits.css")

    refs = parse_refs((ROOT / lang / "07-references.md").read_text(encoding="utf-8"))
    log.info("%s: %d references", lang, len(refs))
    summary = ["# Summary", ""]
    for path in sorted((ROOT / lang).glob("*.md")):
        if path.name in SKIP:
            continue
        text, n = promote(lang, path.name, path.read_text(encoding="utf-8"))
        if path.name.startswith("07-"):
            text = "\n".join(
                f"[]{{#ref-{m[1]}}}" + autolink(l) if (m := REF_ENTRY.match(l.strip())) else l
                for l in text.split("\n")
            )
        elif not path.name.startswith("08-"):
            text = link_citations(lang, path.name, text, refs)
        if n == 0:
            log.error("no headings detected in %s", path.name)
            sys.exit(1)
        (work / "md" / path.name).write_text(text, encoding="utf-8")
        gfm = link_table_citations(path.name, to_gfm(text)) if not path.name.startswith("07-") else to_gfm(text)
        (work / "src" / path.name).write_text(gfm, encoding="utf-8")
        title = next(l[2:] for l in text.split("\n") if l.startswith("# "))
        summary.append(f"- [{title}]({path.name})")
        log.info("%s/%s: %d headings", lang, path.name, n)
    (work / "src" / "SUMMARY.md").write_text("\n".join(summary) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1])
