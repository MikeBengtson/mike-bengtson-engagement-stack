#!/usr/bin/env sh
set -eu

missing=0

while IFS= read -r path; do
  [ -z "$path" ] && continue
  if [ ! -f "$path" ]; then
    echo "Missing required file: $path"
    missing=1
  fi
done <<'EOF'
README.md
AGENTS.md
profile/README.md
profile/identity.md
profile/identity.yaml
cv/README.md
cv/canonical-cv.md
cv/canonical-cv.yaml
cv/work-history.md
cv/work-history.yaml
cv/skills.md
cv/skills.yaml
portfolio/README.md
evidence/README.md
career-strategy/README.md
engagements/README.md
engagements/current-preferences.md
engagements/current-preferences.yaml
engagements/evaluation-rubric.md
engagements/evaluation-rubric.yaml
engagements/request-instructions.md
resume-shaders/README.md
submissions/README.md
EOF

if [ "$missing" -ne 0 ]; then
  exit 1
fi

echo "Required file check passed."

todo_count="$(grep -RIn "TODO" README.md AGENTS.md setup framework profile cv portfolio evidence engagements resume-shaders submissions prompts integrations maintenance templates 2>/dev/null | wc -l | tr -d ' ')"
echo "TODO count: $todo_count"
