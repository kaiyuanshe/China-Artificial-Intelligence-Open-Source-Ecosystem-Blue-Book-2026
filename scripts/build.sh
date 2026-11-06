#!/usr/bin/env bash
# Build site (mdBook), DOCX (pandoc) and PDF (pandoc -> HTML -> WeasyPrint)
# for every language into ./site. Needs: python3, pandoc, mdbook, weasyprint.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
rm -rf site && mkdir -p site/downloads


for lang in zh en; do
  # No associative arrays: macOS ships bash 3.2.
  case "$lang" in
    zh) NAME="中国人工智能开源生态蓝皮书"; LOCALE="zh" ;;
    en) NAME="China-AI-Open-Source-Ecosystem-Blue-Paper"; LOCALE="en" ;;
  esac
  echo "==> [$lang] prepare"
  python3 scripts/prepare.py "$lang"
  work="build/$lang"

  echo "==> [$lang] mdbook"
  (cd "$work" && mdbook build -d "$ROOT/site/$lang")

  echo "==> [$lang] docx"
  (cd "$work/md" && pandoc --from markdown --to docx --toc --toc-depth=3 \
      --metadata "lang=$LOCALE" --resource-path=. \
      -o "$ROOT/site/downloads/$NAME.docx" $(ls *.md | sort))

  echo "==> [$lang] pdf"
  (cd "$work/md" && pandoc --from markdown --to html5 --standalone --embed-resources \
      --toc --toc-depth=2 --metadata "lang=$LOCALE" \
      --metadata "title=$(grep -m1 '^# ' 00-front-matter.md | cut -c3-)" \
      --css "$ROOT/scripts/pdf.css" --resource-path=. \
      -o ../book.html $(ls *.md | sort))
  weasyprint --quiet "$work/book.html" "site/downloads/$NAME.pdf"
done

cp scripts/index.html site/index.html
touch site/.nojekyll
ls -lh site/downloads
