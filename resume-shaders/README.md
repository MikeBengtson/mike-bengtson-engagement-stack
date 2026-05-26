# Resume Shaders

A resume shader is guidance for generating a scoped resume from canonical career materials.

The canonical CV answers: **what is true?**

A resume shader answers: **how should those truths be emphasized for this target?**

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
