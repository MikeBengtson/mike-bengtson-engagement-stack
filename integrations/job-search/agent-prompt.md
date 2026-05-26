# Produce An Engagement Stack Export

At the end of a job-search strategy session, produce two files for Engagement Stack:

1. `job-search-report.md`
2. `job-search-export.yaml`

Use the schema in `integrations/job-search/job-search-export.schema.yaml`.

Do not invent canonical CV facts. Mark recommendations as recommendations, not facts.

If you identify possible resume specializations, emit them as `resume_shader_recommendations` rather than rewriting the canonical CV.

Each shader recommendation must include:

- `name`
- `slug`
- `description`
- `rationale`
- `target.role`
- `target.industry`
- `target.seniority`
- `target.platform`
- `emphasize`
- `deemphasize`
- `preferred_terms`
- `avoid_terms`
- `evidence_gaps`
- `source_report_sections`

Descriptions should be useful to a human deciding whether to maintain that tailored resume variant. Structured fields should be useful to an agent creating `resume-shaders/<slug>.md` and `resume-shaders/<slug>.yaml`.
