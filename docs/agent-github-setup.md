# Agent GitHub Setup With `gh`

Use this guide when a user asks an agent to set up Engagement Stack on GitHub.

Do not publish private facts or generated resumes unless the user approves.

## Prerequisites

- GitHub CLI installed: `gh`
- Git configured locally
- User authenticated: `gh auth status`

## Create A Repository

```sh
gh repo create <owner>/<repo> --public --description "Human-first, agent-readable Career OS" --source=. --remote=origin --push
```

For a private repo:

```sh
gh repo create <owner>/<repo> --private --description "Private Engagement Stack" --source=. --remote=origin --push
```

## Set Topics

```sh
gh repo edit <owner>/<repo> --add-topic career-os --add-topic resume --add-topic portfolio --add-topic agent-readable --add-topic engagement-stack
```

## Run Resume Rendering

```sh
gh workflow run render-resumes.yml --repo <owner>/<repo> -f source=cv/resume-source.md
```

Watch the run:

```sh
gh run list --repo <owner>/<repo> --workflow render-resumes.yml
gh run watch --repo <owner>/<repo>
```

Download artifacts:

```sh
gh run download <run-id> --repo <owner>/<repo> --name rendered-resumes --dir generated/resumes
```

## Create A Release With Resume Artifacts

Only do this with explicit user approval.

```sh
gh release create resumes-$(date +%Y-%m-%d) generated/resumes/* --repo <owner>/<repo> --title "Resume artifacts $(date +%Y-%m-%d)" --notes "Generated from Engagement Stack source."
```

## Optional GitHub Pages

The default human surface is GitHub-rendered Markdown. Pages is optional.

If the user wants Pages:

1. Rename `.github/workflows/publish-pages.disabled.yml` after selecting a site generator.
2. Configure repository Pages settings.
3. Keep Markdown/YAML as source of truth.

## Secrets And Variables

Do not store sensitive career data as public variables.

For API keys, use:

```sh
gh secret set USAJOBS_API_KEY --repo <owner>/<repo>
```

For non-sensitive settings:

```sh
gh variable set ENGAGEMENT_STACK_VERSION --body "1.0.0" --repo <owner>/<repo>
```
