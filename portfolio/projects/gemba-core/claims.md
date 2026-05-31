# Claims

## Claim 1: Can design and ship agentic-development tooling end to end

Explanation: gemba is a working, single-binary agent-orchestration dashboard that Mike designed and built — a Kanban UI for planning, dispatching, and monitoring parallel agentic work. It is not a prototype or a deck; it builds, tests, and releases.

- Role: creator / maintainer (built)
- Best evidence: public repo with source, Makefile dev/build/release loop, CI workflow, and a published docs/product site
- Caveat: none on the artifact itself; this is the cleanest public proof in the portfolio
- Where to look: https://github.com/GembaCore/gemba-core · `README.md` · https://gembacore.github.io/gemba-core/

## Claim 2: Designs vendor-agnostic, adaptor-based architectures

Explanation: gemba separates a **WorkPlane** (work trackers, e.g. Beads via CLI or direct Dolt SQL) from an **OrchestrationPlane** (agent runtimes, e.g. native tmux/iTerm2/Terminal sessions, a Codex driver) behind an adaptor-agnostic `core` of shared types. Either side can be swapped without rewriting the other — "any work tracker × any agent runtime."

- Role: architect (built)
- Best evidence: the `core/`, `internal/adapter/` (noop, bd/Beads, native, mock), and `internal/transport/` (api / jsonl / mcp) layout in the repo
- Caveat: adapter set reflects the runtimes Mike targets; not every tracker/runtime is implemented
- Where to look: repo "Project Layout" section · `core/` and `internal/adapter/`

## Claim 3: Full-stack delivery — Go backend plus embedded React/Vite SPA

Explanation: gemba is a Go service (chi router, OpenAPI spec, SSE event hub with OpenTelemetry propagation, several Cobra CLIs and an MCP-tool server) with a Vite/React single-page app embedded into the binary. One artifact ships both planes.

- Role: full-stack engineer (built)
- Best evidence: `cmd/`, `internal/server/`, `internal/events/` and the embedded `web/` SPA; `make build` produces a single `./bin/gemba`
- Caveat: none material
- Where to look: repo "Development" and "Project Layout" sections

## Claim 4: Operationalizes massively parallel agentic software development

Explanation: gemba was built to make "headless," massively parallel agentic development manageable — milestones, epics, Kanban planning, two-axis dispatch (per-agent parallelism plus sticky session pools), and live progress/drift monitoring in a single pane of glass. This is the same practice Mike stood up at Fidelity, externalized as open source.

- Role: creator (built) — and the practitioner who applies it in industry
- Best evidence: repo "About" and "Two-Axis Work Planning and Dispatch" sections; integration with Beads and Claude Code / Codex
- Caveat: the open-source repo proves the tool and the thinking; the enterprise-scale outcomes it supported are described under the AIDE project and are NDA-bound (no public artifact)
- Where to look: https://github.com/GembaCore/gemba-core · cross-reference `portfolio/projects/aide/`

## Claim 5: Practices open-source engineering hygiene

Explanation: the project ships CI (GitHub Actions), `go test -race ./...` plus frontend tests, golangci-lint, and goreleaser multi-OS/arch release tarballs — the discipline expected of production code, done in public.

- Role: maintainer (built / maintained)
- Best evidence: CI badge/workflow, `make test` / `make lint` / `make release` targets in the repo
- Caveat: small contributor base; primarily a Mike-authored project
- Where to look: repo "Development" section · `.github/workflows/ci.yml`
