#!/usr/bin/env bash
# Render resume + cover-letter variants from Markdown using the navy theme.
#
#   Designed PDFs : pandoc (md -> HTML body) -> embed styles/<theme>.css + density class
#                   -> headless Chrome --print-to-pdf
#   ATS outputs   : pandoc -> DOCX (plain) and TXT (plain)
#
# Variants are declared in resumes/manifest.yaml and follow these conventions:
#   short        -> resumes/short.md                          (tight,  ~2 pages)
#   long         -> resumes/long.md                           (roomy,  ~3 pages)
#   cover-letter -> submissions/cover-letter/cover-letter.md  (letter, 1 page)
#
# Usage:  scripts/render-resumes.sh [short|long|cover-letter|ats|all]   (default: all)
#
# Local rendering needs Pandoc (+ Chrome/Chromium for the designed PDFs).
# No local setup? Use the "Render Resumes" GitHub Actions workflow instead.
set -uo pipefail
cd "$(dirname "$0")/.."

THEME="styles/navy.css"
OUT="generated/resumes"
mkdir -p "$OUT"

command -v pandoc >/dev/null 2>&1 || { echo "Pandoc is required (brew install pandoc) or use GitHub Actions." >&2; exit 1; }

find_chrome() {
  for p in \
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser" \
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" \
    "/Applications/Chromium.app/Contents/MacOS/Chromium" \
    "$(command -v google-chrome 2>/dev/null || true)" \
    "$(command -v chromium 2>/dev/null || true)" \
    "$(command -v chromium-browser 2>/dev/null || true)" \
    "$(command -v chrome 2>/dev/null || true)"; do
    [ -n "${p:-}" ] && [ -x "$p" ] && { printf '%s' "$p"; return 0; }
  done
  return 1
}

# render_pdf <source.md> <density> <out-basename>
render_pdf() {
  src="$1"; density="$2"; out="$3"
  if [ ! -f "$src" ]; then echo "· skip (missing source): $src"; return 0; fi
  body="$(pandoc "$src" -f gfm -t html5)"
  html="$OUT/$out.html"
  {
    printf '%s\n' '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Resume</title><style>'
    cat "$THEME"
    printf '%s\n' '</style></head><body class="density-'"$density"'">'
    printf '%s\n' "$body"
    printf '%s\n' '</body></html>'
  } > "$html"

  chrome="$(find_chrome || true)"
  if [ -n "${chrome:-}" ]; then
    "$chrome" --headless=new --no-sandbox --no-pdf-header-footer \
      --no-first-run --no-default-browser-check --disable-gpu \
      --print-to-pdf="$OUT/$out.pdf" "file://$PWD/$html" >/dev/null 2>&1 || true
    if [ -f "$OUT/$out.pdf" ]; then echo "✓ $OUT/$out.pdf"; else echo "⚠ $out.pdf not produced (Chrome failed)"; fi
  else
    echo "⚠ No Chrome/Chromium found — wrote $html (open and Print ▸ Save as PDF, or use GitHub Actions)."
  fi
}

# render_ats <source.md>  -> ATS-friendly DOCX + TXT (intentionally plain)
render_ats() {
  src="$1"
  if [ ! -f "$src" ]; then echo "· skip ATS (missing source): $src"; return 0; fi
  pandoc "$src" -f gfm -s -o "$OUT/resume-ats.docx" && echo "✓ $OUT/resume-ats.docx" || echo "⚠ docx skipped"
  pandoc "$src" -f gfm -t plain -o "$OUT/resume-ats.txt" && echo "✓ $OUT/resume-ats.txt"  || echo "⚠ txt skipped"
}

target="${1:-all}"
case "$target" in
  short)        render_pdf resumes/short.md tight resume-short ;;
  long)         render_pdf resumes/long.md  roomy resume-long ;;
  cover-letter) render_pdf submissions/cover-letter/cover-letter.md letter cover-letter ;;
  ats)          render_ats resumes/short.md ;;
  all)
    render_pdf resumes/short.md tight  resume-short
    render_pdf resumes/long.md  roomy  resume-long
    render_pdf submissions/cover-letter/cover-letter.md letter cover-letter
    render_ats resumes/short.md
    ;;
  *) echo "usage: $0 [short|long|cover-letter|ats|all]" >&2; exit 2 ;;
esac

echo "Done → $OUT"
