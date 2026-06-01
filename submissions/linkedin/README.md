# LinkedIn Adapter

This adapter generates LinkedIn-ready profile text and job-search material.

Engagement Stack does not assume LinkedIn API access. LinkedIn APIs require OAuth and many capabilities require approval. The default workflow is copy/paste with human review.

## Outputs

Every artifact in `submissions/linkedin/`. All are copy/paste-ready and public-safe (no compensation, rates, or private constraints).

| File | What it is |
|------|------------|
| `headline.md` | Headline options (≤220 chars) + keyword-front-loading note. |
| `about.md` | About / summary section (≤2,600 chars) — hook flagged, plus a short variant. |
| `skills.md` | Prioritized skills list (includes Go) with the top 3 to pin flagged. |
| `experience.md` | Per-role Experience sections, reverse-chronological, paste-ready (≤2,000 chars each). |
| `featured.md` | The 5 Featured items to pin, most-impactful first, with descriptions + URLs. |
| `media.md` | Banner + headshot + custom-URL guidance (navy/gold brand). |
| `recommendations.md` | Target recommenders by relationship + 3 request-note templates. |
| `activity-posts.md` | 5 ready-to-post posts, a LinkedIn-native Article, and a weekly cadence plan. |
| `open-to-work.md` | Open-to-Work setup: visibility trade-off, exact titles/locations/types, public blurb, connection-note + InMail templates. |
| `apply-checklist.md` | Ordered, field-by-field checklist to update the live profile. |
| `profile-export.md` | Consolidated copy/paste source (headline, about, experience, featured, skills, projects) derived from the resumes + profile. |
| `profile-export.yaml` | Machine-readable twin of the profile export for agents. |
| `job-search-request.md` | Prompt/note for recruiters, referrers, or agents helping with search. |

> **Recommended apply order:** follow **`apply-checklist.md`** — it walks every field in sequence (custom URL → headline → about → experience → featured → skills → open-to-work → banner/headshot → first posts) and points at the source file for each step.
