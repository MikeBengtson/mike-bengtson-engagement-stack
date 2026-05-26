<a name="top"></a>

[![Engagement Stack](resources/branding/banner/engagement-stack-banner.png)](https://github.com/MikeBengtson/engagement-stack)

# Engagement Stack

<p>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-22c55e" alt="License: MIT" /></a>&nbsp;
  <a href="AGENTS.md"><img src="https://img.shields.io/badge/agents-readable-06b6d4" alt="Agent readable" /></a>&nbsp;
  <a href="resume-shaders/README.md"><img src="https://img.shields.io/badge/resume-shaders-f43f5e" alt="Resume shaders" /></a>&nbsp;
  <a href="cv/README.md"><img src="https://img.shields.io/badge/source-Markdown%20%2B%20YAML-8b5cf6" alt="Markdown and YAML" /></a>&nbsp;
  <a href=".github/workflows/render-resumes.yml"><img src="https://img.shields.io/badge/render-Pandoc-111827" alt="Pandoc rendering" /></a>&nbsp;
  <a href="setup/START_HERE.md"><img src="https://img.shields.io/badge/setup-no%20runtime%20required-f59e0b" alt="No runtime required" /></a>
</p>

⭐ **Use this as a template** — fork it, delete the examples, then let an agent help you populate a complete Career OS.

<p>
  <a href="https://x.com/intent/tweet?text=Engagement%20Stack%20is%20a%20human-first%2C%20agent-readable%20Career%20OS%20for%20CVs%2C%20portfolio%20evidence%2C%20engagement%20requests%2C%20and%20resume%20shaders:%20https%3A//github.com/MikeBengtson/engagement-stack"><img src="https://img.shields.io/badge/share-000000?logo=x&logoColor=white" alt="Share on X" /></a>&nbsp;
  <a href="https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fgithub.com%2FMikeBengtson%2Fengagement-stack"><img src="https://img.shields.io/badge/share-0A66C2?logo=linkedin&logoColor=white" alt="Share on LinkedIn" /></a>&nbsp;
  <a href="https://www.reddit.com/submit?url=https%3A%2F%2Fgithub.com%2FMikeBengtson%2Fengagement-stack&title=Engagement%20Stack:%20a%20Career%20OS%20for%20humans%20and%20agents"><img src="https://img.shields.io/badge/share-FF4500?logo=reddit&logoColor=white" alt="Share on Reddit" /></a>&nbsp;
  <a href="https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fgithub.com%2FMikeBengtson%2Fengagement-stack&t=Engagement%20Stack:%20a%20Career%20OS%20for%20humans%20and%20agents"><img src="https://img.shields.io/badge/share-FF6600?logo=ycombinator&logoColor=white" alt="Share on Hacker News" /></a>
</p>

Engagement Stack is a human-first, agent-readable Career OS: a source-controlled professional dossier for CV, work history, portfolio evidence, engagement preferences, structured offer requests, and job-search submission materials.

It is not just a resume template. It is a framework for maintaining a complete professional record that humans can browse directly on GitHub and agents can read, cite, tailor, and transform without inventing facts.

## Table Of Contents

- [🚀 Start Here](#-start-here)
- [🎯 What This Repo Is For](#-what-this-repo-is-for)
- [🧠 Core Rule](#-core-rule)
- [🙏 Inspiration](#-inspiration)
- [📦 Repository Layout](#-repository-layout)
- [🧪 Examples](#-examples)
- [📄 Resume And Submission Outputs](#-resume-and-submission-outputs)
- [🎛️ Resume Shaders](#%EF%B8%8F-resume-shaders)
- [🖼️ Brand Assets](#%EF%B8%8F-brand-assets)
- [🔗 Built With Engagement Stack](#-built-with-engagement-stack)

## 🚀 Start Here

- [Set Up Your Stack](setup/START_HERE.md)
- [Agent Instructions](AGENTS.md)
- [Profile](profile/README.md)
- [CV And Work History](cv/README.md)
- [Portfolio](portfolio/README.md)
- [Evidence](evidence/README.md)
- [Engagement Preferences](engagements/README.md)
- [Submission Adapters](submissions/README.md)
- [Maintenance System](maintenance/README.md)

## 🎯 What This Repo Is For

Engagement Stack answers five practical questions:

- **Who is this person?** See `profile/`.
- **What have they done?** See `cv/` and `portfolio/`.
- **What proves it?** See `evidence/` and each project claim map.
- **What engagement do they want now?** See `engagements/`.
- **What can be generated for a channel?** See `submissions/` and `generated/`.
- **How should a resume be specialized?** See `resume-shaders/`.

The root README and folder READMEs are the default human-readable website. No publishing step is required.

## 🧠 Core Rule

Markdown is the human source of truth. YAML is the agent and automation surface.

Every important human document can have a YAML sidecar. The Markdown explains the person and their work. The YAML gives agents structured fields for routing, matching, scoring, validation, and export.

## 🙏 Inspiration

Engagement Stack is inspired in part by [Every Inc.'s `after-automation-agent-mode`](https://github.com/EveryInc/after-automation-agent-mode), especially the idea that a repository can become a durable working surface for agents: local instructions, source material, prompts, review criteria, and outputs arranged so humans and agents can collaborate from the same project context.

This project applies that pattern to a different domain: a professional Career OS for CV, portfolio evidence, engagement preferences, offer handling, and job-search submission materials.

## 📦 Repository Layout

```text
.
├── README.md
├── AGENTS.md
├── setup/                  # onboarding and completeness checks
├── framework/              # framework origin, version, adoption, link-back
├── profile/                # identity, positioning, operating style
├── cv/                     # canonical CV, work history, skills, resume source
├── portfolio/              # projects, claims, case studies, proof
├── evidence/               # proof index: repos, products, artifacts, references
├── career-strategy/        # target roles, markets, positioning, search strategy
├── engagements/            # desired engagements and request instructions
├── resume-shaders/         # role/industry-specific resume shaping rules
├── submissions/            # LinkedIn, ATS, USAJOBS, Indeed, email adapters
├── prompts/                # paste-ready agent prompts
├── integrations/           # optional upstream/downstream repo contracts
├── maintenance/            # refresh cadence and audit checklists
├── templates/              # blank files to copy into a user fork
├── examples/               # disposable fictional example content
├── scripts/                # optional local convenience scripts
└── generated/              # generated artifacts; safe to rebuild
```

[⬆ back to top](#top)

## 🧪 Examples

The `examples/fictional-engineer/` folder is a disposable fixture. It exists to show a complete shape. Delete it when adopting this framework, or keep it as reference. Anything with `.example.md` or `.example.yaml` is sample content, not a user fact.

## 📄 Resume And Submission Outputs

Engagement Stack is designed to generate:

- one-page resume PDF
- two-page resume PDF
- ATS-friendly DOCX
- ATS-friendly TXT
- full CV PDF
- USAJOBS/federal-style resume PDF
- Markdown-native scoped resume source
- LinkedIn profile text
- generic ATS field packs
- engagement request replies

Pandoc is the default renderer. Users do not need to install Pandoc locally: GitHub Actions can render artifacts on demand.

## 🎛️ Resume Shaders

Most people keep a core resume and tailor it for a role, industry, or client. Engagement Stack makes that explicit.

A **resume shader** is a small Markdown/YAML pair that tells an agent how to shape the canonical CV before emitting a scoped resume. It can prioritize certain projects, suppress irrelevant details, adjust language for a target industry, and choose output formats without changing the canonical CV.

Public-safe shaders can live in `resume-shaders/`. Sensitive or highly targeted shaded resumes can live in a private overlay or in `generated/`.

## 🖼️ Brand Assets

This README banner and the social preview image live in [resources/branding/](resources/branding/).

- README banner: [resources/branding/banner/engagement-stack-banner.png](resources/branding/banner/engagement-stack-banner.png)
- Social preview: [resources/branding/social/engagement-stack-social.png](resources/branding/social/engagement-stack-social.png)

Use the social preview in GitHub repository settings or on LinkedIn/X posts introducing the framework.

## 🔗 Built With Engagement Stack

This repository is the framework source. A user fork should keep a link-back so agents and humans can understand the structure and find updates.

Framework docs: [framework/origin.md](framework/origin.md)

[⬆ back to top](#top)
