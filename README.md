# China AI Open Source Ecosystem Blue Paper 2026 / 中国人工智能开源生态蓝皮书

Sources are in `zh/` (Chinese) and `en/` (English). CI publishes the website, PDF and Word files to GitHub Pages.

## Build locally

Requires `python3`, `pandoc`, `mdbook` (0.5.x) and `weasyprint` (plus a CJK font).

```sh
scripts/build.sh   # output in ./site
```

Outputs: `site/zh/`, `site/en/` (mdBook), `site/downloads/*.{pdf,docx}`.

## How it works

`scripts/prepare.py` turns the pandoc-style sources into mdBook input: it adds Markdown headings from chapter numbering, converts grid tables to HTML tables, and drops `01-contents.md` (mdBook, PDF and Word generate their own tables of contents).

## One-time setup

In the repository settings, set **Pages → Source** to **GitHub Actions**.
