# LinkedIn — Media: Banner, Headshot, Custom URL

Actionable setup for the three above-the-fold visual elements. Brand family is
**dark navy `#1f3d5c` with a warm gold accent** — match it across banner and any
generated assets so the profile reads as one system with the GitHub/repo presence.

---

## Custom URL

- **Status: already set** — https://linkedin.com/in/mikebengtson. No action needed.
- Use this exact form (lowercase, no trailing slash) everywhere: résumé site, GitHub
  profile README, email signature, the résumé PDF footer.
- If it ever shows a numeric suffix, fix it under **Edit public profile & URL → Edit your
  custom URL** and reclaim `mikebengtson`.

---

## Banner (background image)

LinkedIn renders the banner at **1584 × 396 px** (4:1). The left ~30% and the bottom-left
are covered by the profile photo and name overlay, so keep those zones clear.

### Ready-to-use banner tagline (pick one)

- **Primary:** `Agentic AI & Developer Productivity — scaling platforms to millions and the toolchains that build them.`
- **Shorter:** `AI engineering leader. Builder + leader at once. Creator of gemba-core.`
- **Punchiest:** `Cut delivery from three months to a two-week sprint — with the agentic toolchain I ship myself.`

### Layout suggestion (navy + gold)

- **Background:** dark navy `#1f3d5c`, ideally a subtle top-left → bottom-right gradient
  (navy deepening toward the right) to match the `engagement-stack` / `job-search-superpower`
  visual family.
- **Safe zone:** put all text in the **right two-thirds**; leave the lower-left ~30% empty
  for the avatar + name overlay.
- **Text:** tagline in white, right-aligned, with **one gold (`#c9a227`-ish warm gold) keyword
  or underline accent** — e.g. gold on "agentic" or a thin gold rule under the line. One gold
  accent only; don't gild the whole thing.
- **Optional right edge:** a faint geometric/line mark in gold at low opacity (the same
  subtle-geometry motif used in the repo banners), kept well clear of the text.
- **Contrast:** keep text large and high-contrast; the banner is small on mobile.

### Existing brand assets to reuse

The repo already ships on-brand navy+gold assets and a generator — reuse the **palette,
gradient, gold accent, and geometric motif**, but note these are branded "Engagement Stack,"
not a personal banner, so adapt rather than upload as-is:

- `resources/branding/banner/engagement-stack-banner.{svg,png}` — README banner (1500×500 SVG / 1280×427 PNG). Source of the exact gradient + gold accent.
- `resources/branding/social/engagement-stack-linkedin-card.{svg}` / `engagement-stack-social.png` — 1200×627 social card.
- `resources/branding/generate.py` — regenerates the family; **adapt this** to emit a 1584×396 personal banner with one of the taglines above (swap "Engagement Stack" wording for Mike's tagline, keep the palette). Documented in `resources/branding/README.md`.

**[gap]** No personal LinkedIn-banner asset (1584×396, Mike-branded) exists yet. Fastest path:
extend `generate.py` to add a `linkedin-profile-banner` size using the established navy/gold
recipe; otherwise compose by hand in Canva/Figma using the palette above.

---

## Headshot (profile photo)

- LinkedIn crops to a **circle**; upload square, **≥ 400 × 400 px** (800–1000 px ideal).
- Recent, well-lit, face filling ~60% of the frame, neutral or softly blurred background.
  A background tinted toward the navy palette ties it to the banner without trying to match exactly.
- Professional but warm — the profile voice is "builder and a leader at once," so approachable, not stiff.
- After upload, set visibility to **Public** so the photo shows to logged-out viewers and in search.

**[gap]** No headshot file is tracked in this repo — supply from Mike's own photos; nothing
to generate here.

---

## Quick checklist

- [ ] Banner 1584×396, navy `#1f3d5c` + one gold accent, text in right two-thirds, tagline chosen
- [ ] Headshot square ≥400px, public visibility on
- [ ] Custom URL confirmed as `linkedin.com/in/mikebengtson` (already set)
- [ ] Banner palette matches the GitHub repo banners (one visual system)
