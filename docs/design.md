# Engagement Stack Design

## Category

Engagement Stack is a Career OS: a public-first, human-readable, agent-readable professional source-of-truth system.

It combines:

- canonical career facts;
- portfolio evidence;
- engagement preferences;
- offer/request intake;
- resume shaders;
- platform-specific submission adapters;
- maintenance workflows.

## Design Goals

1. Humans can browse it directly on GitHub.
2. Agents can read, cite, tailor, and transform it.
3. Canonical facts are separated from generated outputs.
4. Evidence-backed claims are easy to inspect.
5. Users can generate traditional resumes at any time.
6. Users can specialize resumes without corrupting the core CV.
7. Engagement requests have a clear intake format.
8. Private overlays are possible without changing the public framework.

## Information Architecture

Markdown is the human source of truth. YAML is the agent/control surface.

Generated artifacts are disposable.

## Resume Shaders

Resume shaders are role/industry/platform-specific shaping rules. They let users produce scoped resumes while preserving a stable canonical CV.

Flow:

```text
cv/ + profile/ + portfolio/ + evidence/
        +
resume-shaders/<target>.yaml
        ↓
generated scoped resume source
        ↓
Markdown / PDF / DOCX / TXT / platform adapter
```

## Job-Search Integration

The separate `job-search` workflow remains an advisory strategy tool. It can export `job-search-report.md` and `job-search-export.yaml`, which Engagement Stack can ingest.

This keeps strategy and durable source of truth separate but interoperable.

## Runtime Posture

No local runtime is required. Agents populate Markdown/YAML through prompts. GitHub Actions can render resumes.

Optional shell scripts support local users who want command-line rendering or validation.
