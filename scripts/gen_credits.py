#!/usr/bin/env python3
"""Rewrite the publisher blocks of the front matter as logo-over-name grids.

Usage: gen_credits.py   (idempotent; edits zh/ and en/00-front-matter.md)
Each grid is a pandoc grid table (renders as a table in mdBook, docx and PDF).
"""
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
H = "1.2cm"
ZH_PUB = [("hangzhoushirengongzhinengkaiyuanshengtaixueyuan.jpg", "杭州市人工智能开源生态学院")]
ZH_CO = [
    ("zhejiarengongzhinengxueyuan.jpg", "浙江省人工智能学院"),
    ("shanghai-jiaotong-daxue-xiaohui.png", "上海交通大学人工智能研究院"),
    ("shanghai-jiaotong-daxue-zhongwen-hengban.png", "上海交通大学安泰经管学院"),
    ("moda-shequ.png", "魔搭社区"),
    ("chuanbo-danao.png", "传播大脑"),
    ("chaoxinwen.png", "潮新闻"),
    ("datawhale.png", "Datawhale"),
    (None, "浙江大学人工智能教育教学研究中心"),
]
EN_PUB = [("hangzhoushirengongzhinengkaiyuanshengtaixueyuan.jpg", "Hangzhou AI Open Source Ecosystem Academy")]
EN_CO = [
    ("datawhale.png", "Datawhale"),
    ("kaiyuanshe.png", "KAIYUANSHE"),
    ("zhejiarengongzhinengxueyuan.jpg", "Zhejiang Provincial Academy of Artificial Intelligence"),
    ("shanghai-jiaotong-daxue-xiaohui.png", "Artificial Intelligence Institute, Shanghai Jiao Tong University"),
    ("shanghai-jiaotong-daxue-zhongwen-hengban.png", "Antai College of Economics and Management, Shanghai Jiao Tong University"),
    ("moda-shequ.png", "ModelScope"),
    ("chuanbo-danao.png", "Commind"),
    ("chaoxinwen.png", "Tide News"),
    (None, "Center for AI Education and Teaching Research, Zhejiang University"),
]
W = 78  # cell width in characters (must fit the longest image markup)


def cell(item):
    logo, name = item
    return [f"![](logos/{logo}){{height={H}}}" if logo else "", name]


def grid(items, cols):
    rows = [items[i:i + cols] for i in range(0, len(items), cols)]
    sep = "+" + "+".join(":" + "-" * (W - 2) + ":" for _ in range(cols)) + "+"
    out = [sep]
    for row in rows:
        cells = [cell(i) for i in row] + [["", ""]] * (cols - len(row))
        for line in (0, 1):
            # a blank line between logo and name keeps them separate paragraphs
            out.append("|" + "|".join(" " + pad(c[line], W - 1) for c in cells) + "|")
            if line == 0:
                out.append("|" + "|".join(" " * W for _ in cells) + "|")
        out.append("+" + "+".join("-" * W for _ in range(cols)) + "+")
    return "\n".join(out)


def pad(s, width):
    """Pad to a display width: pandoc counts CJK characters as two columns."""
    w = sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in s)
    return s + " " * (width - w)


def apply(path, pub_re, co_re, tail_re, pub, co, cols_pub=1, cols_co=3):
    p = ROOT / path
    t = p.read_text(encoding="utf-8")
    m = re.search(pub_re + r"\n\n.*?\n\n" + co_re + r"\n\n.*?\n\n(?=" + tail_re + ")", t, re.S)
    assert m, path
    blank = (None, "")
    pub = [blank] * ((cols_co - 1) // 2) + pub  # centre the single publisher
    new = (f"{m[1]}\n\n::: credits\n{grid(pub, cols_co)}\n:::\n\n"
           f"{m[2]}\n\n::: credits\n{grid(co, cols_co)}\n:::\n\n")
    p.write_text(t[:m.start()] + new + t[m.end():], encoding="utf-8")


apply("zh/00-front-matter.md", r"(\*\*发布方：\*\*)", r"(\*\*联合发布：\*\*)", r"\*\*二O二六年三月", ZH_PUB, ZH_CO, 1, 3)
apply("en/00-front-matter.md", r"(\*\*Published by:\*\*)", r"(\*\*Co-published by:\*\*)", r"\*\*March 2026\*\*\n\n\*\*Editorial", EN_PUB, EN_CO, 1, 3)
