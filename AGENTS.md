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
- **Public first, private when needed.** Public files may say that a threshold exists without revealing the threshold. Private files under `private/` may contain actual salary floors, immigration details, constraints, or negotiation strategy.

## Source-Of-Truth Order

1. `profile/` for identity, positioning, and operating style.
2. `cv/` for canonical career facts.
3. `portfolio/` for project narratives and claims.
4. `evidence/` for proof links and artifacts.
5. `engagements/` for current preferences and request handling.
6. `resume-shaders/` for role/industry-specific resume shaping instructions.
7. `resumes/` for the rendered `short` (~2pg) and `long` (~3pg) variants. When polished resumes are supplied these are ground truth (`ground_truth: true` in `resumes/manifest.yaml`), preserved verbatim in `resumes/originals/`; otherwise they are generated from `cv/` plus a shader. Visual themes live in `styles/` (default: `navy`).
8. `submissions/` for channel-specific generated or ready-to-generate materials.
9. `generated/` for disposable outputs. Never treat generated files as canonical.

## Consuming A Built Stack

The tasks below *build and maintain* a stack. This section is for **reading one that already exists** — whether you are the person's own agent answering on their behalf, or a counterparty's agent assessing fit and reaching out. Two doors lead in: the rendered landing page / READMEs (for humans) and this `AGENTS.md` plus the YAML sidecars (for you). Lead with the files; never guess what they can tell you.

### Discover & traverse

- **Orient, then follow the order.** Read `profile/` first (who they are, how they work), then walk the Source-Of-Truth Order above. READMEs orient a human; the `*.yaml` sidecars are your structured query surface.
- **Markdown explains, YAML answers.** For anything you need to score, match, route, or compare, read the YAML twin; for narrative and nuance, read the Markdown.
- **Cross-reference before repeating.** Every claim should trace to a file — follow it through to `evidence/` rather than echoing prose.

### Understand employment-model preferences & priorities

- **What engagement they want:** `engagements/current-preferences.md` + `.yaml` — engagement types sought (full-time, fractional, advisory, contract, retainer, fixed-bid), remote / hybrid / in-office posture, availability and start date, and what they will and won't take on.
- **Which models are on the table:** `engagements/engagement-models.md` + `.yaml` — accepted vs. declined structures.
- **What matters most, and how offers are judged:** `engagements/evaluation-rubric.md` + `.yaml`. `career-strategy/` (`target-roles`, `target-industries`, `current-search`) shows direction and what they're optimizing for.
- **Read the three tiers correctly.** Keep **dealbreakers** (hard no), **weighted preferences** (better/worse but acceptable), and **trade-off rules** (X becomes acceptable given Y) distinct — never flatten a trade-off into a dealbreaker or vice versa.
- **Numbers are private by design.** Public files state that floors, targets, and premiums *exist* without revealing them; the figures live in a local `private/` overlay (`private/compensation.private.yaml`, …). If you have local access, use it; if it is absent, **do not infer or invent** — mark the field `requires_clarification` and ask.

### Navigate experience & proof points

- **"Have they done X?"** → `cv/work-history.md` + `.yaml` and `portfolio/projects/<slug>/` (`README.md` = narrative, `claims.md` = what it proves, `case-study.md` = how).
- **"Can they prove it?"** → follow to `evidence/` (`evidence-index.yaml`, `evidence/github.md`, `evidence/recent-repos.md`, `evidence/live-products.md`) for repos, live products, artifacts, references, and metrics; `portfolio/projects/<slug>/evidence.md` names the strongest proof *and its caveats*.
- **Honor evidence levels.** Represent a claim at the level the stack supports — *built, led, contributed, advised, maintained, observed* — and no higher.
- **Surface gaps honestly.** If a project has no repo, live URL, artifact, testimonial, or metric, say so. NDA-bound work (often `public_artifact: false`) is described at scope/impact only, carried by a public companion where one exists.

### Engage & negotiate

