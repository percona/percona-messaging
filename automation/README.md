# Automation

This directory contains configuration files that power repository automation checks.

For the full automation system map (workflows + scripts + config + AI usage), see [AUTOMATION.md](../AUTOMATION.md).

## Files

- `messaging-impact-map.yml`: rules-based mapping of changed topics to files that must be reviewed
- `claim-types.yml`: canonical claim categories and keyword hints used by suggestion tooling

## How configuration is used

- `scripts/impact_check.py` reads `messaging-impact-map.yml` during pull request checks
- `scripts/suggest_updates.py` combines `messaging-impact-map.yml` and `claim-types.yml` to generate reviewer suggestions
- `scripts/duplicate_detector.py` uses canonical markdown overlap checks to flag potential duplication

## Related components

- Workflow triggers and orchestration: [`.github/workflows/`](../.github/workflows/)
- Script implementations: [scripts/README.md](../scripts/README.md)