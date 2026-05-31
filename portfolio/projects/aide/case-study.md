# Case Study

> Internal / NDA. Described at the level of publicly stated program scope only; no confidential architecture, data, or figures beyond the resume of record.

## Context

Fidelity Brokerage's call-center associates (~8,900 of them) worked across 14+ separate servicing tools backed by dozens of systems. Average handle time (AHT) — the time to resolve a customer interaction — was a major cost and experience lever. The brokerage launched AIDE, an AI "single pane of glass," to consolidate that surface and target **$175M in AHT savings over five years**, alongside a Brokerage AI Innovation workstream to operationalize agentic development.

## Problem

Two intertwined problems: (1) deliver a consolidated servicing platform that meaningfully reduces AHT across thousands of associates, and (2) deliver it fast enough — and with enough engineering capacity — to hit an aggressive, nine-figure business case.

## Constraints

- Highly regulated brokerage environment; correctness, auditability, and release governance are non-negotiable.
- Aggressive timeline against a five-year, $175M savings target.
- A delivery org that needed to roughly double under deadline.
- Integration with dozens of existing back-end systems and 14+ legacy servicing tools.

## Approach

- **Led engineering** for AIDE as VP / Multi-Squad Chapter Leader, owning delivery across squads and the cross-squad SDLC governance (integration testing, release management, AI-assisted review).
- **Scaled the org 14 → 31 engineers in six months** via internal, external, associate, and contingent recruiting, onboarding, and training.
- **Operationalized agentic development** to compress cycle time: a reusable, skill-based code-generation pipeline cut some feature classes from ~3 months to a single two-week sprint (up to ~6×). This approach is externalized publicly as `gemba-core`.
- **Stood up an enterprise RAG + MCP knowledge layer**, vectorizing thousands of Confluence pages and Swagger/API contracts so institutional knowledge was directly consumable by agentic pipelines.
- **Set the brokerage's agentic-development standard** — Claude Code, Codex, SpecKit, GitNexus code graphs, local MCP servers (incl. a Playwright driver) — and introduced Beads as a parallel-workstream data plane for mainframe modernization.

## Outcome

Shipped AIDE's highest-impact servicing capabilities — Wire/ACH transfer, stock and funds trading, multi-holding trading and liquidation, and call-notes optimization — directly advancing the program's $175M AHT-savings target, while standing up the agentic-development practice that compressed delivery cycles across the org.

## Evidence

- Resume of record: `resumes/long.md`, `resumes/short.md`
- Public companion (demonstrable): https://github.com/GembaCore/gemba-core
- See `evidence.md` and `claims.md` in this folder.

> No public repo or URL exists for AIDE itself (internal / NDA). For hands-on, inspectable proof of the underlying agentic-development capability, see `portfolio/projects/gemba-core/`.
