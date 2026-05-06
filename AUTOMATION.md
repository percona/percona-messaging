# Repository Automation

This document is the single entry point for automation across the repository.

It explains how `.github/workflows/`, `scripts/`, and `automation/` work together.

## Automation architecture

- `**.github/workflows/**`: when automation runs (triggers, permissions, PR comments, scheduled jobs).
- `**scripts/**`: what automation executes (Python logic for checks, reports, and sync tasks).
- `**automation/**`: automation inputs (impact map, claim categories, and other config data).
- `**data/**`: machine-readable inputs/outputs used by automation (for example case-study registry and processed RSS GUID state).

## Documentation ownership boundary

- Tracking backlog and issue intake live in [reference/launch-and-automation-backlog.md](reference/launch-and-automation-backlog.md).
- Operational runbooks and sign-off protocols live in [scripts/README.md](scripts/README.md) under `Validation sign-off runbooks`.
- Keep runbook procedure steps out of backlog trackers.
- Backlog docs should point to canonical runbook sections.

## Operational setup references

- Labels: [.github/label-definitions.json](.github/label-definitions.json) and [scripts/apply_github_labels.sh](scripts/apply_github_labels.sh) (details in [scripts/README.md](scripts/README.md) under `GitHub labels`).
- Project field and item automation commands: [gh project manual](https://cli.github.com/manual/gh_project).
- Validation sign-off execution protocols: [scripts/README.md](scripts/README.md) under `Validation sign-off runbooks`.
- Example `Launch track` field creation command:
  - `gh project field-create <number> --owner percona --name "Launch track" --data-type SINGLE_SELECT --single-select-options "P0 Go-live,P1 Soon,P2 Later,Not launch"`

## Workflow map


| Workflow                                          | Trigger                                           | Uses scripts                                                                                 | Uses config/data                                                    | Output                                                             |
| ------------------------------------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `.github/workflows/terminology-check.yml`         | PR touching `*.md`, Vale config, or tool versions | inline shell checks                                                                          | repository markdown content + `automation/tool-versions.json`       | Fails/warns on banned terms and naming issues                      |
| `.github/workflows/impact-check.yml`              | PR touching markdown/impact map/script            | `scripts/impact_check.py`                                                                    | `automation/messaging-impact-map.yml`                               | PR comment + summary with impact checklist                         |
| `.github/workflows/impact-slash-commands.yml`     | PR comments beginning with `/impact-ok`, `/impact-reset`, or `/impact-all` | `scripts/impact_check.py`                                                                    | hidden waiver comment + `automation/messaging-impact-map.yml`       | Updates waivers and refreshes impact checklist                     |
| `.github/workflows/smart-suggestions.yml`         | PR touching markdown/automation/script            | `scripts/suggest_updates.py`                                                                 | `automation/messaging-impact-map.yml`, `automation/claim-types.yml` | PR comment with suggestion candidates                              |
| `.github/workflows/content-governance-checks.yml` | PR touching markdown/template/check scripts       | `scripts/new_file_gate.py`, `scripts/check_doc_coverage.py`, `scripts/duplicate_detector.py`, `scripts/governance_waiver.py` | PR template + markdown corpus + hidden waiver comment               | PR governance comment; fails on blocking checks                    |
| `.github/workflows/governance-slash-commands.yml` | PR comments `/governance-ok`, `/governance-reset`, `/governance-all` | same governance scripts                                                                      | hidden waiver comment (`messaging-governance-waiver-data:v1`)      | Updates waivers, refreshes governance comment, reruns governance workflow |
| `.github/workflows/staleness-report.yml`          | Weekly schedule + manual dispatch                 | `scripts/staleness_report.py`                                                                | git history + markdown corpus                                       | Updates/creates maintenance staleness issue                        |
| `.github/workflows/case-study-monitor.yml`        | Weekly schedule + manual dispatch                 | `scripts/sync_case_studies.py`, `scripts/suggest_updates.py`                                 | external feed -> `data/case-studies.json`                           | Creates/updates automation PR with refreshed data                  |
| `.github/workflows/prose-and-links.yml`           | PR touching markdown or prose config              | *(none, uses marketplace actions)*                                                           | `_typos.toml`, `.lychee.toml`, `.markdownlint.yaml`                 | Spelling, markdown structure, external link health                 |
| `.github/workflows/quarterly-citation-review.yml` | Quarterly (15 Jan/Apr/Jul/Oct) + manual dispatch  | `scripts/quarterly_lychee_citation_review_issue.py`                                          | `automation/lychee-quarterly-review-citations.json`                 | New issue listing CI-excluded citation URLs for human verification |
| `.github/workflows/docs-whats-new-monitor.yml` | Daily schedule + manual dispatch (opt-in) | `scripts/docs_whats_new_monitor.py` | RSS feed + `data/docs_whats_new_seen_guids.json` | New `product-update` issues (backup intake) |

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
| Labels | The workflow applies **`product-update`** (matching the [Product release update](.github/ISSUE_TEMPLATE/product-release-update.md) template) plus **`Area:*`** labels inferred from the announcement title (for example `Area: PostgreSQL`). Labels must exist in the repo (see [.github/label-definitions.json](.github/label-definitions.json)). |

**Cadence and limits:** the feed only exposes a bounded number of recent items; keep the workflow enabled and on a daily schedule so new announcements are not missed before they roll off the feed.

**Dedupe behavior:** the workflow dedupes by searching for a stable GUID hash marker in existing issue bodies before creating a new issue. It does not open automation PRs for state updates.

**Area labeling:** classification uses keywords from the RSS title (and falls back to `Area: Cross-product` when no rule matches). Adjust mapping logic in [`.github/workflows/docs-whats-new-monitor.yml`](.github/workflows/docs-whats-new-monitor.yml) when naming patterns change.

**Bootstrap / recovery** (refresh state without opening issues for everything currently in the feed):

```bash
python scripts/docs_whats_new_monitor.py bootstrap --state data/docs_whats_new_seen_guids.json
```


### Impact Check waivers (`/impact-ok`)

When **required** impact rules list `must_review` files that you will **not** edit in this PR, a maintainer (**Owner**, **Member**, or **Collaborator**) can acknowledge that in-band:

- Comment **`/impact-ok all`** on the PR to waive every missing required path for the current diff (equivalent to applying the **`impact-check-waived`** label, which `impact-check.yml` still merges into waiver state).
- Comment **`/impact-ok <path>`** once per file, using the **exact** backticked path from the checklist (example: `/impact-ok reference/canonical-naming.md`).

The workflow [`.github/workflows/impact-slash-commands.yml`](.github/workflows/impact-slash-commands.yml) stores state in a hidden PR comment (`<!-- messaging-impact-waiver-data:v1 -->` + JSON), then re-runs `impact_check.py` and **updates the same checklist comment** as the normal Impact Check. Remove waivers or re-run checks if the diff changes materially. Restrict who can use slash commands by repo role (same as label bypass).

## Where automation runs in the contributor flow

1. Contributor opens a PR.
2. PR workflows run checks and publish comments/summaries.
3. Maintainers/domain owners review both content and automation feedback.
4. Blocking checks must pass before merge.
5. Scheduled workflows create maintenance artifacts (issues/PRs) outside normal PR flow.

See [CONTRIBUTING.md](CONTRIBUTING.md) for contributor-facing workflow behavior and [GOVERNANCE.md](GOVERNANCE.md) for review/approval policy.

## Impact check manual acknowledgement

For false positives where maintainers agree no edit is needed in a listed `must_review` file:

- Comment `/impact-ok all` to acknowledge all currently missing required paths (you can add a short note on the same line after `all`; only the first word on the first line is read as the argument).
- Comment `/impact-all` as a shortcut for `/impact-ok all`.
- Comment `/impact-ok <exact path>` to acknowledge one path at a time (same rule: optional same-line text after the path is ignored).
- Comment `/impact-reset all` to clear all recorded waivers for the PR.
- Comment `/impact-reset <exact path>` to remove one waiver. If `/impact-ok all` is active, this path-specific reset is stored as an explicit exception.

The slash-command workflow stores waiver state in a hidden PR comment and re-runs the impact check so the checklist comment reflects waived items.

## Content governance manual acknowledgement

When maintainers agree a governance gate is satisfied outside automation (or the gate is a false positive):

- Comment `/governance-ok all` or `/governance-all` to waive **all three** blocking gates for that PR (new file justification, doc navigation coverage, duplicate detector).
- Comment `/governance-ok new-file`, `/governance-ok doc-coverage`, or `/governance-ok duplicate` to waive **one** gate at a time (aliases: `coverage` maps to doc coverage; `dupes` maps to duplicate).
- Comment `/governance-reset all` to clear waiver state for the PR.
- Comment `/governance-reset <same token>` to remove one waiver. While `/governance-ok all` is active, a path-specific reset records an exception (same pattern as Impact Check reset paths).

The slash-command workflow stores JSON in a hidden PR comment (`messaging-governance-waiver-data:v1`), refreshes the visible governance report, and requests a rerun of **Content Governance Checks** so check status matches waiver state.

Waiver state resolution rule:

- Impact Check and Content Governance use **different** hidden markers (`messaging-impact-waiver-data:v1` vs `messaging-governance-waiver-data:v1`); each workflow only reads its own marker.
- If multiple waiver marker comments exist for that marker, automation selects the newest created comment with valid JSON.
- If the newest created payload is malformed, automation falls back to the next newest valid payload.
- If no valid payload exists, automation uses an empty waiver state.

## Impact Check and Smart Suggestions: scope and limits

**Impact Check** (`impact-check.yml`, `scripts/impact_check.py`) evaluates pull request diffs against **`automation/messaging-impact-map.yml`**. It lists **`must_review`** paths when rule triggers match (file globs and optional diff regexes). It does **not** compute a full propagation graph across the repo, infer impact levels (low / medium / high), or replace the human flow in [reference/decomposition-and-propagation.md](reference/decomposition-and-propagation.md) or **`.cursor/rules/impact-analysis.mdc`**.

**Smart Suggestions** (`smart-suggestions.yml`, `scripts/suggest_updates.py`) combines the same impact map with **`automation/claim-types.yml`** to propose additional candidates. Treat both Impact Check and Smart Suggestions comments as **map-backed hints**: extend coverage by editing `messaging-impact-map.yml` (and claim hints) when reviews repeatedly surface misses.

**Canonical messaging directories** (`framework/`, `products/`, `use-cases-value-pillars/`, `offerings/`) are routing targets for decomposition; automation only surfaces files that rules enumerate. Reviewers remain responsible for cross-module consistency when claims move.

## PR comment upsert standard

Marker-managed PR comments must use the shared helper at `scripts/github/upsert_marker_comment.js`.

- Keep marker strings stable. Treat them as persistent IDs.
- Prefix the rendered comment body with the marker (`${marker}\n...`).
- Use one marker per workflow comment type (for example impact checklist, governance report, smart suggestions).
- Call the helper from `actions/github-script` steps instead of inlining list/update/create comment logic.
- For **human-visible** marker comments, pass `automationFooter: { workflowFile, eventName }` so the rendered comment ends with the triggering GitHub event, a link to the workflow file on `main`, and links to `AUTOMATION.md` (this section) and `automation/README.md`. Do **not** append this footer to hidden machine-readable marker payloads (for example waiver JSON comments).

Current workflows using this standard:

- `.github/workflows/content-governance-checks.yml`
- `.github/workflows/governance-slash-commands.yml` (governance report comment only; waiver payload comments omit the footer)
- `.github/workflows/impact-check.yml`
- `.github/workflows/impact-slash-commands.yml` (impact checklist comment only; waiver payload comments omit the footer)
- `.github/workflows/markdown-hygiene-autofix.yml`
- `.github/workflows/smart-suggestions.yml`

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
This section is tracking-only and should not duplicate runbook execution steps.

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
For sign-off execution protocols, see the `Validation sign-off runbooks` section in [scripts/README.md](scripts/README.md), including issue #9 (`new file gate`) and issue #15 (`multi-check integration smoke`).
When testing PR-based scripts locally, run against a base/head git range similar to CI.

For spelling, links, and markdown structure, use the same tools as [prose-and-links.yml](.github/workflows/prose-and-links.yml): `typos` (see `_typos.toml`), `lychee` (see `.lychee.toml`), and `markdownlint-cli2` (see `.markdownlint.yaml`). Markdownlint enforces structure, not grammar or product voice.

## Tool versions in automation

Repository-managed automation tool versions live in `automation/tool-versions.json`.

- **Vale version source of truth:** `automation/tool-versions.json` -> `vale.version`
- **Current consumer:** `.github/workflows/terminology-check.yml`
- **Bump path:** update `vale.version`, open PR, and confirm the workflow log prints `Using Vale v...` and `vale -v` for the updated version.