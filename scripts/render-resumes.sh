#!/usr/bin/env sh
set -eu

SOURCE="${1:-cv/resume-source.md}"
OUT_DIR="${2:-generated/resumes}"

mkdir -p "$OUT_DIR"

copy_markdown_sources() {
  cp "$SOURCE" "$OUT_DIR/resume-one-page.md"
  cp "$SOURCE" "$OUT_DIR/resume-two-page.md"
  cp "$SOURCE" "$OUT_DIR/resume-ats.md"
  cp "$SOURCE" "$OUT_DIR/resume-full-cv.md"
  cp "$SOURCE" "$OUT_DIR/resume-usajobs.md"
}

render_with_pandoc() {
  pandoc "$SOURCE" -s -o "$OUT_DIR/resume-one-page.pdf"
  pandoc "$SOURCE" -s -o "$OUT_DIR/resume-two-page.pdf"
  pandoc "$SOURCE" -s -o "$OUT_DIR/resume-ats.docx"
  pandoc "$SOURCE" -t plain -o "$OUT_DIR/resume-ats.txt"
  pandoc "$SOURCE" -s -o "$OUT_DIR/resume-full-cv.pdf"
  pandoc "$SOURCE" -s -o "$OUT_DIR/resume-usajobs.pdf"
}

render_with_docker() {
  docker run --rm --volume "$(pwd):/data" --user "$(id -u):$(id -g)" pandoc/latex "$SOURCE" -s -o "$OUT_DIR/resume-one-page.pdf"
  docker run --rm --volume "$(pwd):/data" --user "$(id -u):$(id -g)" pandoc/latex "$SOURCE" -s -o "$OUT_DIR/resume-two-page.pdf"
  docker run --rm --volume "$(pwd):/data" --user "$(id -u):$(id -g)" pandoc/latex "$SOURCE" -s -o "$OUT_DIR/resume-ats.docx"
  docker run --rm --volume "$(pwd):/data" --user "$(id -u):$(id -g)" pandoc/core "$SOURCE" -t plain -o "$OUT_DIR/resume-ats.txt"
  docker run --rm --volume "$(pwd):/data" --user "$(id -u):$(id -g)" pandoc/latex "$SOURCE" -s -o "$OUT_DIR/resume-full-cv.pdf"
  docker run --rm --volume "$(pwd):/data" --user "$(id -u):$(id -g)" pandoc/latex "$SOURCE" -s -o "$OUT_DIR/resume-usajobs.pdf"
}

if command -v pandoc >/dev/null 2>&1; then
  copy_markdown_sources
  render_with_pandoc
elif command -v docker >/dev/null 2>&1; then
  copy_markdown_sources
  render_with_docker
else
  echo "Pandoc or Docker is required for local rendering. Use the GitHub Actions workflow to render without local setup." >&2
  exit 1
fi

echo "Rendered resume artifacts into $OUT_DIR"
