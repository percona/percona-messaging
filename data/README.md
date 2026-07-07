# Data

This directory stores canonical machine-readable registries used by messaging automation.

## Files

- `case-studies.json`: manual case-study registry updated when maintainers adopt published proof (see monthly [case study maintenance reminder](../.github/workflows/case-study-maintenance-reminder.yml))
- `docs_whats_new_seen_guids.json`: RSS item GUIDs already handled by the optional Docs What's New **backup** monitor (issue opened or skipped as duplicate). Updated via automation PRs from the monitor workflow after each run; see [AUTOMATION.md](../AUTOMATION.md).

## Notes

- Keep this data factual and sourceable.
- `case-studies.json` is updated manually via pull request when maintainers adopt published proof.
- `docs_whats_new_seen_guids.json` is updated by automation pull requests from the Docs What's New monitor after each run.
