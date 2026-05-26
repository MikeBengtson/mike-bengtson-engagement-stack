# Ingest Job Search Export

Use this when another workflow produces `job-search-report.md` and `job-search-export.yaml`.

Read:

- `integrations/job-search/job-search-export.schema.yaml`
- the provided export files

Then map the export into:

- `career-strategy/current-search.md` if present, or create it
- `submissions/linkedin/job-search-request.md`
- `engagements/current-preferences.md`
- `engagements/current-preferences.yaml`
- `cv/skills.md`
- `resume-shaders/<slug>.md` and `resume-shaders/<slug>.yaml` for approved shader recommendations
- `submissions/ats-generic/field-pack.md`

Ask before changing canonical work-history facts.

## Resume Shader Ingestion

For each `resume_shader_recommendations` item:

1. Read `name`, `slug`, `description`, `rationale`, `target`, `emphasize`, `deemphasize`, `preferred_terms`, `avoid_terms`, `evidence_gaps`, and `source_report_sections`.
2. Present the shader option to the user in human-readable form before creating files.
3. If the user approves it, create or update:
   - `resume-shaders/<slug>.md` for the human strategy, using `description`, `rationale`, evidence gaps, and source report sections.
   - `resume-shaders/<slug>.yaml` for the agent control surface, mapping `target`, `emphasize`, `deemphasize`, and language fields into the `resume_shader/v1` shape.
4. Do not generate a final resume until the user approves the shader.
5. Put unsupported claims in the shader's evidence gaps rather than adding them to the canonical CV.
