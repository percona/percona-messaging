# Launch program, GitHub issues, and automation backlog

Use this file as the **source list** before creating issues on GitHub.  
**Labels** are defined in `[.github/label-definitions.json](../.github/label-definitions.json)`; apply with `[scripts/apply_github_labels.sh](../scripts/apply_github_labels.sh)`.

Ownership boundary for this document:

- Keep this file focused on backlog tracking, issue intake context, and prioritization.
- Keep operational execution protocols in [scripts/README.md](../scripts/README.md) under `Validation sign-off runbooks`.
- Use [AUTOMATION.md](../AUTOMATION.md) as the repository automation entry point and navigation hub.

**Priority IDs in this doc** (`P0`, `P1`, `P2`) map to GitHub labels `**P0 - launch blocker`**, `**P1 - important soon`**, and `**P2 - backlog**`, one label per issue is enough for priority.

## GitHub: opened issues (live)

Use this table to see what already exists on GitHub vs what is still only in the backlog sections below.

**Project board:** [Messaging go-live](https://github.com/orgs/percona/projects), one backlog for all messaging-program work. Differentiate launch vs non-launch using the custom field **Launch track** (`P0 Go-live`, `P1 Soon`, `P2 Later`, `Not launch`) plus saved views (**Launch** = filter to `P0 Go-live`; **All** = no filter). Execution still uses **Workflow stage** (`Todo`, `Next`, `In progress`, `Needs review`, `Done`). GitHub’s built-in **Status** field is optional.

Field setup guidance for `Launch track` is maintained in [AUTOMATION.md](../AUTOMATION.md) under `Operational setup references`.


| #   | Title                                                                                          | URL                                                                                                              |
| --- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| 1   | Implement launch hygiene automation (labels, project membership, workflow stage, stale triage) | [https://github.com/percona/percona-messaging/issues/1](https://github.com/percona/percona-messaging/issues/1)   |
| 2   | Concept: legal-sensitive and competitive language go-live review                               | [https://github.com/percona/percona-messaging/issues/2](https://github.com/percona/percona-messaging/issues/2)   |
| 3   | PO: confirm and update CODEOWNERS handles                                                      | [https://github.com/percona/percona-messaging/issues/3](https://github.com/percona/percona-messaging/issues/3)   |
| 4   | Set branch protection for main (approval + status checks + restricted push)                    | [https://github.com/percona/percona-messaging/issues/4](https://github.com/percona/percona-messaging/issues/4)   |
| 5   | Future: notify stakeholders when canonical messaging changes (Slack/email)                     | [https://github.com/percona/percona-messaging/issues/5](https://github.com/percona/percona-messaging/issues/5)   |
| 6   | Validate: terminology and banned terms check (terminology-check.yml)                           | [https://github.com/percona/percona-messaging/issues/6](https://github.com/percona/percona-messaging/issues/6)   |
| 7   | Validate: impact check (impact-check.yml + impact_check.py)                                    | [https://github.com/percona/percona-messaging/issues/7](https://github.com/percona/percona-messaging/issues/7)   |
| 8   | Validate: smart suggestions (smart-suggestions.yml + suggest_updates.py)                       | [https://github.com/percona/percona-messaging/issues/8](https://github.com/percona/percona-messaging/issues/8)   |
| 9   | Validate: new file gate (content-governance-checks + new_file_gate.py)                         | [https://github.com/percona/percona-messaging/issues/9](https://github.com/percona/percona-messaging/issues/9)   |
| 10  | Validate: doc coverage / navigation links (check_doc_coverage.py)                              | [https://github.com/percona/percona-messaging/issues/10](https://github.com/percona/percona-messaging/issues/10) |
| 11  | ~~Validate: duplicate content detector (duplicate_detector.py)~~ **Removed:** check dropped as low signal ([issue #11](https://github.com/percona/percona-messaging/issues/11)) | [https://github.com/percona/percona-messaging/issues/11](https://github.com/percona/percona-messaging/issues/11) |
| 12  | Validate: staleness report workflow (staleness-report.yml + staleness_report.py)               | [https://github.com/percona/percona-messaging/issues/12](https://github.com/percona/percona-messaging/issues/12) |
| 13  | Validate: case study monitor workflow (case-study-monitor.yml + sync_case_studies.py)          | [https://github.com/percona/percona-messaging/issues/13](https://github.com/percona/percona-messaging/issues/13) |
| 14  | Validate: prose and links workflow (typos + markdownlint + lychee)                             | [https://github.com/percona/percona-messaging/issues/14](https://github.com/percona/percona-messaging/issues/14) |
| 15  | Validate: PR smoke, multiple workflows on one change                                           | [https://github.com/percona/percona-messaging/issues/15](https://github.com/percona/percona-messaging/issues/15) |
| 16  | Implement: reviewer SLA reminders for stalled PRs                                              | [https://github.com/percona/percona-messaging/issues/16](https://github.com/percona/percona-messaging/issues/16) |
| 17  | Implement: track smart-suggestion quality (precision / recall over time)                       | [https://github.com/percona/percona-messaging/issues/17](https://github.com/percona/percona-messaging/issues/17) |
| 18  | Implement: decomposition / propagation completeness check before merge                         | [https://github.com/percona/percona-messaging/issues/18](https://github.com/percona/percona-messaging/issues/18) |
| 19  | Define product → social announcement workflow (timing, owners, and automation ideas)           | [https://github.com/percona/percona-messaging/issues/19](https://github.com/percona/percona-messaging/issues/19) |
| 20  | Implement: canonical discoverability check (beyond new-file doc coverage)                      | [https://github.com/percona/percona-messaging/issues/20](https://github.com/percona/percona-messaging/issues/20) |
| 21  | Implement: fixture-based regression tests for automation scripts                               | [https://github.com/percona/percona-messaging/issues/21](https://github.com/percona/percona-messaging/issues/21) |


**Project board policy:** the board is **inclusive** (program + launch + later work can all live here). Set **Launch track** on every card so the **Launch** saved view stays honest. Align **Launch track** with issue labels when you triage (for example `P0 - launch blocker` → **P0 Go-live**; roadmap automation → **P2 Later** or **Not launch**). Issue **#13** may stay off the project by policy if you prefer; if it is on the board, set **Not launch** or **P2 Later** unless it truly blocks go-live.

## Intake prerequisites and references

Use these references when creating or triaging automation issues:

- Label source and apply script: [.github/label-definitions.json](../.github/label-definitions.json) and [scripts/apply_github_labels.sh](../scripts/apply_github_labels.sh).
- Project field conventions and views: see the policy notes in this file under `GitHub: opened issues (live)`.
- Project automation commands: [gh project manual](https://cli.github.com/manual/gh_project).
- Operational sign-off protocols: [scripts/README.md](../scripts/README.md) (`Validation sign-off runbooks`).
- Automation architecture and workflow map: [AUTOMATION.md](../AUTOMATION.md).

Operational steps for creating labels, configuring project automation, or running validation are intentionally documented in operational docs, not in this tracking backlog.

## Legend


| Tag         | Meaning                                                                 |
| ----------- | ----------------------------------------------------------------------- |
| **test**    | Capability exists in-repo; sign off that behavior matches expectations. |
| **build**   | Not implemented yet; track as work.                                     |
| **process** | Working session or operational task (not necessarily code).             |


---

## Automation implementation references

Use these implementation docs instead of adding execution detail here:

- Workflow architecture and trigger map: [AUTOMATION.md](../AUTOMATION.md)
- Script and runbook execution details: [scripts/README.md](../scripts/README.md)
- Workflow files and repository automation config: [.github/workflows/](../.github/workflows/)

---

## Implemented in repo: validate before go-live (**test**)


| ID  | Suggested issue title                                          | Notes                                                                                    |
| --- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| A1  | Validate: terminology / banned terms (`terminology-check.yml`) | Overlaps conceptually with **typos**; terminology = policy, typos = spelling.            |
| A2  | Validate: impact check                                         |                                                                                          |
| A3  | Validate: smart suggestions                                    |                                                                                          |
| A4  | Validate: new file gate                                        | See `scripts/README.md` (New file gate sign-off protocol for issue #9).                  |
| A5  | Validate: doc coverage                                         |                                                                                          |
| A6  | ~~Validate: duplicate detector~~ **Removed** (see issue #11)                                   |                                                                                          |
| A7  | Validate: staleness report                                     |                                                                                          |
| A8  | Validate: case study monitor                                   | Needs `CASE_STUDY_FEED_URL` repo variable when used.                                     |
| A9  | Optional: multi-check integration smoke (one PR)               | See `scripts/README.md` (Multi-check integration smoke sign-off protocol for issue #15). |
| A10 | Validate: spelling (`typos` / `_typos.toml`)                   | Use operational docs for tool configuration details.                                     |
| A11 | Validate: markdown structure (`markdownlint-cli2`)             | Not grammar; tuned for this corpus (see `.markdownlint.yaml`).                           |
| A12 | Validate: external links (`lychee` / `.lychee.toml`)           | Use operational docs for tool configuration details.                                     |


---

## Not in CI yet: track as issues (**build** or **process**)


| ID  | Suggested issue title                                                                           | Type    | Notes                                                             |
| --- | ----------------------------------------------------------------------------------------------- | ------- | ----------------------------------------------------------------- |
| G1  | Define and apply GitHub label taxonomy                                                          | process | See [scripts/README.md](../scripts/README.md) `GitHub labels`.    |
| G2  | Pre–go-live project board (columns + criteria)                                                  | process |                                                                   |
| D1  | Deeper **style / grammar** (Vale `write-good`/Microsoft, or LanguageTool, or editorial process) | build   | **Not** covered by markdownlint; pair with brand voice reviewers. |
| D2  | PR comment automation: replace ad-hoc `github-script` with find/create-or-update actions        | build   | Optional cleanup.                                                 |


### Near-term automation (from `AUTOMATION.md` / `OPEN-SOURCE-MESSAGING-PLAYBOOK.md`): **build**


| ID  | Title (short)                                                                                                                                             |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N1  | **SKIP (for now):** Launch-readiness label consistency (`ready-for-launch`, `go-live:`*), not needed until PR labels are an agreed GTM/release convention |
| N3  | Reviewer SLA reminders, [opened as #16](https://github.com/percona/percona-messaging/issues/16)                                                           |
| N4  | Suggestion precision / recall metrics, [opened as #17](https://github.com/percona/percona-messaging/issues/17) (**P2 / Roadmap: later** on issue)         |
| N5  | Decomposition-completeness assistant, [opened as #18](https://github.com/percona/percona-messaging/issues/18) (**P2 / Roadmap: later** on issue)          |


### Next wave: **build**


| ID  | Title (short)                                                                                                                                                                         |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| W1  | Canonical link / discoverability beyond new files, [opened as #20](https://github.com/percona/percona-messaging/issues/20) (**P2 / Roadmap: later** on issue)                         |
| W2  | Fixture-based regression tests for `scripts/`, [opened as #21](https://github.com/percona/percona-messaging/issues/21) (**P2 / Roadmap: later** on issue)                             |
| W3  | **SKIP (for now):** Rule drift report (terminology docs vs checks), over-engineered for current phase                                                                                 |
| W4  | Auto-triage labels for issues                                                                                                                                                         |
| W5  | PR change-risk / suggested reviewers                                                                                                                                                  |
| W6  | Suggestion quality feedback loop                                                                                                                                                      |
| W7  | Cross-repo adaptation watcher (report-only)                                                                                                                                           |
| W8  | Post-merge missed-propagation sampler                                                                                                                                                 |
| W9  | **Downstream execution assets:** registry + check/notify for decks, webpages, datasheets, enablement, etc., when canonical messaging changes (see *Future wish* below; pairs with W7) |


### Future wish (north star, not v1)

**Downstream impact automation:** when canonical messaging in this repository changes, you want a durable loop that: (1) records which **downstream** materials exist and depend on it (e.g. slide decks, website pages, PDF datasheets, sales enablement, partner pages), (2) **detects** relevant merges or diffs and **notifies** the right people or systems that those assets may be stale, and (3) stays **report-first**, with no automatic writes to CMS, Slides, or file shares until product and security agree. This is the execution-side complement to in-repo [propagation](decomposition-and-propagation.md); it extends the same “don’t miss surfaces” problem beyond markdown.

### Stakeholder / content (non-automation): **process** or **build**


| ID  | Title                                             | Who to involve (typical)   |
| --- | ------------------------------------------------- | -------------------------- |
| P1  | Walkthrough: Cursor rules vs public governance    | Cindy, Kim; Legal optional |
| P2  | Walkthrough: terminology & naming source of truth | Cindy, Legal, PMs          |
| P3  | Walkthrough: smart suggestions & impact map       | Cindy, PMs                 |
| C1  | Pre-publish scrub: internal names / markers       | Legal, PM per file         |
| C2  | Pre-publish: competitive / third-party lines      | Legal (e.g. Jaimie), PMs   |
| C3  | Audit: customer names vs published case studies   | Marketing, PM              |
| C4  | Resolve accuracy flags in copy                    | Owning PM, Legal if needed |
| C5  | CODEOWNERS real handles + Kate                    | Kate, admin                |
| C6  | Branch protection + required checks               | Admin                      |
| C7  | Read site: Docsify vs MkDocs                      | PMs, you                   |
| C8  | Build with AI competition admin                   | You, program owner         |


---

## Suggested default labels (when opening on GitHub)


| Backlog row              | Suggested labels                                                                                                                                                                        |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| All **A** (validation)   | `Testing / sign-off` · `Automation & CI` · `Launch program` · `P0 - launch blocker` (use `P1 - important soon` for A9 if you treat it as optional).                                     |
| **N** (near-term builds) | `Feature / build` · `Automation & CI` · `Roadmap: soon` · `Launch program` or `**P1 - important soon`** (pick one priority label).                                                      |
| **W** (next wave)        | `Feature / build` · `Automation & CI` · `Roadmap: later` · `**P2 - backlog`**.                                                                                                          |
| **C** (content)          | `Content & messaging` or `Governance & policy` · `Go-live & repo setup` if repo-only · `Needs: legal review` / `Needs: product or GTM` as needed · `Launch program` · priority as fits. |
| **P** (walkthroughs)     | `Work session` · `Governance & policy` or `Automation & CI` · `Launch program` · `Needs: …` as needed.                                                                                  |
| **G** (program ops)      | `Go-live & repo setup` · `Work session` (G2) · `**P0 - launch blocker`** for G1 if it gates everything else.                                                                            |
| **D** (tooling cleanup)  | `Feature / build` or `Automation & CI` · `**P2 - backlog`** unless it blocks you.                                                                                                       |


---

## Product-driven implementation ideas (for N/W backlog)

- When offerings or positioning change, treat `messaging-impact-map.yml` and `claim-types.yml` as versioned alongside product (same release train).
- If you later adopt PR launch labels for GTM, add a small consistency check then (N1 was deferred).
- Case study + staleness automation supports **proof-point** updates when marketing changes claims.
- Decomposition assistant (N5) reduces **missed downstream** when pillar or product pages move.
- **W9** (downstream-asset registry + notifications) closes the loop when messaging ships but **GTM and web** own slides and pages outside the repo.

This document is the tracking source before you bulk-create issues. Keep it in sync as scopes change.