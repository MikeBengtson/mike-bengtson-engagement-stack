# LinkedIn Activity — Posts & Article

Copy/paste-ready LinkedIn activity for Mike Bengtson. Public only — no compensation, rates, or private constraints. Facts grounded in `profile-export.md`, `experience.md`, and `engagements/current-preferences.md`. AIDE specifics are under NDA; only scope/impact level appears here.

> Posting note: LinkedIn shows the first ~140 chars before "…see more," so the hook line is load-bearing. Keep hashtags to 3–5. Drop links in the first comment when reach matters (LinkedIn down-ranks outbound links in the post body).

---

## Post 1 — Availability announcement (open to fractional + full-time)

**Hook:** After ~four years leading Brokerage's agentic-AI transformation at Fidelity, I'm opening up my next chapter.

**Body:**

After ~four years leading Fidelity Brokerage's agentic-AI transformation, I'm planning my next chapter — and I'm available starting July 2026.

What I do: operationalize agentic / AI-assisted development across an organization. Standards, tooling (Claude Code, Codex, MCP, SpecKit, code-graph intelligence), RAG/MCP knowledge layers, evals, and guardrails — then the org-building to make it stick. I lead multi-squad organizations and still write code with the same toolchains I ask my teams to adopt.

I'm prioritizing **fractional and advisory** engagements with leaders standing up a genuine agentic pipeline — and I'll consider the right **full-time** VP/Director mandate. Atlanta + Remote.

If you're operationalizing agentic development, scaling an AI-engineering org, or modernizing a platform under deadline, I'd love to compare notes.

**Soft CTA:** What's the biggest blocker you're hitting in moving agentic development from pilot to production? Curious what others are seeing.

**Hashtags:** #AgenticAI #EngineeringLeadership #FractionalLeadership #DeveloperProductivity #AIEngineering

---

## Post 2 — Agentic-development insight

**Hook:** The hard part of agentic development isn't the model. It's the surface you give it to act on.

**Body:**

The hard part of agentic development isn't the model. It's the surface you give it to act on.

A coding agent is only as good as the context it can reach. Drop one into a large codebase with no map and it confidently does the wrong thing. Give it a code graph, vectorized API contracts, institutional docs it can actually retrieve, and a clear spec — and the same model starts behaving like a senior engineer who's been on the team for a year.

The pattern that's worked for me:
- **Spec-driven, not vibe-driven.** Frame the task precisely up front; let the agent compress the hours in the middle; review hard at the back.
- **Make knowledge retrievable.** RAG + MCP over your docs and contracts beats a longer prompt every time.
- **Give it a map.** Code-graph intelligence so the agent understands blast radius before it edits.
- **Evals and guardrails, always.** The further an agent runs from human oversight, the worse it gets.

Done right, this isn't incremental. I've watched it pull delivery for some feature classes from ~3 months down to a single two-week sprint.

**Soft CTA:** If you're building this muscle on your team, happy to swap notes on what's working — and what isn't.

**Hashtags:** #AgenticAI #AIEngineering #DeveloperProductivity #RAG #MCP

---

## Post 3 — gemba-core / open source

**Hook:** I open-sourced the framework I use to run dozens of coding agents in parallel without losing the thread: gemba-core.

**Body:**

I open-sourced gemba-core — the framework I built to keep massively parallel agentic coding flows from turning into chaos.

When you run many coding sessions at once, the bottleneck stops being the model and becomes orchestration: what's each agent working on, what's done, what's blocked, and how do you keep work-tracking honest across all of it? gemba-core is a vendor-agnostic answer to that — work-tracking and session orchestration for parallel agentic development, shipped as a single Go binary with an embedded React/Vite SPA.

It's deliberately not tied to any one model or vendor. The bet behind it: the durable layer in agentic development is the orchestration and the record of work — not whichever model is winning this quarter.

It's free and open source. Issues, ideas, and PRs welcome.

**Soft CTA:** Building anything in the parallel-agents space? I'd love to hear how you're handling work-tracking and orchestration — link to the repo in the comments.

**Hashtags:** #OpenSource #AgenticAI #Golang #React #DeveloperTools

> First comment: gemba-core → https://github.com/GembaCore/gemba-core

---

## Post 4 — "What good looks like": operationalizing AI across an org

**Hook:** Most "AI transformations" stall at the demo. Here's what it actually takes to operationalize agentic development across an org.

**Body:**

Most "AI transformations" stall at the impressive demo. Operationalizing agentic development across an organization is a different — and harder — problem. What good looks like:

