# Scripts

This directory contains Python scripts used by CI workflows and local validation.

For the cross-repo automation overview, see [AUTOMATION.md](../AUTOMATION.md).

## Pull request intelligence scripts

- `impact_check.py`: checks changed files against `automation/messaging-impact-map.yml`
- `suggest_updates.py`: generates deterministic suggestion candidates for impacted files
- `new_file_gate.py`: enforces required PR justification fields when new markdown files are added
- `check_doc_coverage.py`: verifies new markdown docs are linked from repository navigation docs
- `duplicate_detector.py`: detects high-overlap markdown content to reduce duplication

## External signal script

- `sync_case_studies.py`: syncs case-study data from an external JSON feed
- `staleness_report.py`: builds scheduled stale-content maintenance reports
- `quarterly_lychee_citation_review_issue.py`: builds the body for the quarterly CI-excluded citation URL review issue

## GitHub workflow helper scripts

- `github/upsert_marker_comment.js`: shared marker-based upsert helper for workflow-managed PR comments

## Workflow entry points

- `.github/workflows/impact-check.yml` -> `impact_check.py`
- `.github/workflows/smart-suggestions.yml` -> `suggest_updates.py`
- `.github/workflows/content-governance-checks.yml` -> `new_file_gate.py`, `check_doc_coverage.py`, `duplicate_detector.py`
- `.github/workflows/staleness-report.yml` -> `staleness_report.py`
- `.github/workflows/quarterly-citation-review.yml` -> `quarterly_lychee_citation_review_issue.py`
- `.github/workflows/case-study-monitor.yml` -> `sync_case_studies.py`, `suggest_updates.py`

## AI-assisted automation development

AI is useful for proposing rules, test cases, and script refactors, but each change should be validated against expected false positives/false negatives before merge.

When requesting AI help for script changes, include:

- target workflow and script name
- the exact failure mode to catch
- allowed exceptions and boundary conditions
- expected output format (exit code, markdown report, JSON artifact, PR comment content)

## GitHub labels

Human-readable label names, colors, and descriptions live in [`.github/label-definitions.json`](../.github/label-definitions.json) (for example **`P0 - launch blocker`**, **`Automation & CI`**, not `area/automation`). After the remote repository exists, run [`apply_github_labels.sh`](apply_github_labels.sh) (requires `gh` and `jq`, and a logged-in `gh auth login` session) to create or update labels in place on GitHub.

## Prose, spelling, and links (not Python)

[Prose and links](../.github/workflows/prose-and-links.yml) uses marketplace actions; configuration lives in the repo root:

- **Spelling:** install [`typos`](https://github.com/crate-ci/typos) locally, or rely on CI; config [`_typos.toml`](../_typos.toml).
- **External URLs:** [`lychee`](https://github.com/lycheeverse/lychee) with [`.lychee.toml`](../.lychee.toml).
- **Markdown structure** (not product grammar): [`markdownlint-cli2`](https://github.com/DavidAnson/markdownlint-cli2) with [`.markdownlint.yaml`](../.markdownlint.yaml) and [`.markdownlintignore`](../.markdownlintignore).

Local markdownlint commands (same tool as CI):

- Check: `npx -y markdownlint-cli2@0.22.1 "**/*.md"`
- Autofix whitespace: `npx -y markdownlint-cli2@0.22.1 --fix "**/*.md"`
