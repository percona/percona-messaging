# Repository Automation

This document is the single entry point for automation across the repository.

It explains how `.github/workflows/`, `scripts/`, and `automation/` work together.

## Automation architecture

- `**.github/workflows/**`: when automation runs (triggers, permissions, PR comments, scheduled jobs).
- `**scripts/**`: what automation executes (Python logic for checks, reports, and sync tasks).
- `**automation/**`: automation inputs (impact map, claim categories, and other config data).
- `**data/**`: machine-readable inputs/outputs used by automation (for example case-study registry and processed RSS GUID state).

## Workflow map


| Workflow                                          | Trigger                                     | Uses scripts                                                                                 | Uses config/data                                                    | Output                                            |
| ------------------------------------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------- |
| `.github/workflows/terminology-check.yml`         | PR touching `*.md`                          | inline shell checks                                                                          | repository markdown content                                         | Fails/warns on banned terms and naming issues     |
| `.github/workflows/impact-check.yml`              | PR touching markdown/impact map/script      | `scripts/impact_check.py`                                                                    | `automation/messaging-impact-map.yml`                               | PR comment + summary with impact checklist        |
| `.github/workflows/smart-suggestions.yml`         | PR touching markdown/automation/script      | `scripts/suggest_updates.py`                                                                 | `automation/messaging-impact-map.yml`, `automation/claim-types.yml` | PR comment with suggestion candidates             |
| `.github/workflows/content-governance-checks.yml` | PR touching markdown/template/check scripts | `scripts/new_file_gate.py`, `scripts/check_doc_coverage.py`, `scripts/duplicate_detector.py` | PR template + markdown corpus                                       | PR governance comment; fails on blocking checks   |
| `.github/workflows/staleness-report.yml`          | Weekly schedule + manual dispatch           | `scripts/staleness_report.py`                                                                | git history + markdown corpus                                       | Updates/creates maintenance staleness issue       |
| `.github/workflows/case-study-monitor.yml`        | Weekly schedule + manual dispatch           | `scripts/sync_case_studies.py`, `scripts/suggest_updates.py`                                 | external feed -> `data/case-studies.json`                           | Creates/updates automation PR with refreshed data |
| `.github/workflows/prose-and-links.yml`         | PR touching markdown or prose config        | _(none — uses marketplace actions)_                                                          | `_typos.toml`, `.lychee.toml`, `.markdownlint.yaml`                 | Spelling, markdown structure, external link health |
| `.github/workflows/quarterly-citation-review.yml` | Quarterly (15 Jan/Apr/Jul/Oct) + manual dispatch | `scripts/quarterly_lychee_citation_review_issue.py`                                      | `automation/lychee-quarterly-review-citations.json`                 | New issue listing CI-excluded citation URLs for human verification |
| `.github/workflows/docs-whats-new-monitor.yml`    | Daily schedule + manual dispatch (opt-in)     | `scripts/docs_whats_new_monitor.py`                                                          | RSS feed + `data/docs_whats_new_seen_guids.json`                    | New `product-update` issues (backup intake); PR updates GUID state |


## Docs What's New monitor (optional)

**Role:** This is a **secondary, catch-all safety net**, not the primary way canonical messaging stays current. Product and GTM should still drive versioned updates through the normal **Product release update** process (release artifacts, owners, and timelines). The monitor exists so that if something ships and **no one files an issue**, we still get a **triage signal** from the official Percona Documentation **What's New** RSS feed (not HTML scraping) before announcements age off the feed.

When enabled, scheduled automation watches that feed and opens GitHub issues aligned with the **Product release update** template flow (`product-update` label, `[Release]` title prefix). Treat opened issues as **intake to confirm or close**, not as an authoritative release checklist.

