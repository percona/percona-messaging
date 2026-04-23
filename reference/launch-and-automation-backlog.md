# Launch program, GitHub issues, and automation backlog

Use this file as the **source list** before creating issues on GitHub.  
**Labels** are defined in [`.github/label-definitions.json`](../.github/label-definitions.json); apply with [`scripts/apply_github_labels.sh`](../scripts/apply_github_labels.sh).

**Priority IDs in this doc** (`P0`, `P1`, `P2`) map to GitHub labels **`P0 - launch blocker`**, **`P1 - important soon`**, and **`P2 - backlog`** — one label per issue is enough for priority.

## Bootstrap: push, labels, project, then issues

Do this **before** bulk-creating issues so labels exist and the **Project** (board) is ready. Labels and projects do **not** depend on each other, but the **order** below avoids empty boards and re-clicking.

1. **Push** this branch to `origin` so the latest [`.github/label-definitions.json`](../.github/label-definitions.json) and docs are on GitHub.
2. **Create labels** on the remote (idempotent: safe to re-run):
   - Install [GitHub CLI](https://cli.github.com/) and log in: `gh auth login`
   - For project features later: `gh auth refresh -h github.com -s project` (or ensure your token can manage Projects).
   - From repo root: `./scripts/apply_github_labels.sh` (needs `gh` and `jq`).
3. **Create the project** (org or repo **Projects** tab, or `gh project create` — see [gh project](https://cli.github.com/manual/gh_project)). Name it something stable, e.g. *Messaging go-live*, and add columns that match your flow (e.g. **Todo / Next / In progress / Done**).
4. **Auto-add** (pick one; optional but nice):
   - In **Project** settings, use a **workflow** / rule to add new issues that match a filter (e.g. have **`Launch program`** or are in this repo), *or*
   - When creating issues: `gh issue create ... --project "Project name"` (requires `project` scope; same refresh as above), *or*
   - After the fact: `gh project item-add` with the issue URL.
5. **Open issues** one by one (or scripted); they should get labels from step 2 and the project from step 4.

Run steps 2–4 on a machine with **`gh`**, **`jq`**, and permission to change labels/projects for this repository (or use the GitHub web UI for labels and Projects). **Current remote in this clone:** `https://github.com/percona/percona-messaging.git` (edit this line if the canonical URL changes).

## Legend

| Tag        | Meaning                                                                 |
| ---------- | ----------------------------------------------------------------------- |
| **test**   | Capability exists in-repo; sign off that behavior matches expectations. |
| **build**  | Not implemented yet; track as work.                                    |
| **process** | Working session or operational task (not necessarily code).           |

---

## GitHub Actions inventory (third-party vs custom)

All workflows use **`actions/checkout@v4`** (official). Below: what is **pre-made** vs **repository-owned**.

| Workflow | Marketplace / pre-built | Custom (this repo) | Could swap for more pre-built later |
| -------- | ------------------------ | -------------------- | ------------------------------------- |
| `terminology-check.yml` | `actions/checkout` only | Inline `grep` / shell for policy terms | Could move some patterns into **`typos`** `_typos.toml` (`[default.extend-words]` corrections) or a small **cspell** config; policy rules are still yours. |
| `impact-check.yml` | `actions/checkout`, `actions/setup-python`, `actions/github-script` | `scripts/impact_check.py` | Comment upsert could use **sticky PR comment** actions; map logic stays custom. |
| `smart-suggestions.yml` | checkout, setup-python, **github-script** | `scripts/suggest_updates.py` | Same as above for comments. |
| `content-governance-checks.yml` | checkout, **github-script** | `new_file_gate.py`, `check_doc_coverage.py`, `duplicate_detector.py` | Gate/coverage/duplicate logic is inherently repo-specific. |
| `staleness-report.yml` | checkout, **upload-artifact**, **github-script** | `scripts/staleness_report.py` | Issue upsert could use a dedicated **create-or-update-issue** action; report body stays custom. |
| `case-study-monitor.yml` | checkout, setup-python, **peter-evans/create-pull-request** | `sync_case_studies.py`, `suggest_updates.py` | PR creation is already a standard action; sync script is custom. |
| `prose-and-links.yml` | **crate-ci/typos**, **DavidAnson/markdownlint-cli2-action**, **lycheeverse/lychee-action** | Config only: `_typos.toml`, `.lychee.toml`, `.markdownlint.yaml`, `.markdownlintignore` | Fully pre-built runners; you only maintain config. |

**`actions/github-script`:** maintained by GitHub; your **inline JavaScript** is custom. Alternatives: **`peter-evans/find-comment` + `create-or-update-comment`**, or **marocchino/sticky-pull-request-comment**, if you want less JS in YAML.

---

## Implemented in repo — validate before go-live (**test**)

| ID  | Suggested issue title | Notes |
| --- | --------------------- | ----- |
| A1  | Validate: terminology / banned terms (`terminology-check.yml`) | Overlaps conceptually with **typos**; terminology = policy, typos = spelling. |
| A2  | Validate: impact check | |
| A3  | Validate: smart suggestions | |
| A4  | Validate: new file gate | |
| A5  | Validate: doc coverage | |
| A6  | Validate: duplicate detector | |
| A7  | Validate: staleness report | |
| A8  | Validate: case study monitor | Needs `CASE_STUDY_FEED_URL` repo variable when used. |
| A9  | Optional: multi-check integration smoke (one PR) | |
| A10 | Validate: spelling (`typos` / `_typos.toml`) | Add words to `[default.extend-identifiers]` as you hit false positives. |
| A11 | Validate: markdown structure (`markdownlint-cli2`) | Not grammar; tuned for this corpus (see `.markdownlint.yaml`). |
| A12 | Validate: external links (`lychee` / `.lychee.toml`) | Tune `exclude` if a host is flaky in CI. |

---

## Not in CI yet — track as issues (**build** or **process**)

| ID  | Suggested issue title | Type | Notes |
| --- | --------------------- | ---- | ----- |
| G1  | Define and apply GitHub label taxonomy | process | Run `scripts/apply_github_labels.sh` after repo exists. |
| G2  | Pre–go-live project board (columns + criteria) | process | |
| D1  | Deeper **style / grammar** (Vale `write-good`/Microsoft, or LanguageTool, or editorial process) | build | **Not** covered by markdownlint; pair with brand voice reviewers. |
| D2  | PR comment automation: replace ad-hoc `github-script` with find/create-or-update actions | build | Optional cleanup. |

### Near-term automation (from `AUTOMATION.md` / `IMPLEMENTATION.md`) — **build**

| ID  | Title (short) |
| --- | ------------- |
| N1  | Launch-readiness label consistency (`ready-for-launch`, `go-live:*`) |
| N2  | CODEOWNERS coverage / drift check |
| N3  | Reviewer SLA reminders |
| N4  | Suggestion precision / recall metrics |
| N5  | Decomposition-completeness assistant |

### Next wave — **build**

| ID  | Title (short) |
| --- | ------------- |
| W1  | Canonical link / discoverability beyond new files |
| W2  | Fixture-based regression tests for `scripts/` |
| W3  | Rule drift report (terminology docs vs checks) |
| W4  | Auto-triage labels for issues |
| W5  | PR change-risk / suggested reviewers |
| W6  | Suggestion quality feedback loop |
| W7  | Cross-repo adaptation watcher (report-only) |
| W8  | Post-merge missed-propagation sampler |
| W9  | **Downstream execution assets:** registry + check/notify for decks, webpages, datasheets, enablement, etc., when canonical messaging changes (see *Future wish* below; pairs with W7) |

### Future wish (north star, not v1)

**Downstream impact automation:** when canonical messaging in this repository changes, you want a durable loop that: (1) records which **downstream** materials exist and depend on it (e.g. slide decks, website pages, PDF datasheets, sales enablement, partner pages), (2) **detects** relevant merges or diffs and **notifies** the right people or systems that those assets may be stale, and (3) stays **report-first**—no automatic writes to CMS, Slides, or file shares until product and security agree. This is the execution-side complement to in-repo [propagation](decomposition-and-propagation.md); it extends the same “don’t miss surfaces” problem beyond markdown.

### Stakeholder / content (non-automation) — **process** or **build**

| ID  | Title | Who to involve (typical) |
| --- | ----- | ------------------------- |
| P1  | Walkthrough: Cursor rules vs public governance | Cindy, Kim; Legal optional |
| P2  | Walkthrough: terminology & naming source of truth | Cindy, Legal, PMs |
| P3  | Walkthrough: smart suggestions & impact map | Cindy, PMs |
| C1  | Pre-publish scrub: internal names / markers | Legal, PM per file |
| C2  | Pre-publish: competitive / third-party lines | Legal (e.g. Jaimie), PMs |
| C3  | Audit: customer names vs published case studies | Marketing, PM |
| C4  | Resolve accuracy flags in copy | Owning PM, Legal if needed |
| C5  | CODEOWNERS real handles + Kate | Kate, admin |
| C6  | Branch protection + required checks | Admin |
| C7  | Read site: Docsify vs MkDocs | PMs, you |
| C8  | Build with AI competition admin | You, program owner |

---

## Suggested default labels (when opening on GitHub)

| Backlog row | Suggested labels |
| ----------- | ---------------- |
| All **A\*** (validation) | `Testing / sign-off` · `Automation & CI` · `Launch program` · **`P0 - launch blocker`** (use **`P1 - important soon`** for A9 if you treat it as optional). |
| **N\*** (near-term builds) | `Feature / build` · `Automation & CI` · `Roadmap: soon` · `Launch program` or **`P1 - important soon`** (pick one priority label). |
| **W\*** (next wave) | `Feature / build` · `Automation & CI` · `Roadmap: later` · **`P2 - backlog`**. |
| **C\*** (content) | `Content & messaging` or `Governance & policy` · `Go-live & repo setup` if repo-only · `Needs: legal review` / `Needs: product or GTM` as needed · `Launch program` · priority as fits. |
| **P\*** (walkthroughs) | `Work session` · `Governance & policy` or `Automation & CI` · `Launch program` · `Needs: …` as needed. |
| **G\*** (program ops) | `Go-live & repo setup` · `Work session` (G2) · **`P0 - launch blocker`** for G1 if it gates everything else. |
| **D\*** (tooling cleanup) | `Feature / build` or `Automation & CI` · **`P2 - backlog`** unless it blocks you. |

---

## Product-driven implementation ideas (for N/W backlog)

- When offerings or positioning change, treat **`messaging-impact-map.yml`** and **`claim-types.yml`** as versioned alongside product (same release train).
- Launch labels + checks (N1) align repo state with **GTM / PM** “ready to ship” language.
- Case study + staleness automation supports **proof-point** updates when marketing changes claims.
- Decomposition assistant (N5) reduces **missed downstream** when pillar or product pages move.
- **W9** (downstream-asset registry + notifications) closes the loop when messaging ships but **GTM and web** own slides and pages outside the repo.

This document is the checklist **before** you bulk-create issues; keep it in sync as scopes change.
