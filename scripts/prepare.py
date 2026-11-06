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


def promote(lang: str, name: str, text: str) -> tuple[str, int]:
    chapter = re.compile(rf"^\*\*({LANG[lang]['chapter']})\*\*$")
    bold_num = re.compile(rf"^\*\*({NUM}) (.+?)\*\*$")
    plain_num = re.compile(rf"^({NUM}) (\S.{{0,100}})$")
    out, count = [], 0
    for line in text.split("\n"):
        line = line.rstrip()
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


def to_gfm(text: str) -> str:
    # `-raw_html` is NOT used: complex tables must fall back to HTML tables.
    return subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "gfm", "--wrap=none"],
        input=text, capture_output=True, text=True, check=True,
    ).stdout


def main(lang: str) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    work = ROOT / "build" / lang
    shutil.rmtree(work, ignore_errors=True)
    (work / "src").mkdir(parents=True)
    (work / "md").mkdir()
    shutil.copytree(ROOT / "media", work / "src" / "media")
    shutil.copytree(ROOT / "media", work / "md" / "media")
    shutil.copy(ROOT / "book" / lang / "book.toml", work / "book.toml")

    summary = ["# Summary", ""]
    for path in sorted((ROOT / lang).glob("*.md")):
        if path.name in SKIP:
            continue
        text, n = promote(lang, path.name, path.read_text(encoding="utf-8"))
        if n == 0:
            log.error("no headings detected in %s", path.name)
            sys.exit(1)
        (work / "md" / path.name).write_text(text, encoding="utf-8")
        (work / "src" / path.name).write_text(to_gfm(text), encoding="utf-8")
        title = next(l[2:] for l in text.split("\n") if l.startswith("# "))
        summary.append(f"- [{title}]({path.name})")
        log.info("%s/%s: %d headings", lang, path.name, n)
    (work / "src" / "SUMMARY.md").write_text("\n".join(summary) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1])