1. **A standard, not a free-for-all.** One agreed toolchain (for us: Claude Code, Codex, SpecKit, code graphs, local MCP servers) so teams compound on each other's work instead of each reinventing it.
2. **A knowledge layer agents can read.** Vectorize your docs and API contracts so institutional knowledge is retrievable, not trapped in someone's head or a stale wiki.
3. **Governance that fits the SDLC.** Test generation, SDK migrations, static-analysis remediation, and a real data plane for tracking agent work — not a side process bolted on.
4. **Leaders who still touch the code.** You can't set a credible agentic standard from a slide. The people defining it should be using it.
5. **Evals and guardrails from day one.** Velocity without quality gates is just faster regressions.

Get these right and the cycle-time gains are dramatic. Skip them and you get a flashy pilot that never reaches production.

**Soft CTA:** Which of these is the hardest in your org? In my experience it's #1 — getting an organization to actually converge on one standard.

**Hashtags:** #AIEngineering #AgenticAI #EngineeringLeadership #DigitalTransformation #DeveloperProductivity

---

## Post 5 — Lesson from leading the AIDE program (public-safe; NDA scope/impact only)

**Hook:** I spent two years leading an AI program with a nine-figure efficiency target. The biggest lesson had nothing to do with AI.

**Body:**

I spent two years leading an AI servicing program built around a nine-figure average-handle-time savings target — consolidating a sprawl of servicing tools into a single pane of glass for thousands of call-center associates.

The biggest lesson had nothing to do with the models.

It was this: **a nine-figure target is a forcing function for focus, not a license to boil the ocean.** When the number is that big, every team wants to add "their" feature to the platform. The job of leadership is the opposite — relentlessly sequencing the few capabilities that actually move handle time, and saying "not yet" to the rest.

A few things that held up under that pressure:
- Grow the team fast *and* keep delivery coherent — we roughly doubled the engineering org in six months without losing the plot.
- Ship the highest-impact workflows first; resist the gravity of the long tail.
- Treat the efficiency number as a north star for prioritization, not a promise you scatter across fifty half-built features.

(Program specifics are under NDA — this is the leadership shape, not the internals.)

**Soft CTA:** If you've led a program against a big top-line number, how did you keep scope honest? Always looking to learn how others held the line.

**Hashtags:** #EngineeringLeadership #AIEngineering #ProgramManagement #Leadership #AgenticAI

---

## LinkedIn Article

> Adapted from `engagement-stack/docs/feature-article-v2.md` into a LinkedIn-native long-form article. Paste into LinkedIn's article editor (Write article). Title ≤150 chars works best for the headline field. Attribution to Dan Shipper (Every) and Kieran Klassen is preserved exactly.

**Title:** Have Your Agent Call Mine: Why Your Career Needs an Agent Surface

**Dek (subtitle / first line):** AI doesn't shrink the amount of human work — it moves it. Here's what that means for the most under-built surface in your professional life: your own career.

**Body:**

The traditional resume is too small for modern professional life.

An engineer's real market signal is scattered across work history, GitHub repositories, live products, architecture notes, shipped artifacts, testimonials, references, stated preferences, hard constraints, and the actual shape of the opportunities they want next. A PDF carries a sliver of that. A LinkedIn profile carries a different sliver. Neither is a maintained source of truth — and, more to the point in 2026, neither can be read by an agent.

That last part is the problem worth solving.

### The agent surface

Dan Shipper, who runs Every, has spent the last two years arguing that AI doesn't shrink the amount of human work — it moves it. In *The Knowledge Economy Is Over. Welcome to the Allocation Economy*, he makes the case that once models commoditize yesterday's competence, the scarce skill becomes allocation: deciding what to point an agent at, and judging what it brings back. His colleague Kieran Klassen calls the shape of the new workflow the **human sandwich** — a person frames the task at the front, an agent compresses hours into minutes in the middle, and a person evaluates the result at the back. Shipper's blunter version: every agent needs a human, and the further an agent runs from human oversight, the worse it gets.

Buried in that work is a corollary that matters for everyone, not just software companies. If agents are going to do real work on your behalf, the things they act on have to be legible to them. Shipper's point about software in the agent era is that a product now has to be usable by humans and agents at the same time — same product, same data, two kinds of reader. Call that an **agent surface**: a structured face on something a person can read and an agent can act on, with neither one a second-class citizen.

Most of the digital world doesn't have one yet. Your career certainly doesn't.

### Build it human-first, with the agent in the sidecar

So I built one for my own professional life — an agent surface I call an Engagement Stack. It's a human-first, agent-readable career dossier: Markdown for people, YAML for agents, evidence-backed project claims, explicit engagement preferences, structured offer requests, evaluation rubrics, resume shaders, and platform-specific submission adapters — all in one versioned repository.

