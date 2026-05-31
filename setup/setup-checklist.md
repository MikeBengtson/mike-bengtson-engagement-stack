# Setup Checklist

- [ ] Replace placeholder identity fields.
- [ ] Fill canonical CV facts.
- [ ] Add at least three work history entries or mark why fewer exist.
- [ ] Add at least one portfolio project.
- [ ] Add proof links for every public claim where possible.
- [ ] Fill current engagement preferences.
- [ ] Fill evaluation rubric trade-offs or mark defaults as intentional.
- [ ] Copy `private.example/` to ignored `private/` if private thresholds or constraints are needed.
- [ ] Confirm private overlays are not staged in git.
- [ ] Fill contact and request instructions.
- [ ] Review LinkedIn export material.
- [ ] Decide: do you already have polished resume(s)?
  - [ ] YES — import them as-is into `resumes/` (`short.md` ~2pg, `long.md` ~3pg) and preserve originals in `resumes/originals/`; skip resume generation.
  - [ ] NO — generate `resumes/short.md` / `resumes/long.md` from `cv/` plus a shader in `resume-shaders/`.
- [ ] Render resume artifacts (navy theme) via `scripts/render-resumes.sh` or the Render Resumes workflow.
- [ ] Remove or keep `examples/` intentionally.
- [ ] Keep or remove the framework link-back intentionally.
