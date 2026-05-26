# Engagement Stack: A Career OS For Humans And Agents

The traditional resume is too small for modern professional life.

An engineer's real market signal is distributed across work history, GitHub repositories, live products, architecture notes, shipped artifacts, testimonials, preferences, constraints, and the current shape of the opportunities they actually want. A PDF resume can carry a sliver of that. A LinkedIn profile can carry another sliver. Neither is a maintained source of truth.

Engagement Stack treats a career as a system. Have your agent call mine.

It is a human-first, agent-readable professional dossier: Markdown for people, YAML for agents, evidence-backed project claims, explicit engagement preferences, structured offer requests, evaluation rubrics, resume shaders, and platform-specific submission adapters.

The core idea is simple: keep canonical facts stable, then generate scoped outputs from them.

A user can maintain one canonical CV, then apply a resume shader for an AI platform role, a federal technology role, a fractional CTO engagement, or a developer-tools staff engineer position. The shader changes emphasis, language, ordering, and output targets. It does not rewrite history.

This mirrors how people already behave. They keep a core resume, then specialize it for the opportunity. Engagement Stack makes that behavior explicit, versioned, and agent-assisted.

The repo itself is the website. GitHub renders the README and cross-linked documents. No publishing step is required. If the user wants traditional artifacts, GitHub Actions can render Markdown-native scoped resumes plus PDF, DOCX, and TXT outputs with Pandoc.

Engagement Stack also defines an intake surface. A potential employer or client can submit an engagement request by email with a structured subject line and an optional YAML packet. Humans can read it. Agents can parse it. Missing fields can trigger clarification before evaluation.

That evaluation can be explicit. A job seeker may prefer remote work but accept hybrid for exceptional work, or prefer full-time employment but consider contract work at a premium. Engagement Stack captures those trade-offs as both human-readable priorities and agent-readable scoring rules.

This is not just a job-search toolkit. It is a professional operating system for the agent era.
