# Job Search Integration

`../job-search` is currently a standalone skill, not a full repo. It provides a strategic job-search and resume-optimization workflow.

Engagement Stack should remain the durable Career OS. Job-search workflows can feed it through an export packet.

## Recommended Relationship

Keep them separate:

- **`job-search`** is an advisory workflow. It researches the market, interviews the user, identifies target roles/industries, and recommends positioning.
- **Engagement Stack** is the durable source of truth. It stores canonical facts, evidence, preferences, resume shaders, generated outputs, and maintenance history.

The handoff is an optional export packet. `job-search` should not directly rewrite the user's Engagement Stack unless the user asks an agent to perform ingestion.

## Contract

An upstream job-search agent may produce:

```text
job-search-report.md
job-search-export.yaml
```

Engagement Stack can ingest those files using [../../prompts/ingest-job-search-export.md](../../prompts/ingest-job-search-export.md).

## Handoff Flow

1. Run the job-search workflow.
2. Ask it to produce an Engagement Stack export.
3. Save `job-search-report.md` and `job-search-export.yaml`.
4. In this repo, use [../../prompts/ingest-job-search-export.md](../../prompts/ingest-job-search-export.md).
5. Review changes before committing.

## Mapping

| Job-search output | Engagement Stack destination |
| --- | --- |
| target roles | `career-strategy/target-roles.yaml`, `career-strategy/current-search.md` |
| target industries | `career-strategy/target-industries.yaml`, `career-strategy/current-search.md` |
| transferable skills | `cv/skills.md`, `cv/skills.yaml` after user review |
| employment type recommendations | `engagements/current-preferences.md`, `engagements/current-preferences.yaml` after user review |
| geographic preferences | `engagements/current-preferences.yaml` and `engagements/evaluation-rubric.yaml` after user review |
| compensation preferences | `engagements/evaluation-rubric.md`, `engagements/evaluation-rubric.yaml`, or `private/compensation.private.yaml` after user review; contractor paths should include hourly min/target/max and rate basis |
| resume recommendations | `resume-shaders/` or `prompts/create-resume-shader.md` after user review |
| resume shader recommendations | proposed `resume-shaders/<slug>.md` and `resume-shaders/<slug>.yaml` using the exported description, rationale, target, emphasis, language, and evidence-gap fields |
| LinkedIn recommendations | `submissions/linkedin/` |
| next steps | `career-strategy/recommendations.md` |

## Canonical Fact Boundary

The job-search export is advisory. It may recommend positioning, target roles, and resume changes, but it is not canonical proof. Do not copy claims into `cv/` or `portfolio/` unless the user confirms them and evidence exists.

## Shader Recommendation Contract

`resume_shader_recommendations` are option descriptions, not generated resumes. Each recommendation should include:

- `name` and `slug` for the proposed shader;
- `description` explaining the tailored resume strategy in human language;
- `rationale` tying the shader to the job-search report;
- `target` fields for role, industry, seniority, and platform;
- `emphasize`, `deemphasize`, `preferred_terms`, and `avoid_terms` for agent shaping;
- `evidence_gaps` for claims that need proof before use.

During ingestion, create shader files only after user approval. The shader can then generate Markdown-native scoped resume source, PDF, DOCX, or TXT outputs through the normal Engagement Stack resume flow.
