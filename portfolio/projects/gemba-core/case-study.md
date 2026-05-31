# Case Study

## Context

Massively parallel, "headless" agentic software development became technically possible faster than it became *manageable*. Developers could spawn many coding agents, but the planning lived in trackers (Jira, Beads, Todo.txt), the execution lived in terminals, and the output lived in git — three timelines that never met in one place. Mike hit this wall directly while operationalizing agentic development at scale and built gemba to close the gap, then open-sourced it under MIT.

## Problem

In agentic projects of any appreciable scale, five obstacles recur (as stated in the repo):

- Planning is disconnected from execution.
- Priority is invisible — the dependency graph says what *can* run; nothing says what *should* run next.
- Expertise is siloed — product, architecture, UX, QA, release, and security judgment are all needed, but the operator can't personally wear every hat.
- State is fragile — git, the tracker, LLM sessions, and sidecar artifacts each move on their own timeline; "undo back to yesterday" doesn't exist.
- Orchestration tooling is tied to one runtime — supporting one tracker or one agent framework means a rewrite when either moves.

## Constraints

- Must be vendor-agnostic: pluggable across both work trackers and agent runtimes.
- Must ship as something a developer can actually run — a single binary, not a stack to assemble.
- Must speak the languages of both planes: tracker concepts (milestones, epics, Kanban) and runtime concepts (sessions, dispatch, pools).
- Must hold production engineering standards in public (tests, lint, CI, releases).

## Approach

- Designed an **adaptor-agnostic core** of shared types (`WorkItem`, `AgentRef`, `Relationship`) separating a **WorkPlane** (e.g. Beads via CLI or direct Dolt SQL) from an **OrchestrationPlane** (e.g. native tmux/iTerm2/Terminal sessions, a Codex driver, a deterministic mock runner).
- Built a Go service: chi router with an OpenAPI spec, an SSE event hub with OpenTelemetry propagation, an auth layer (token/TLS/OIDC interface), and several Cobra CLIs — including `gemba-mcp`, an MCP-tool server variant so agents can query and report through the Model Context Protocol.
- Built a Vite/React SPA for the Kanban "walk the floor" experience and **embedded it into the Go binary**, so the whole product ships as one `./bin/gemba`.
- Added **two-axis dispatch**: per-agent parallelism (capacity) plus opt-in sticky session pools (continuity — long-lived sessions that survive across work items and pick up ready work autonomously).
- Wrapped it in open engineering hygiene: a single `Makefile` dev/build/release loop, `go test -race` + frontend tests, golangci-lint, and goreleaser multi-OS/arch releases, all wired through GitHub Actions CI.

## Outcome

A working, MIT-licensed, single-binary agent-orchestration dashboard published in public, pinned on Mike's GitHub profile, with a live documentation/product site. It is the cleanest public demonstration of the parallel-agentic-development practice Mike sells as an engineering leader — built with the same toolchain (Claude Code, Codex, Beads, MCP) he asks organizations to adopt.

## Evidence

- Repository: https://github.com/GembaCore/gemba-core
- Live docs/product site: https://gembacore.github.io/gemba-core/
- See `evidence.md` and `claims.md` in this folder for the claim-by-claim mapping.

> Honest caveat: adoption is early (single-digit stars at time of writing). The proof here is the artifact and its engineering quality, not popularity. Enterprise outcomes enabled by this class of tooling at Fidelity are NDA-bound — see `portfolio/projects/aide/`.
