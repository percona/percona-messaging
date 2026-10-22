# Automation

This directory contains configuration files that power repository automation checks.

For the full automation system map (workflows + scripts + config + AI usage), see [AUTOMATION.md](../AUTOMATION.md).

## Files

- `messaging-impact-map.yml`: rules-based mapping of changed topics to files that must be reviewed
- `lychee-quarterly-review-citations.json`: URLs excluded from lychee in CI; source for the [quarterly citation review workflow](../.github/workflows/quarterly-citation-review.yml) (keep in sync with `.lychee.toml` `exclude` for those URLs)

## How configuration is used

- `scripts/impact_check.py` reads `messaging-impact-map.yml` during pull request checks

## Coverage model

Rules declare **`must_review`** paths (and optional **`suggest_globs`** for non-blocking breadth). There is no guarantee every propagation target under `framework/`, `products/`, `use-cases-value-pillars/`, or `offerings/` appears for a given change: if reviews keep finding gaps, add or tighten rules in **`messaging-impact-map.yml`**. See [AUTOMATION.md](../AUTOMATION.md) (`Impact Check: scope and limits`).

## Related components

- Workflow triggers and orchestration: [`.github/workflows/`](../.github/workflows/)
- Script implementations: [scripts/README.md](../scripts/README.md)
