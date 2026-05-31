# Resumes

Rendered, presentation-ready resume variants — distinct from the **canonical facts** in [`cv/`](../cv/) and from **content emphasis** in [`resume-shaders/`](../resume-shaders/).

Three concepts, three axes:

| Axis | Question | Lives in |
|------|----------|----------|
| **Facts** | *What is true?* | `cv/`, `portfolio/`, `evidence/` |
| **Shading** | *What should be emphasized for this target?* | `resume-shaders/` |
| **Format** | *How long, and how should it look?* | `resumes/` (here) + `styles/` |

## Variants

Two canonical lengths, both rendered with the **navy** theme (`styles/navy.css`):

- **short** — `short.md`, ~2 pages, tight density. The default submission resume; also the source for the ATS DOCX/TXT.
- **long** — `long.md`, ~3 pages, roomy density. Graduated detail: full recent roles, tapering for older ones.

A matching one-page **cover letter** lives in [`../submissions/cover-letter/`](../submissions/cover-letter/).

The machine-readable declaration is [`manifest.yaml`](manifest.yaml).

## Ground-truth first

If you **already have polished resumes**, Engagement Stack uses them as-is. It does **not** rewrite them.

1. Drop your originals into [`originals/`](originals/) (preserved verbatim, never modified).
2. Place the short and long versions at `short.md` / `long.md` (Markdown). These are marked `ground_truth: true` in the manifest.
3. The resume-*generation* steps (canonical-CV interview, draft writing) are **skipped** — run them only if you explicitly want to refine.
4. Shaders still apply **on top** for role/industry specifics, emitting tailored copies under `generated/` or `submissions/` without touching your originals.

If you do **not** have a resume yet, generate one: populate `cv/`, pick or write a shader, and produce `short.md` / `long.md` from there.

## Render

```bash
scripts/render-resumes.sh short          # navy 2-page PDF (+ ATS docx/txt)
scripts/render-resumes.sh long           # navy 3-page PDF
scripts/render-resumes.sh cover-letter   # navy 1-page letter
scripts/render-resumes.sh all            # everything
```

Outputs go to `generated/resumes/` (gitignored). No local setup? Use the **Render Resumes** GitHub Actions workflow.
