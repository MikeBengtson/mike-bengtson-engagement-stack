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
- `engagements/evaluation-rubric.md` and `engagements/evaluation-rubric.yaml` for public-safe compensation posture and trade-off rules
- `private/compensation.private.yaml` for private annual salary and contractor hourly-rate min/target/max values, only if the user approves storing them locally
- `cv/skills.md`
- `resume-shaders/<slug>.md` and `resume-shaders/<slug>.yaml` for approved shader recommendations
- `submissions/ats-generic/field-pack.md`

Ask before changing canonical work-history facts.

## Compensation Preference Ingestion

Read `compensation_preferences` from the export when present:

- `annual_salary_min`
- `annual_salary_target`
- `annual_salary_max`
- `hourly_rate_min`
- `hourly_rate_target`
- `hourly_rate_max`
- `hourly_rate_basis`
- `notes`

If the export recommends contract, freelance, fractional, advisory, or other non-salary engagement types but does not include `hourly_rate_min` and `hourly_rate_max`, switch to interview mode before finalizing the rubric. Ask the user:

1. What is your minimum acceptable contractor hourly rate?
2. What is your target contractor hourly rate?
3. What is your stretch or maximum quoted contractor hourly rate?
4. What is the rate basis: W2 contract, 1099, corp-to-corp, retainer-equivalent, or something else?
5. Should these numbers be stored privately under `private/compensation.private.yaml`?

Keep actual salary and hourly-rate numbers out of public files unless the user explicitly approves public storage. Public files can state that contractor rates exist privately and describe the trade-off logic.

## Resume Shader Ingestion

For each `resume_shader_recommendations` item:

1. Read `name`, `slug`, `description`, `rationale`, `target`, `emphasize`, `deemphasize`, `preferred_terms`, `avoid_terms`, `evidence_gaps`, and `source_report_sections`.
2. Present the shader option to the user in human-readable form before creating files.
3. If the user approves it, create or update:
   - `resume-shaders/<slug>.md` for the human strategy, using `description`, `rationale`, evidence gaps, and source report sections.
   - `resume-shaders/<slug>.yaml` for the agent control surface, mapping `target`, `emphasize`, `deemphasize`, and language fields into the `resume_shader/v1` shape.
4. Do not generate a final resume until the user approves the shader.
5. Put unsupported claims in the shader's evidence gaps rather than adding them to the canonical CV.
