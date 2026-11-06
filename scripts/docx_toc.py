#!/usr/bin/env python3
"""Lay out a pandoc .docx like the PDF: title page | contents | publisher
page | Preface onwards.

Pandoc always emits the TOC block first, so it is relocated to right after the
book title (the first Heading 1), which is centred on its own page. A page
break is also added before the second Heading 1 (the Preface), so the
publisher/credits block gets its own page. Every later Heading 1 (chapters,
references, appendix) starts a new page.

usage: docx_toc.py FILE.docx
"""
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}


def page_break() -> etree._Element:
    p = etree.Element(f"{{{W}}}p")
    r = etree.SubElement(p, f"{{{W}}}r")
    etree.SubElement(r, f"{{{W}}}br").set(f"{{{W}}}type", "page")
    return p


def main(path: Path) -> None:
    with zipfile.ZipFile(path) as z:
        items = [(i, z.read(i.filename)) for i in z.infolist()]
    doc = next(d for i, d in items if i.filename == "word/document.xml")
    root = etree.fromstring(doc)
    body = root.find("w:body", NS)

    toc = next(
        (c for c in body if c.tag == f"{{{W}}}sdt" and c.find(".//w:docPartGallery", NS) is not None),
        None,
    )
    if toc is None:
        sys.exit("docx_toc: no TOC block found")
    h1 = [
        c for c in body
        if c.tag == f"{{{W}}}p"
        and c.find("w:pPr/w:pStyle", NS) is not None
        and c.find("w:pPr/w:pStyle", NS).get(f"{{{W}}}val") == "Heading1"
    ]
    if len(h1) < 2:
        sys.exit("docx_toc: expected a title and a Preface heading")
    title, preface = h1[0], h1[1]
    body.remove(toc)
    title.addnext(page_break())
    title.getnext().addnext(toc)
    toc.addnext(page_break())
    preface.addprevious(page_break())

    # Every later chapter (Heading 1) starts on a new page, as in the PDF.
    for h in h1[2:]:
        ppr = h.find("w:pPr", NS)
        anchor = [e for e in ppr if e.tag in (f"{{{W}}}pStyle", f"{{{W}}}keepNext", f"{{{W}}}keepLines")][-1]
        anchor.addnext(etree.Element(f"{{{W}}}pageBreakBefore"))

    # Add line spacing to publisher logo paragraphs so wrapped rows don't touch.
    pic_ns = "http://schemas.openxmlformats.org/drawingml/2006/picture"
    for p in body.findall("w:p", NS):
        if any("logos/" in c.get("descr", "") for c in p.findall(f".//{{{pic_ns}}}cNvPr")):
            ppr = p.find("w:pPr", NS)
            if ppr is None:
                ppr = etree.Element(f"{{{W}}}pPr")
                p.insert(0, ppr)
            sp = etree.SubElement(ppr, f"{{{W}}}spacing")
            for k, v in (("before", "180"), ("after", "180"), ("line", "340"), ("lineRule", "auto")):
                sp.set(f"{{{W}}}{k}", v)

    # Centre the title in the upper third of its page.
    ppr = title.find("w:pPr", NS)
    for tag, attrs in (("spacing", {"before": "4800", "after": "240"}), ("jc", {"val": "center"})):
        el = etree.SubElement(ppr, f"{{{W}}}{tag}")
        for k, v in attrs.items():
            el.set(f"{{{W}}}{k}", v)

    new = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)
    tmp = Path(tempfile.mkstemp(suffix=".docx")[1])
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for info, data in items:
            z.writestr(info, new if info.filename == "word/document.xml" else data)
    shutil.move(tmp, path)


if __name__ == "__main__":
    main(Path(sys.argv[1]))
