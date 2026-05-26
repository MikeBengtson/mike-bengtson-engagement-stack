# Offer Evaluation Prompt

I want to evaluate an engagement offer against this Engagement Stack.

Read:

- `engagements/current-preferences.md`
- `engagements/current-preferences.yaml`
- `engagements/engagement-models.md`
- `engagements/evaluation-rubric.md`
- `engagements/evaluation-rubric.yaml`
- `engagements/offer-packet.schema.yaml`
- any available `private/*.private.md` or `private/*.private.yaml`

Then parse the offer I provide.

## Process

1. Validate the offer against `engagements/offer-packet.schema.yaml`.
2. If required fields are missing, draft a clarification email before scoring.
3. Check the offer against rubric dealbreakers and any private overlay constraints.
4. Score each rubric category that has enough information.
5. For any category that cannot be scored, mark it `requires_clarification`.
6. Apply trade-off rules explicitly. Do not hide a weak category inside a blended score.
7. Produce:
   - total score;
   - category scores;
   - dealbreaker status;
   - missing fields;
   - trade-offs that could improve fit;
   - recommended response.

If private overlays are absent, do not infer salary floors, work authorization details, or sensitive constraints. Mark those categories `requires_clarification` when needed.

If scoring weights are still placeholders, say so and provide a qualitative evaluation only.
