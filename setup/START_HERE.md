# Start Here

Use this guide when adopting Engagement Stack for yourself or helping someone populate it.

## Fast Path

1. Fork or copy this repository.
2. Delete `examples/` or keep it only as reference.
3. Read [AGENTS.md](../AGENTS.md).
4. Paste [prompts/populate-engagement-stack.md](../prompts/populate-engagement-stack.md) into your coding agent.
5. Let the agent interview you and fill the scaffold.
6. Review every generated claim before sharing.
7. Run the completeness audit in [setup/completeness-audit.md](completeness-audit.md).
8. Render resume artifacts with GitHub Actions or `scripts/render-resumes.sh`.

## No Runtime Required

The default setup requires only GitHub, Markdown, YAML, and an agent. Local scripts are optional conveniences.

## What To Fill First

1. `profile/identity.md`
2. `profile/positioning.md`
3. `cv/canonical-cv.md`
4. `cv/work-history.md`
5. `cv/skills.md`
6. `portfolio/README.md`
7. `engagements/current-preferences.md`
8. `engagements/request-instructions.md`

## What Can Wait

- Offer scoring details.
- Private compensation thresholds.
- Deep project case studies.
- References and testimonials.
- GitHub Pages publishing.
- USAJOBS API integration.
