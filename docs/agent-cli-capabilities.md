# Agent CLI Capabilities

This framework supports compliant automation where official tools or stable local tools exist.

## Supported By Default

| Surface | Tool | Use |
| --- | --- | --- |
| GitHub | `gh` | create repos, run workflows, manage releases, set secrets |
| Resume rendering | Pandoc / Docker / GitHub Actions | generate PDF, DOCX, TXT |
| Local validation | shell + Ruby in CI | required-file check and YAML parse |

## Supported With User Credentials

| Surface | Tool | Use |
| --- | --- | --- |
| USAJOBS | official REST API via `curl` | search public federal job announcements |

USAJOBS requires an API key for search. Store it as a secret, not in source.

## Generate-Only By Default

| Surface | Reason |
| --- | --- |
| LinkedIn | APIs are OAuth/approval-gated and many capabilities are restricted |
| Indeed | public docs are mostly partner/employer/ATS oriented |
| Workday/Greenhouse/Lever/Ashby/SmartRecruiters/iCIMS | candidate submission surfaces vary by employer |

For these, Engagement Stack generates copy/paste-ready material and attachment artifacts.

## Automation Rule

If a platform does not provide a compliant user-facing API or CLI, generate human-reviewed material instead of automating platform actions.