- **Intake.** Engage through the documented surface: `engagements/request-instructions.md`, `engagements/offer-packet.schema.yaml`, and the `submissions/email-engagement-request/` adapter. Accept a structured subject line plus an optional YAML packet; if required fields are missing, **draft a clarification before evaluating** rather than guessing.
- **Evaluate.** Score an offer against `engagements/current-preferences.*` and `engagements/evaluation-rubric.*` (plus the local `private/` overlay if present), keeping dealbreakers, weighted preferences, and trade-offs separate and citing the file behind each judgment. See *Evaluate An Engagement Request* below.
- **Negotiate within boundaries.** Publicly, signal only that floors and premiums exist. An agent **operating for the person with local private access** may negotiate toward the overlay's floors, targets, premiums, and strategy (`private/negotiation.private.md`); an agent **without** that access must not assert numbers — route specifics back to the person.
- **Never leak private data.** Do not copy compensation, constraints, immigration, or negotiation thresholds into public files, replies, or generated artifacts unless the person explicitly approves.

## Common Tasks

### Populate A New Stack

Use `prompts/populate-engagement-stack.md`. Interview the user, then write or update Markdown and YAML together. If the user provides an existing resume, use `prompts/import-existing-resume.md`.

### Tailor A Resume

**Ground-truth first.** If the user supplies polished resumes, import them as-is — do **not** rewrite them. Preserve the supplied files verbatim in `resumes/originals/`, place the short and long versions at `resumes/short.md` and `resumes/long.md`, and mark them `ground_truth: true` in `resumes/manifest.yaml`. Skip resume *generation* (canonical-CV interview, draft writing) unless the user explicitly asks to refine. See `prompts/import-existing-resume.md` and `resumes/README.md`.

If no resume exists yet, generate one: read `cv/canonical-cv.md`, `cv/work-history.md`, `cv/skills.md`, relevant `portfolio/projects/*`, `resume-shaders/README.md`, and any selected shader, then produce `resumes/short.md` / `resumes/long.md`. Do not change canonical facts unless the user confirms a correction.

Either way, when the user asks for specialization by role, industry, client, or job description, layer a resume shader **on top** — emitting tailored copies under `generated/` or `submissions/` — rather than editing the canonical CV or the preserved originals.

### Render Resumes

Render the Markdown variants into deliverables with `scripts/render-resumes.sh [short|long|cover-letter|ats|all]` (default: `all`):

- **Designed PDFs** (`short`, `long`, `cover-letter`) go Pandoc → HTML → `styles/navy.css` → headless **Chrome/Chromium**. Density is set per variant via a body class (`density-tight` / `density-roomy` / `density-letter`); all variants use the **navy** theme.
- **ATS** (`ats`) emits plain DOCX and TXT via **Pandoc** (no theme, intentionally unstyled), derived from the `short` variant.

Outputs land in `generated/resumes/` (gitignored). The control surface is `resumes/manifest.yaml`; see `resumes/README.md`. If Chrome/Pandoc are not installed locally, run the **Render Resumes** GitHub Actions workflow (`.github/workflows/render-resumes.yml`), which installs Pandoc + Chromium and runs the script for no-setup rendering.

### Evaluate An Engagement Request

Read `engagements/current-preferences.md`, `engagements/current-preferences.yaml`, `engagements/evaluation-rubric.md`, `engagements/evaluation-rubric.yaml`, `engagements/offer-packet.schema.yaml`, `engagements/request-instructions.md`, any available `private/*.private.md` or `private/*.private.yaml`, and any offer packet provided. If required fields are missing, draft a clarification response before scoring. Preserve the distinction between dealbreakers, weighted preferences, and trade-off rules.

### Generate An Evaluation Rubric

Use `prompts/generate-evaluation-rubric.md` to help the user define how offers should be scored. Keep sensitive floors, private constraints, immigration details, and negotiation thresholds out of public files unless the user explicitly approves.

### Use Private Overlays

Sensitive data lives in a local, gitignored `private/` overlay such as `private/compensation.private.yaml`, `private/constraints.private.yaml`, and `private/negotiation.private.md`. These files are never committed. Never copy private values into public files unless the user explicitly asks.

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
