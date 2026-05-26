# Agent Instructions

You are helping maintain or use an Engagement Stack: a human-first, agent-readable Career OS for professional identity, CV, portfolio evidence, engagement preferences, offer/request handling, and job-search submissions.

Treat this repository as the source of truth. Do not invent, exaggerate, or smooth over missing evidence.

## Operating Principles

- **Read before writing.** Inspect the relevant Markdown and YAML files before generating resumes, summaries, proposals, or responses.
- **Cite local files.** When making a claim about the person, cite the file that supports it.
- **Separate fact from positioning.** A canonical fact belongs in `cv/`, `profile/`, `portfolio/`, or `evidence/`. Tailoring belongs in `submissions/` or `generated/`.
- **Respect evidence levels.** Distinguish "built", "led", "contributed", "advised", "maintained", and "observed".
- **Do not fabricate proof.** If a project lacks a live URL, repo, artifact, testimonial, or metric, say what is missing.
- **Prefer humans first.** Root and folder READMEs should stay readable by people browsing GitHub.
- **Use YAML as the control surface.** YAML files are for agents, validation, scoring, and export. Markdown remains the human source of truth.
- **Protect private overlays.** If private data is absent, do not infer it. Use placeholders or ask.

## Source-Of-Truth Order

1. `profile/` for identity, positioning, and operating style.
2. `cv/` for canonical career facts.
3. `portfolio/` for project narratives and claims.
4. `evidence/` for proof links and artifacts.
5. `engagements/` for current preferences and request handling.
6. `resume-shaders/` for role/industry-specific resume shaping instructions.
7. `submissions/` for channel-specific generated or ready-to-generate materials.
8. `generated/` for disposable outputs. Never treat generated files as canonical.

## Common Tasks

### Populate A New Stack

Use `prompts/populate-engagement-stack.md`. Interview the user, then write or update Markdown and YAML together. If the user provides an existing resume, use `prompts/import-existing-resume.md`.

### Tailor A Resume

Read `cv/canonical-cv.md`, `cv/work-history.md`, `cv/skills.md`, relevant `portfolio/projects/*`, `resume-shaders/README.md`, and any selected shader. Generate tailored source under `submissions/generated/` or `generated/resumes/`. Do not change canonical facts unless the user confirms a correction.

If the user asks for specialization by role, industry, client, or job description, create or update a resume shader rather than editing the canonical CV.

### Evaluate An Engagement Request

Read `engagements/current-preferences.md`, `engagements/current-preferences.yaml`, `engagements/evaluation-rubric.md`, `engagements/evaluation-rubric.yaml`, `engagements/offer-packet.schema.yaml`, `engagements/request-instructions.md`, and any offer packet provided. If required fields are missing, draft a clarification response before scoring. Preserve the distinction between dealbreakers, weighted preferences, and trade-off rules.

### Generate An Evaluation Rubric

Use `prompts/generate-evaluation-rubric.md` to help the user define how offers should be scored. Keep sensitive floors, private constraints, immigration details, and negotiation thresholds out of public files unless the user explicitly approves.

### Generate LinkedIn Or ATS Material

Use `submissions/linkedin/`, `submissions/ats-generic/`, and `submissions/indeed/`. Generate copy/paste-ready text and structured YAML. Do not automate platform actions unless the user explicitly asks and the platform supports compliant access.

### Use GitHub

Use `docs/agent-github-setup.md` for `gh` CLI setup, Actions, releases, and optional Pages. Do not publish generated artifacts publicly unless the user explicitly approves.

## Platform Automation Boundaries

- GitHub: supported through the official `gh` CLI.
- Pandoc: supported locally or through GitHub Actions.
- USAJOBS: official search API can be used if the user provides an API key.
- LinkedIn: generate profile/application material; do not assume API access.
- Indeed: generate application material; do not scrape or automate applications by default.
- Generic ATS: generate field packs and tailored attachments for human submission.
