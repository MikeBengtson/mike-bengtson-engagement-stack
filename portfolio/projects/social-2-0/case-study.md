# Case Study

> Commercial product, proprietary. Described from the resume of record; no public artifact remains to link.

## Context

Amobee's Social Channels team integrated paid-advertising APIs from multiple social platforms — Facebook, Twitter, Snapchat, Pinterest — each with its own auth model, data shapes, and quirks. Treating each as a one-off integration did not scale.

## Problem

Unify four disparate third-party advertising APIs, plus internal data and state, behind a single coherent platform — with the hard cross-cutting concerns (identity, grouping, orchestration) solved once rather than per channel.

## Constraints

- Four very different third-party APIs, each evolving independently.
- Multi-identity authentication across providers.
- Production commercial platform with real advertisers.
- A legacy local-dev/deploy toolchain (Vagrant/Bash/Fabric) slowing the team.

## Approach

- **Designed Social 2.0** as a unified Java microservices platform consolidating the Facebook, Twitter, Snapchat, and Pinterest ad APIs with internal data and state.
- **Personally built the cross-cutting services**: multi-identity OAuth, ad-hoc entity-grouping, and front-end orchestration.
- **Led the founding Snapchat-channel "tiger team"** building Java/Spring Boot/PostgreSQL microservices.
- **Modernized DevOps**, replacing Vagrant/Bash/Fabric with a Kubernetes solution that cut configuration overhead and deployment errors; later set the long-term maintenance strategy for the Facebook offering and remotely led an 8-person offshore dev/test team.

## Outcome

A unified, production microservices platform that turned four bespoke social-ad integrations into one coherent surface — with the auth, grouping, and orchestration plumbing built to be reused — and a Kubernetes-based DevOps toolchain that reduced configuration overhead and deployment errors.

## Evidence

- Resume of record: `resumes/long.md`, `resumes/short.md`
- See `evidence.md` and `claims.md` in this folder.

> No public repo or live URL remains (proprietary; Amobee assets acquired/wound down). For hands-on public proof of Mike's engineering, see `portfolio/projects/gemba-core/`.