*Human-first* is the load-bearing word. The Markdown is the source of truth a person writes and reads; the YAML rides alongside it as the machine-readable twin, generated from the same canonical facts. This is the opposite of an autopilot that files your applications while you sleep. It's a sidecar: you drive, your agent rides beside you reading the same dashboard, and you keep both hands on the wheel. The human sandwich isn't a limitation to design around here — it's the operating principle.

Shipper himself has grown skeptical that every employee inside a company needs a personal agent; he now expects organizations to converge on one shared "super agent." Fair — for an employee. But your career isn't an employee inside one company. It's a single identity transacting across dozens of opportunities, employers, and clients over decades. That's exactly the case where a personal, portable, agent-readable surface earns its keep.

### Canonical facts in, scoped outputs out

The core mechanic is simple: keep canonical facts stable, then generate scoped outputs from them.

You maintain one canonical CV. Then you apply a resume shader for an AI-platform role, a federal technology role, a fractional-CTO engagement, or a developer-tools staff position. The shader changes emphasis, language, ordering, and output target. It does not rewrite history.

This is the allocation economy in miniature. You supply the situated taste — which role, which framing, which opportunity is worth your time — and the agent renders against it. You allocate; it produces.

### What happens when it feeds your job search

A dossier that only sits there is just a nicer resume. The whole point of an agent surface is that *other* agents can drink from it. A companion strategy prompt reads the stack and returns positioning, target roles, an honest hop-length on each pivot, and recommended shaders for the openings actually worth pursuing. Then the loop closes: it hands back an advisory packet your stack can ingest *after you've reviewed it*. Strategy on top, source of truth underneath, a human approving the handoff in between. The human sandwich again, this time spanning two tools instead of one.

That division of labor is deliberate. The strategy layer stays volatile and opinionated. The Engagement Stack stays the durable, slow-moving record. Neither tries to be the other, and the human signs off before anything the agent recommends becomes a fact.

### Have your agent call mine

The surface points outward as well as in. It defines an intake surface: a potential employer or client can submit an engagement request with a structured subject line and an optional YAML packet. A human can read it. An agent can parse it. Missing fields trigger clarification before evaluation — and the evaluation itself is explicit. Prefer remote but accept hybrid for exceptional work; prefer fractional but consider full-time for the right mandate. Those trade-offs live as both human-readable priorities and agent-readable scoring rules.

*Have your agent call mine.* That stops being a joke the moment both sides have a real surface to call.

None of this requires putting your whole life in public. The public repo can state that private thresholds exist while ignored local overlays hold the actual salary floors, negotiation strategy, and sensitive constraints. The browseable face stays curated; the decision model stays complete for the one agent that works for you.

This is not just a job-search toolkit. It's a professional operating system for the agent era — the human-first kind, where the agent rides in the sidecar and you keep the wheel.

---

*The allocation economy, the agent surface, and the "human sandwich" are drawn from Dan Shipper and his colleagues at Every — see [The Knowledge Economy Is Over. Welcome to the Allocation Economy](https://every.to/chain-of-thought/the-knowledge-economy-is-over-welcome-to-the-allocation-economy) and [After Automation](https://every.to/p/after-automation). The "human sandwich" framing is Kieran Klassen's.*

**Suggested article hashtags:** #AgenticAI #FutureOfWork #AIEngineering #CareerStrategy #AllocationEconomy

---

## Weekly Cadence Plan

A light, sustainable rhythm — designed to build presence ahead of July 2026 availability without becoming a second job.

**Per week:**
- **1–2 posts/week.** One "insight/value" post (Posts 2, 3, or 4 style) earlier in the week; optionally one lighter post or repost-with-commentary later.
- **Comment on 3–5 posts/week** from people in agentic AI / engineering-leadership circles. Thoughtful comments often out-reach your own posts for visibility.
- **Reply to every comment** on your own posts within the first few hours — early engagement drives distribution.

**Monthly:**
- **1 long-form Article** (start with the one above), or a heavier "what good looks like" post if an Article is too much that month.
- Refresh the **Featured** section if a post performs well — pin the winners.

**Sequencing suggestion (first 4 weeks):**
1. Week 1: Post 2 (agentic insight) — lead with value, not availability.
2. Week 2: Post 3 (gemba-core / OSS) — concrete proof you build.
3. Week 3: Post 4 ("what good looks like") + publish the Article.
4. Week 4: Post 1 (availability) — by now there's a body of work behind the ask. Hold Post 5 (AIDE lesson) for any week you want a leadership-credibility beat.

> Tip: as July 2026 nears, shift the mix toward availability and let the value posts carry the credibility. Pair this cadence with the `open-to-work.md` setup (discretion now → public closer to availability).
