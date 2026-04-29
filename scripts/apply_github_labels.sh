#!/usr/bin/env bash
# Apply or update labels from .github/label-definitions.json (requires: gh, jq, repo auth).
# Usage: from repo root, ./scripts/apply_github_labels.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
JSON="${ROOT}/.github/label-definitions.json"
if ! command -v gh >/dev/null 2>&1; then
  echo "gh (GitHub CLI) is not installed" >&2
  exit 1
fi
if ! command -v jq >/dev/null 2>&1; then
  echo "jq is not installed" >&2
  exit 1
fi
if [[ ! -f "$JSON" ]]; then
  echo "Missing ${JSON}" >&2
  exit 1
fi

# One-time migration: rename legacy GitHub default label when needed.
if gh label list --limit 200 --search "documentation" --json name | jq -e '.[] | select(.name=="documentation")' >/dev/null 2>&1 \
  && ! gh label list --limit 200 --search "messaging" --json name | jq -e '.[] | select(.name=="messaging")' >/dev/null 2>&1; then
  gh label edit "documentation" --name "messaging" --description "Improvements or additions to messaging"
fi

count=$(jq 'length' "$JSON")
i=0
while [[ "$i" -lt "$count" ]]; do
  name=$(jq -r --argjson idx "$i" '.[$idx].name' "$JSON")
  color=$(jq -r --argjson idx "$i" '.[$idx].color' "$JSON")
  desc=$(jq -r --argjson idx "$i" '.[$idx].description' "$JSON")
  # --force: update in place if label already exists (gh 2.4+)
  gh label create "$name" --color "$color" --description "$desc" --force
  i=$((i + 1))
done
echo "Applied ${count} label(s)."
