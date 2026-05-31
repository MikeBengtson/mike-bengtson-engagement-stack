# Evidence

| Evidence | URL / Path | Supports Claim | Notes |
| --- | --- | --- | --- |
| Public repository (source, MIT) | https://github.com/GembaCore/gemba-core | 1, 2, 3, 5 | Go + React single-binary; Mike is creator/maintainer |
| Project / docs site | https://gembacore.github.io/gemba-core/ | 1, 4 | Live GitHub Pages site |
| Repo "About" description | "Agent orchestration dashboard — Kanban UI for any work tracker × any agent runtime." | 1, 2, 4 | Verbatim repository tagline |
| Project Layout (core/ + adapters) | repo `core/`, `internal/adapter/{noop,bd,native,mock}`, `internal/transport/{api,jsonl,mcp}` | 2 | WorkPlane vs OrchestrationPlane separation |
| Backend + embedded SPA | repo `cmd/`, `internal/server/`, `internal/events/`, embedded `web/` | 3 | `make build` → single `./bin/gemba` |
| CI / test / lint / release | `.github/workflows/ci.yml`; `make test` (`go test -race`), `make lint`, `make release` (goreleaser) | 5 | Open engineering hygiene |
| Pinned on GitHub profile | https://github.com/MikeBengtson | 1 | gemba-core is Mike's pinned repo |

## Caveats

- Adoption metrics (stars/forks) are modest (single digits at time of writing). The strength of this evidence is the **artifact and its engineering quality**, not popularity.
- Enterprise outcomes that this class of tooling enabled at Fidelity are NDA-bound and have no public artifact; see `portfolio/projects/aide/`.
