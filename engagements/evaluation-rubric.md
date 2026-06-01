# Engagement Evaluation Rubric

Use this file to describe how engagement opportunities should be evaluated. It should be readable by humans first: recruiters, hiring managers, clients, collaborators, and the person maintaining this stack.

The companion YAML file, `evaluation-rubric.yaml`, is the agent-readable scoring surface.

## Purpose

This rubric clarifies:

- what the person prefers;
- what is acceptable;
- what is a dealbreaker;
- what trade-offs could make a weaker offer acceptable;
- what information an offer packet must include before it can be scored.

The rubric should not be treated as a rigid vending machine. It is a decision aid. Strong offers can still require conversation, and weak offers can still reveal useful opportunities.

## Top Priorities

Three co-equal top priorities sit above the weighted categories below. They gate fit before scoring nuances:

1. **A true agentic pipeline** — working on a genuine agentic pipeline, not AI as a label on legacy work.
2. **Organization-wide AI impact** — the chance for organization-wide impact with AI efforts.
3. **Income to expectations** — income/revenue in keeping with his expectations. Figures are not stated here; they live in the private overlay (`private/compensation.private.yaml`).

## Hard Dealbreakers

Any one of these is an automatic no, regardless of category scores:

- mandatory or full in-office;
- any relocation;
- travel above 10%.

## Priority Categories

### Engagement Model

Describe the preferred and acceptable forms of engagement:

- full-time employment;
- part-time employment;
- hourly contract;
- fixed-bid project;
- retained consulting;
- advisory or fractional role;
- outcome-based, assignment-based, or consignment-based work;
- founding or cofounding role;
- board, advisor, or expert-network engagement.

Clarify trade-offs. For example: full-time may be preferred, but contract work may be acceptable above a premium rate; advisory may be acceptable only with a narrow scope and low meeting load.

### Compensation And Economics

Document the economics that matter:

- salary, hourly rate, fixed fee, retainer, or budget range;
- contractor hourly minimum, target, and maximum/stretch quote;
- contractor rate basis, such as W2 contract, 1099, corp-to-corp, retainer-equivalent, expected billable hours, and whether the rate includes taxes, benefits, insurance, equipment, travel, fees, unpaid time, or bench time;
- bonus, commission, equity, token, or upside structure;
- benefits and paid time off;
- payment schedule;
- deposit or prepayment requirements;
- expense reimbursement;
- premium required for contracting, in-office work, travel, urgency, exclusivity, or risk.

Sensitive compensation floors should live in a private overlay such as `private/compensation.private.yaml`.

### Location And Physical Presence

Score remote, hybrid, in-office, relocation, commute, and timezone requirements.

Examples:

- remote may be preferred;
- hybrid may be acceptable if local;
- in-office may be acceptable only for unusually strong compensation, mission fit, or career leverage;
- relocation may be unacceptable or require a separate premium.

### Travel And Schedule Load

Evaluate:

- expected travel percentage;
- notice period;
- weekend travel;
- international travel;
- on-call or emergency expectations;
- meeting load;
- timezone spread;
- weekly capacity.

### Work Authorization And Compliance

Capture requirements such as:

- citizenship;
- permanent residency;
- H1B or other visa sponsorship;
- EAD or work permit;
- security clearance;
- export-control restrictions;
- background checks;
- professional licenses;
- country, state, or jurisdiction constraints.

This section helps agents reject or clarify offers that cannot legally work.

### Role And Scope Fit

Evaluate:

- title and seniority;
- individual contributor vs manager vs executive/operator;
- hands-on delivery vs advisory work;
- ownership and decision rights;
- ambiguity level;
- team size;
- reporting line;
- expected outcomes.

### Technical, Domain, And Craft Fit

Score fit against preferred skills, stacks, domains, and problem types. Also document avoided work: stale stacks, low-agency maintenance, misaligned industries, or work that does not build on the person's strengths.

### Mission, Values, And Reputation

Capture industries, products, customers, or organizational behaviors that increase or decrease fit. Include reputational risk and ethical boundaries.

### Autonomy And Operating Model

Evaluate:

- decision rights;
- management style;
- async vs meeting-heavy culture;
- documentation quality;
- ability to choose tools and process;
- bureaucracy;
- stakeholder access.

### Legal, IP, And Risk

Evaluate:

- IP assignment;
- invention assignment;
- confidentiality;
- noncompete;
- nonsolicit;
- liability and indemnity;
- arbitration and governing law;
- cancellation terms;
- payment risk;
- exclusivity.

### Portfolio Rights And Career Leverage

Score whether the engagement creates durable proof:

- public case study rights;
- GitHub or open-source contribution rights;
- permission to cite the work;
- testimonial or reference potential;
- recognizable brand value;
- network access;
- skill compounding.

### Offer Packet Quality

An offer that cannot be evaluated should not receive a confident score. Missing fields should produce a clarification request before scoring.

## Trade-Off Rules

Trade-off rules describe when the person would bend on a preference.

Examples:

- Full-time employment is preferred, but contracting is acceptable at a meaningful premium.
- Remote is preferred, but hybrid local is acceptable for strong work and a clear schedule.
- In-office is weak by default, but may become acceptable if compensation, mission fit, and career leverage are unusually strong.
- Travel is acceptable when planned and reimbursed, but not when frequent, unpaid, or short-notice.
- A lower-cash offer may be acceptable with strong equity, public proof, elite learning, or mission fit.

## Offer Validation

Before scoring, an agent should check whether the offer packet includes enough information for each high-weight category. If not, draft a clarification request instead of inventing assumptions.

## Private Overlay

This public rubric can say that a premium or threshold exists without revealing the number. Real salary floors, target compensation, private work authorization details, current-employer constraints, family or health constraints, and negotiation strategy should live under ignored `private/` files.

Sensitive data lives in a local, gitignored `private/` overlay (`private/compensation.private.yaml`, `private/constraints.private.yaml`, `private/negotiation.private.md`) that is never committed. If private overlays are absent, agents should not infer hidden thresholds — ask.
