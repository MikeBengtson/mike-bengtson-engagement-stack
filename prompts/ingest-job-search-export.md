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
- `submissions/ats-generic/field-pack.md`

Ask before changing canonical work-history facts.
