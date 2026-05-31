# gemba-core

## Summary

**gemba** is an open-source agent-orchestration dashboard — a Kanban UI for *any work tracker × any agent runtime*. It is a single-binary Go + React application (MIT-licensed) that gives developers one pane of glass for planning, dispatching, and monitoring massively parallel "headless" agentic software development.

The problem it solves: in large-scale agentic development, planning is disconnected from execution. Issues live in one place (Jira, Beads, Todo.txt), agents run in a terminal, and output lands in git — with no single surface tying milestones, epics, and Kanban planning to the actual ordering, dispatching, and monitoring of work. gemba unifies those planes: it pairs a **WorkPlane** (work trackers such as Beads) with an **OrchestrationPlane** (agent runtimes such as native tmux/iTerm2/Terminal sessions or a Codex driver) behind an adaptor-agnostic core, so swapping either side does not require a rewrite.

This is Mike's strongest piece of public, hands-on evidence: a real, buildable, tested codebase that he created and maintains, demonstrating the agentic-development practice he operationalizes inside engineering organizations.

## Role

**Creator and maintainer.** Mike designed the architecture (adaptor-agnostic core, WorkPlane/OrchestrationPlane split, SSE event hub, MCP-tool server variant), built the project, and maintains it in public. Evidence level: **built** (and **maintained**).

## What This Demonstrates

- Designing and shipping a real agentic-development tool end to end — not a slide, a working single-binary product.
- Vendor-agnostic architecture: pluggable adapters so one tracker/runtime can be swapped for another without a rewrite.
- Full-stack range: Go backend (chi router, OpenAPI, SSE/OTEL eventing, Cobra CLIs) plus an embedded Vite/React SPA, shipped as one binary.
- Engineering hygiene in the open: CI workflow, `go test -race` + frontend tests, golangci-lint, goreleaser multi-OS/arch releases, a published docs site.
- Direct, public proof of the parallel-agentic-development thesis Mike sells as a leader — the same toolchain (Claude Code, Codex, Beads, MCP) he asks organizations to adopt.

## Links

- Repository: https://github.com/GembaCore/gemba-core
- Live product: https://gembacore.github.io/gemba-core/ (project + documentation site)
- Documentation: https://gembacore.github.io/gemba-core/
