# Scripts

This directory contains Python scripts used by CI workflows and local validation.

For the cross-repo automation overview, see [AUTOMATION.md](../AUTOMATION.md).

## Pull request intelligence scripts

- `impact_check.py`: checks changed files against `automation/messaging-impact-map.yml`
  - applies waiver state from slash commands (`/impact-ok`, `/impact-reset`) including path-specific resets when `all` is active
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
  - when duplicate marker comments exist, the helper updates the newest created marker comment and logs a warning

## Workflow entry points

- `.github/workflows/impact-check.yml` -> `impact_check.py`
- `.github/workflows/smart-suggestions.yml` -> `suggest_updates.py`
- `.github/workflows/content-governance-checks.yml` -> `new_file_gate.py`, `check_doc_coverage.py`, `duplicate_detector.py`
- `.github/workflows/staleness-report.yml` -> `staleness_report.py`
- `.github/workflows/quarterly-citation-review.yml` -> `quarterly_lychee_citation_review_issue.py`
- `.github/workflows/case-study-monitor.yml` -> `sync_case_studies.py`, `suggest_updates.py`
- `.github/workflows/markdown-hygiene-autofix.yml` -> `markdownlint-cli2 --fix` with `automation/markdown-hygiene-autofix.jsonc`

## Validation sign-off runbooks

Operational ownership note: this section is the canonical home for sign-off execution protocols. Backlog trackers should link here instead of duplicating procedure steps.

- Issue #9 new file gate: see `New file gate sign-off protocol (issue #9)` below and [issue #9](https://github.com/percona/percona-messaging/issues/9).
- Issue #15 multi-check integration smoke: see `Multi-check integration smoke sign-off protocol (issue #15)` below and [issue #15](https://github.com/percona/percona-messaging/issues/15).

## New file gate sign-off protocol (issue #9)

Use this protocol to produce low-lift PASS or FAIL evidence for `new_file_gate.py` in `.github/workflows/content-governance-checks.yml`.

### When to use this runbook

- Use when validating issue #9 behavior before go-live sign-off.
- Use after changing `new_file_gate.py`, the PR template fields it evaluates, or workflow wiring in `content-governance-checks.yml`.

### Preconditions

- Run from a branch in this repository (not a fork) so PR comment upserts can write.
- Keep the PR as draft during validation.
- Use one throwaway markdown path for validation, then remove it before merge if needed.

### Deterministic scenarios

1. **Pass path:** add one new `.md` file and complete all required PR-body headings with specific content.
2. **Fail path:** keep the same `.md` file, but leave one required heading empty or weak (for example `TBD`).
3. **No-op path:** remove the added `.md` file and push again to confirm the check reports no added markdown files.

Expected outcomes:

- Pass path: `Content Governance Checks` is green for `new_file_gate`.
- Fail path: `new_file_gate` fails, the report lists missing or insufficient sections, and includes scaffold guidance.
- No-op path: report says no added markdown files detected and remains non-blocking.

### Sign-off record

- Post `@brianamarie Sign-off: PASS | FAIL - <one line>`.
- Add 3 to 5 bullets covering scenario outcomes, PR comment upsert behavior, and any follow-up issue.

## Multi-check integration smoke sign-off protocol (issue #15)

Use this protocol for one realistic draft PR that triggers multiple workflows together and validates integration behavior.

### When to use this runbook

- Use when validating issue #15 integration behavior across multiple workflows on one PR.
- Use after changes to workflow triggers, marker-comment upsert behavior, or automation inputs that can alter check-set composition.

### Preconditions

- Run from a branch in this repository (not a fork) so PR comment upserts can write as expected.
- Use existing files only, do not create new markdown files in this smoke PR.
- Keep the PR as draft while testing.

### Deterministic file touch set

- Edit one existing markdown file, for example `reference/launch-and-automation-backlog.md`.
- Edit one existing automation/config file that still keeps checks green, for example `automation/messaging-impact-map.yml` or `_typos.toml`.
- Optional for broader coverage, include `.markdownlint.yaml` or `.lychee.toml`.

Expected checks for this scenario:

- `Terminology Check`
- `Impact Check`
- `Smart Suggestions`
- `Content Governance Checks`
- `Prose and links` (`Spelling (typos)`, `Markdown structure (markdownlint)`, `Links (lychee)`)

### Tier model

- Tier A (core smoke, required): verify trigger coverage, rerun stability, and comment idempotency.
- Tier B (extended diagnostics, conditional): run only when Tier A fails or behavior is unclear.