| Detail | Value |
| ------ | ----- |
| Workflow | [`.github/workflows/docs-whats-new-monitor.yml`](.github/workflows/docs-whats-new-monitor.yml) |
| Script | [`scripts/docs_whats_new_monitor.py`](scripts/docs_whats_new_monitor.py) |
| Feed | [`https://docs.percona.com/feed_rss_created.xml`](https://docs.percona.com/feed_rss_created.xml) (human hub: [What's new](https://docs.percona.com/new/)) |
| State file | [`data/docs_whats_new_seen_guids.json`](data/docs_whats_new_seen_guids.json) |
| Enable | Repository **Settings → Secrets and variables → Actions → Variables**: set `DOCS_WHATS_NEW_MONITOR_ENABLED` to `true` |
| Labels | The workflow applies **`product-update`**, matching the [Product release update](.github/ISSUE_TEMPLATE/product-release-update.md) template; create that label on the repo if it does not exist yet. |

**Cadence and limits:** the feed only exposes a bounded number of recent items; keep the workflow enabled and on a daily schedule so new announcements are not missed before they roll off the feed.

**Bootstrap / recovery** (refresh state without opening issues for everything currently in the feed):

```bash
python scripts/docs_whats_new_monitor.py bootstrap --state data/docs_whats_new_seen_guids.json
```

## Where automation runs in the contributor flow

1. Contributor opens a PR.
2. PR workflows run checks and publish comments/summaries.
3. Maintainers/domain owners review both content and automation feedback.
4. Blocking checks must pass before merge.
5. Scheduled workflows create maintenance artifacts (issues/PRs) outside normal PR flow.

See [CONTRIBUTING.md](CONTRIBUTING.md) for contributor-facing workflow behavior and [GOVERNANCE.md](GOVERNANCE.md) for review/approval policy.

## AI and automation: how to use AI responsibly

AI can help design or refine automations, but should not replace deterministic enforcement where exact rules are required.

Use this decision pattern for each automation use case:

- **Deterministic check** when policy is explicit and binary (for example banned terms, required PR fields).
- **AI-assisted check** when inference or broader contextual suggestions are needed.
- **Hybrid** when deterministic gating plus AI suggestions gives the best coverage.

When using AI to change automation, always include:

- Intended failure mode (what should be caught)
- Scope boundaries (what should *not* be caught)
- False-positive tolerance and reviewer expectation
- Output format (blocking error, warning, PR comment, issue, or report)

## Planned and candidate automation backlog

This list is intentionally broader than current implementation so ideas are not lost before issues are opened.

### Planned next (high-confidence, near-term)

- PR launch-readiness label consistency checks (`ready-for-launch`, `go-live:`*)
- Reviewer-SLA reminder automations for aging approvals
- Confidence tracking for suggestion precision/recall over time

### Candidate next wave (needs scoping)

- Decomposition-completeness assistant for propagation coverage
- Canonical-link integrity check (new/changed docs must be discoverable from navigation docs)
- Automation regression tests for scripts (fixture-based expected outputs)
- Auto-triage labeler for incoming issues (`intake`, `decomposition`, `governance`, `automation`, `training`)
- PR change-risk scorer to suggest required reviewer set based on touched areas

### Longer-horizon ideas

- Suggestion quality feedback loop (reviewers mark suggestions useful/not useful to improve scoring)
- Cross-repo adaptation watcher for known downstream channels (report-only, no auto-write)
- "Missed propagation" post-merge auditor that samples merged PRs for coverage gaps
- **Downstream-asset impact tracking:** a maintained registry of execution assets that consume canonical messaging (e.g. slide decks, web pages, datasheets, sales tools). When this repo changes, automation (or a scheduled job) checks the map and **notifies** asset owners of what may need a refresh, without assuming direct write access to those systems

Track opportunities as issues labeled `automation`.  
Until issues are opened, keep this section as the backlog source of truth.

## Automation intake rubric (before opening an issue)

Use this quick filter so automation scope stays practical:

- **Failure mode:** what concrete problem does this catch?
- **Signal quality:** what false-positive rate is acceptable?
- **Blast radius:** which files/workflows are affected?
- **Enforcement mode:** block, warn, comment, report, or scheduled issue?
- **Owner and cadence:** who maintains it, and how often is it reviewed?

## Local validation

See [scripts/README.md](scripts/README.md) for script-level usage.  
When testing PR-based scripts locally, run against a base/head git range similar to CI.

For spelling, links, and markdown structure, use the same tools as [prose-and-links.yml](.github/workflows/prose-and-links.yml): `typos` (see `_typos.toml`), `lychee` (see `.lychee.toml`), and `markdownlint-cli2` (see `.markdownlint.yaml`). Markdownlint enforces structure, not grammar or product voice.