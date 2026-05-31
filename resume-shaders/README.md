# Resume Shaders

A resume shader is guidance for generating a scoped resume from canonical career materials.

The canonical CV answers: **what is true?**

A resume shader answers: **how should those truths be emphasized for this target?**

## Content, Not Format

Shaders are the **content-emphasis** axis. They are **orthogonal to format and length**.

- **Shading** (here) decides *what to emphasize* for a role, industry, client, or job description.
- **Format and length** (`resumes/` + `styles/`) decide *how long and how it looks* — the short (~2pg) and long (~3pg) variants and the navy theme.

A shader applies **on top of** a supplied ground-truth resume to layer in industry/role specifics, **or** drives generation from the canonical `cv/` when no resume exists yet. It never sets page count or visual styling — that is the job of `resumes/`.

## Why This Exists

People rarely submit one universal resume. They keep a core resume, then tailor it for:

- a role;
- an industry;
- a client;
- a platform;
- a seniority level;
- a specific job description;
- a geography or work model.

Engagement Stack makes this normal behavior explicit and auditable.

## Shader Files

Each shader should have:

```text
resume-shaders/<shader-slug>.md
resume-shaders/<shader-slug>.yaml
```

Markdown explains the human strategy. YAML gives agents structured shaping rules.

## Shader Rules

- Do not invent facts.
- Do not edit canonical CV facts.
- Prefer evidence-backed claims.
- Suppress irrelevant material rather than deleting it from source.
- Mark risky or weak claims.
- Store highly targeted shaded resumes in a private overlay when appropriate.

## Example Uses

- `ai-platform-engineer`
- `staff-full-stack`
- `developer-tools-founder`
- `federal-technology-role`
- `fractional-cto`