### Acceptance thresholds

- Trigger coverage: all expected checks appear for this deterministic PR shape.
- Comment idempotency: marker-managed comments update in place and do not duplicate after reruns.
- Runtime health: no outlier runtime beyond your team budget for routine PR checks.
- Guidance quality: at least one failing check (if induced) gives clear first-fix direction.
- Branch-protection parity: check names in PR runs match required checks in branch protection.

### Execution sequence

1. Open a draft PR with the baseline mixed change, then verify all expected checks appear.
2. Record exact check names and completion status.
3. Confirm each marker-managed PR comment is upserted in place (updated, not duplicated).
4. Push one small follow-up commit to force reruns, then confirm check-set stability and idempotency again.
5. If Tier A passes all thresholds, stop and sign off.
6. If any threshold fails, run Tier B:
  - Introduce one controlled lint or terminology failure.
  - Verify first-fix guidance is clear and actionable.
  - Revert the induced failure in the next commit.

### Failure classes (for fast follow-up issue creation)

- F1: Trigger mismatch (missing or unexpected workflows)
- F2: Comment idempotency defect (duplicate or stale marker comments)
- F3: Flaky or slow checks (unstable outcomes or runtime outliers)
- F4: Guidance UX gap (failure output does not explain next fix step)
- F5: Branch-protection mismatch (required checks differ from runtime names)

### Sign-off record for issue #15

- Post `@brianamarie Sign-off: PASS | FAIL - <one line>`.
- Include: `Tier run`, exact `Check set observed`, `Rerun delta`, `Comment idempotency`, `Protection parity`, and `Follow-ups`.
- Add 3 to 5 bullets for observations and follow-up issues for any confusing UX.

## AI-assisted automation development

AI is useful for proposing rules, test cases, and script refactors, but each change should be validated against expected false positives/false negatives before merge.

When requesting AI help for script changes, include:

- target workflow and script name
- the exact failure mode to catch
- allowed exceptions and boundary conditions
- expected output format (exit code, markdown report, JSON artifact, PR comment content)

## GitHub labels

Human-readable label names, colors, and descriptions live in `[.github/label-definitions.json](../.github/label-definitions.json)` (for example `**P0 - launch blocker`**, `**Automation & CI`**, not `area/automation`). After the remote repository exists, run `[apply_github_labels.sh](apply_github_labels.sh)` (requires `gh` and `jq`, and a logged-in `gh auth login` session) to create or update labels in place on GitHub.

## Prose, spelling, and links (not Python)

[Prose and links](../.github/workflows/prose-and-links.yml) uses marketplace actions; configuration lives in the repo root:

- **Spelling:** install `[typos](https://github.com/crate-ci/typos)` locally, or rely on CI; config `[_typos.toml](../_typos.toml)`.
- **External URLs:** `[lychee](https://github.com/lycheeverse/lychee)` with `[.lychee.toml](../.lychee.toml)`.
- **Markdown structure** (not product grammar): `[markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2)` with `[.markdownlint.yaml](../.markdownlint.yaml)` and `[.markdownlintignore](../.markdownlintignore)`.

Local markdownlint commands (same tool as CI):

- Check: `npx -y markdownlint-cli2@0.22.1 "**/*.md"`
- Autofix whitespace: `npx -y markdownlint-cli2@0.22.1 --fix "**/*.md"`

Issue #81 uses a dedicated hygiene-only config for safe PR auto-fixes:

- Config: `automation/markdown-hygiene-autofix.jsonc` (`MD009`, `MD012`, `MD047` only).
- Local check-only parity command: `npx -y markdownlint-cli2@0.22.1 --config automation/markdown-hygiene-autofix.jsonc "**/*.md"`.
- Local parity command: `npx -y markdownlint-cli2@0.22.1 --config automation/markdown-hygiene-autofix.jsonc --fix "**/*.md"`.
- Phase 1 (dry-run): set repository variable `MARKDOWN_HYGIENE_AUTO_PUSH_ENABLED=false` and run check mode plus fallback guidance only.
- Phase 2 (auto-push): set `MARKDOWN_HYGIENE_AUTO_PUSH_ENABLED=true` for non-fork PR branches.
- Promotion criteria: reruns stay idempotent (no extra bot commits or duplicate marker comments), and fixed diffs stay non-semantic.
- Rollback switch: disable `.github/workflows/markdown-hygiene-autofix.yml` if regressions appear.