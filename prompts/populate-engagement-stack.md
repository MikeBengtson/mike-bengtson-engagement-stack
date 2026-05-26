# Populate This Engagement Stack

You are helping me populate an Engagement Stack: a human-first, agent-readable Career OS for my CV, work history, portfolio evidence, engagement preferences, and job-search submission materials.

Read these files first:

- `README.md`
- `AGENTS.md`
- `setup/START_HERE.md`
- `setup/required-files.md`
- `private.example/README.md`

Then interview me in stages. Ask no more than five questions at a time. After each stage, write or update the relevant Markdown and YAML files.

## Stage 1: Identity And Positioning

Collect:

- public name / professional handle
- current professional label
- location and time-zone posture
- public links
- one-line positioning
- short bio
- best-fit work
- work that is not a fit

Update:

- `profile/identity.md`
- `profile/identity.yaml`
- `profile/positioning.md`
- `profile/positioning.yaml`

## Stage 2: CV Facts

Collect:

- current and past roles
- dates
- organizations
- engagement type
- scope
- outcomes
- skills
- education/credentials

Update:

- `cv/canonical-cv.md`
- `cv/canonical-cv.yaml`
- `cv/work-history.md`
- `cv/work-history.yaml`
- `cv/skills.md`
- `cv/skills.yaml`
- `cv/education.md`
- `cv/education.yaml`

## Stage 3: Portfolio And Evidence

Collect:

- projects
- role on each project
- repo/live/product links
- claims each project proves
- strongest caveats or missing proof

Update:

- `portfolio/README.md`
- `portfolio/portfolio.yaml`
- `portfolio/projects/<slug>/`
- `evidence/`

## Stage 4: Engagement Preferences

Collect:

- desired engagement types
- remote/hybrid/in-office preferences
- availability
- dealbreakers
- offer evaluation priorities
- trade-offs that would make weaker-fit opportunities acceptable
- request intake preferences

Update:

- `engagements/current-preferences.md`
- `engagements/current-preferences.yaml`
- `engagements/engagement-models.md`
- `engagements/engagement-models.yaml`
- `engagements/evaluation-rubric.md`
- `engagements/evaluation-rubric.yaml`
- `engagements/offer-packet.schema.yaml`
- `engagements/request-instructions.md`

Use `prompts/generate-evaluation-rubric.md` if the user wants a deeper rubric interview.

## Stage 5: Submission Adapters

Generate first-pass:

- LinkedIn headline/about/experience material
- ATS field pack
- Indeed profile pack
- resume source targets
- base resume shader

Update:

- `submissions/linkedin/`
- `submissions/ats-generic/`
- `submissions/indeed/`
- `cv/resume-source.md`
- `resume-shaders/`

## Rules

- Do not invent facts.
- Mark missing evidence explicitly.
- Keep private or sensitive details out of public files unless I approve.
- Use ignored `private/` overlays for salary floors, sensitive constraints, work authorization details, and negotiation thresholds.
- Keep Markdown human-readable and YAML parseable.
- Cite which files you changed after each stage.
