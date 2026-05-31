# Start Here

Use this guide when adopting Engagement Stack for yourself or helping someone populate it.

## Fast Path

1. Fork or copy this repository.
2. Delete `examples/` or keep it only as reference.
3. Read [AGENTS.md](../AGENTS.md).
4. Paste [prompts/populate-engagement-stack.md](../prompts/populate-engagement-stack.md) into your coding agent.
5. Let the agent interview you and fill the scaffold.
6. Copy `private.example/` to ignored `private/` if you need private salary, constraint, or negotiation overlays.
7. Review every generated claim before sharing.
8. Run the completeness audit in [setup/completeness-audit.md](completeness-audit.md).
9. Render resume artifacts with GitHub Actions or `scripts/render-resumes.sh`.

## Do You Already Have Polished Resume(s)?

This decides whether you import or generate. Either way, the output lands in [`resumes/`](../resumes/) as two variants — **short** (~2pg) and **long** (~3pg) — both rendered with the **navy** theme.

- **YES — I have polished resume(s).** Use them as-is; Engagement Stack does not rewrite them.
  1. Drop your originals into [`resumes/originals/`](../resumes/originals/) (preserved verbatim).
  2. Place the short and long versions at `resumes/short.md` / `resumes/long.md`.
  3. **Skip** resume generation — run it only if you explicitly want to refine.
  4. Shaders still layer role/industry specifics on top without touching your originals.

- **NO — I do not have a resume yet.** Generate one: populate `cv/`, pick or write a shader in [`resume-shaders/`](../resume-shaders/), and produce `resumes/short.md` / `resumes/long.md` from there.

Then render with `scripts/render-resumes.sh` (or the **Render Resumes** GitHub Actions workflow). See [`resumes/README.md`](../resumes/README.md) for details.

## No Runtime Required

The default setup requires only GitHub, Markdown, YAML, and an agent. Local scripts are optional conveniences.

## Public And Private Data

This framework is public-first, but the user may still need private data for accurate evaluation. Public files can describe preferences and trade-off rules. Private overlays can hold actual numbers and sensitive facts.

Copy:

```sh
cp -R private.example private
```

Then fill `private/`. That folder is ignored by default.

## What To Fill First

1. `profile/identity.md`
2. `profile/positioning.md`
3. `cv/canonical-cv.md`
4. `cv/work-history.md`
5. `cv/skills.md`
6. `portfolio/README.md`
7. `engagements/current-preferences.md`
8. `engagements/evaluation-rubric.md`
9. `engagements/request-instructions.md`

## What Can Wait

- Private compensation thresholds.
- Private work authorization, current-employer, family, health, or negotiation constraints.
- Deep project case studies.
- References and testimonials.
- GitHub Pages publishing.
- USAJOBS API integration.
