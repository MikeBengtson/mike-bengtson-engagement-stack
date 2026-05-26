# Generate Engagement Evaluation Rubric

I want to define how this Engagement Stack evaluates offers, opportunities, contracts, and engagement requests.

Read:

- `README.md`
- `AGENTS.md`
- `profile/positioning.md`
- `career-strategy/current-search.md`
- `engagements/current-preferences.md`
- `engagements/current-preferences.yaml`
- `engagements/engagement-models.md`
- `engagements/engagement-models.yaml`
- `engagements/evaluation-rubric.md`
- `engagements/evaluation-rubric.yaml`
- `engagements/offer-packet.schema.yaml`
- `integrations/job-search/README.md`

If a `job-search-export.yaml` is available, use it as advisory input for target roles, target industries, geography, employment-type recommendations, compensation posture, and resume shader recommendations. Do not treat it as canonical fact.

## Goal

Create or update:

- `engagements/evaluation-rubric.md`
- `engagements/evaluation-rubric.yaml`
- `engagements/offer-packet.schema.yaml` if required fields need to change

The Markdown should help humans understand the person's priorities. The YAML should let agents score offers, identify dealbreakers, validate missing offer-packet fields, and draft clarification requests.

## Interview Method

Ask in small batches. For each category, ask:

1. What is preferred?
2. What is acceptable?
3. What is a dealbreaker?
4. What would make you bend on that preference?
5. Which details are private and should live outside the public repo?

## Priority Categories

Cover these categories:

- engagement model;
- compensation and economics;
- location and physical presence;
- travel and schedule load;
- work authorization and compliance;
- role and scope fit;
- technical, domain, and craft fit;
- mission, values, and reputation;
- autonomy and operating model;
- legal, IP, and risk;
- portfolio rights and career leverage;
- offer packet quality.

## Trade-Off Examples To Elicit

Ask whether patterns like these apply:

- full-time is preferred, but contract work is acceptable above a premium;
- remote is preferred, but hybrid local is acceptable for strong work;
- in-office is acceptable only above a compensation, mission-fit, or career-leverage threshold;
- travel is acceptable if planned, reimbursed, and capped;
- lower cash is acceptable with meaningful equity, public proof, or strategic career value;
- a weaker title is acceptable with strong scope and decision rights;
- a boring domain is acceptable for exceptional compensation or low schedule load.

## Scoring Rules

Produce a 100-point rubric unless I request another scale.

For each category include:

- weight;
- required offer fields;
- preferred answers;
- acceptable answers;
- unacceptable answers;
- trade-off rules;
- whether private thresholds are needed.

Use these statuses:

- `dealbreaker`
- `preferred`
- `acceptable`
- `acceptable_with_tradeoff`
- `requires_clarification`
- `not_acceptable`

## Privacy Rules

Keep public-safe priorities in this repo. Put sensitive compensation floors, private constraints, family details, immigration details, or negotiation thresholds in a private overlay unless I explicitly approve public storage.

## Output Rules

- Do not invent preferences.
- If I have not answered enough questions, leave `TODO` values.
- Make the YAML parseable.
- Make the Markdown understandable to a human reading the repo on GitHub.
- Preserve the distinction between dealbreakers, weighted preferences, and trade-off rules.
