# Data

This directory stores canonical machine-readable registries used by messaging automation.

## Files

- `case-studies.json`: manual case-study registry updated when maintainers adopt published proof (see monthly [case study maintenance reminder](../.github/workflows/case-study-maintenance-reminder.yml))
- `docs_whats_new_seen_guids.json`: RSS item GUIDs already handled by the optional Docs What's New **backup** monitor (issue opened or skipped as duplicate). Updated via automation PRs from the monitor workflow after each run; see [AUTOMATION.md](../AUTOMATION.md).

## Notes

- Keep this data factual and sourceable.
- Automated sync workflows may update this file through pull requests.
