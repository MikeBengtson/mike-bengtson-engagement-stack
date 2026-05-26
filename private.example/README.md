# Private Overlay Example

This folder is a committed example. Do not put real private data here.

For a real user stack, copy this folder to `private/`:

```sh
cp -R private.example private
```

`private/` is ignored by `.gitignore`, so it stays local by default.

## What Belongs In `private/`

Use private overlays for information that should not appear in the public repo:

- salary floors and target compensation;
- hourly, retainer, and fixed-bid rate floors;
- negotiation thresholds;
- private work authorization details;
- family, health, relocation, commute, or schedule constraints;
- current employer constraints;
- sensitive dealbreakers;
- private references;
- unredacted offer packets;
- highly targeted resume shaders or generated resumes.

## How Agents Should Use It

When evaluating an offer, agents should read public files first, then private overlays if present:

1. `engagements/current-preferences.md`
2. `engagements/current-preferences.yaml`
3. `engagements/evaluation-rubric.md`
4. `engagements/evaluation-rubric.yaml`
5. `engagements/offer-packet.schema.yaml`
6. `private/*.private.md`
7. `private/*.private.yaml`

If private files are absent, agents must not infer hidden floors or constraints. They should mark the relevant category `requires_clarification`.

## Safety Check

Before publishing, run:

```sh
git status --ignored --short
```

Files under `private/` should appear as ignored, not staged.
