# Import Existing Resume Or CV

Use this when the user provides an existing resume, CV, LinkedIn export, website bio, or work-history document.

**Ground-truth first: if a polished resume is supplied, treat it as the source of truth and use it as-is. Do not rewrite, reword, or "improve" it.**

Read:

- `AGENTS.md`
- `resumes/README.md`
- `resumes/manifest.yaml`
- `cv/README.md`

Steps:

1. **Preserve the originals verbatim.** Copy each supplied document, unchanged, into `resumes/originals/`. These are never modified.
2. **Place the working variants.** Put the ~2-page version at `resumes/short.md` and the ~3-page version at `resumes/long.md`, both in Markdown. If the user supplied only one length, place it as the closer match and ask whether to derive the other (derivation is the only case where you reshape content, and only with confirmation).
3. **Mark ground truth.** Set `ground_truth: true` for the imported variant(s) in `resumes/manifest.yaml`. Confirm `theme: navy` and the appropriate `density` (`tight` for short, `roomy` for long).
4. **Skip generation.** Do not run the canonical-CV interview or draft new resume prose. The generation path is for users with *no* resume. Run it only if the user explicitly asks to refine.
5. **Extract facts without altering the resume.** Pull canonical facts (roles, dates, organizations, skills, education) into `cv/` and generate any missing YAML sidecars. This populates the stack; it does not change the imported resume.
6. **Produce a gap list.** Note missing dates, unclear roles, unsupported claims, and stale links — as observations, not edits.

Then optionally offer:

- **Role/industry shading.** Layer a resume shader **on top** of the ground-truth variants to emit tailored copies under `generated/` or `submissions/`, never touching `resumes/originals/` or the imported `short.md` / `long.md`. See `prompts/create-resume-shader.md`.
- **Rendering.** Produce deliverables with `scripts/render-resumes.sh [short|long|cover-letter|ats|all]` — navy PDFs via headless Chrome, plain ATS DOCX/TXT via Pandoc, into `generated/resumes/`. No local setup? Use the **Render Resumes** GitHub Actions workflow.

Do not overwrite canonical facts, the preserved originals, or the imported variants without explicit confirmation.
