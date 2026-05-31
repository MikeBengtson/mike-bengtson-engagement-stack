# Portfolio

This folder contains project case studies and evidence-backed claims.

Each project has:

```text
portfolio/projects/<project-slug>/
├── README.md       # human-readable narrative
├── project.yaml    # parseable control surface
├── claims.md       # what the project proves, with caveats
├── evidence.md     # proof table (links / paths)
└── case-study.md   # context → problem → approach → outcome
```

## Evidence Posture

Mike's career spans two decades of production platforms, but most of that work is **internal employer software** (Fidelity, Amobee) that is proprietary or under NDA — there is no public repo or live URL to link. Those projects are documented honestly here and rest on Mike's role plus the resume of record (`resumes/long.md`, `resumes/short.md`).

The **strongest public, hands-on evidence is `gemba-core`** — an open-source, MIT-licensed agent-orchestration framework Mike created and maintains, with a real buildable codebase, CI, tests, and a live docs site. Where internal work is described (especially the agentic-development practice behind AIDE), `gemba-core` is the public, inspectable companion that demonstrates the same capability.

See `evidence/` for the consolidated proof index (`github.md`, `live-products.md`, `evidence-index.yaml`).

## Featured Projects

| Project | Role | Evidence level | Public artifact |
| --- | --- | --- | --- |
| [gemba-core](projects/gemba-core/) | Creator / maintainer | built | **Yes** — [public repo](https://github.com/GembaCore/gemba-core) + [docs site](https://gembacore.github.io/gemba-core/) |
| [AIDE (Fidelity Brokerage)](projects/aide/) | Led engineering | led | No — internal / NDA |
| [Consumer Portfolio Capability (Fidelity)](projects/consumer-portfolio-capability/) | Led / Chapter Leader | led | No — internal / NDA |
| [Amobee Marketplace](projects/amobee-marketplace/) | Architect / lead | led | No — proprietary, not public today |
| [Social 2.0](projects/social-2-0/) | Designer / lead | built | No — proprietary, not public today |
