# Governance

This document defines how Percona Messaging stays trustworthy: messaging is current, traceable, and reviewable because canonical content is maintained in tracked markdown with clear ownership and decision rights.

## What "trustworthy" means here

- **Current:** canonical messaging reflects the latest approved position.
- **Traceable:** every canonical change has issue and pull-request history.
- **Reviewable:** owners and maintainers are explicit, and approval paths scale with risk.

## Canonical status (source of truth)

- `main` contains approved canonical messaging.
- Open pull requests may contain proposed future changes, but they are not canonical until merged.
- Issues and drafts can support thinking and planning, but they are never the source of truth.

## Governance principles

- **Single canonical source:** approved messaging lives in tracked repository markdown, not in decks, chat threads, private notes, or ad hoc Notion pages.
- **Clear boundary for private material:** confidential or sensitive material stays outside this public repository, but requests that start privately should still be captured as tracked issues with source context.
- **Shared operating model:** domain owners and repository maintainers co-own review of material changes, with specialist reviewers added for legal, launch-sensitive, brand, or other high-risk topics.
- **Reusable-first change model:** decompose and propagate updates through existing canonical modules before creating new one-off pages.

## Roles and decision rights

- **Repository maintainers (Solutions Marketing):** steward structure, workflow, templates, and final merged wording quality. Current maintainers: Briana Swift, Val Bogatyreva.
- **Domain owners:** accountable for messaging accuracy in their product, offering, or subject area (typically product owners, product managers, or business unit leaders).
- **Contributors:** can include maintainers, domain owners, and other collaborators; they propose changes, explain rationale, and identify downstream impact.
- **Reviewers:** typically maintainers, domain owners, and relevant technical leads; they validate accuracy, terminology, and cross-file consistency.
- **Specialist reviewers:** provide legal, launch-sensitive, brand, or other risk-specific input when needed.

Percona Messaging uses RAPID to keep decision rights explicit.

| Decision type                                       | Recommend                              | Agree / Input                                | Perform                      | Decide                                         |
| --------------------------------------------------- | -------------------------------------- | -------------------------------------------- | ---------------------------- | ---------------------------------------------- |
| Repository structure and workflow                   | Repository maintainers                 | Domain owners and affected reviewers         | Repository maintainers       | Repository lead                                |
| Framework messaging and naming rules                | Repository maintainers                 | Domain owners and specialist reviewers       | Contributors and maintainers | Messaging governance lead                      |
| Product or offering messaging updates               | Domain owner or designated contributor | Repository maintainer and affected reviewers | Contributor                  | Domain owner                                   |
| High-risk public claims or launch-sensitive changes | Domain owner or repository maintainer  | Specialist reviewers                         | Contributor and maintainer   | Designated approver for the affected risk area |

## Ownership map and CODEOWNERS

`CODEOWNERS` is the source of truth for reviewer auto-assignment and path ownership. Use `[CODEOWNERS](CODEOWNERS)` as the base ownership map and keep it aligned with the roles above.

## Review and approval operating model

For day-to-day workflow details, use [CONTRIBUTING.md](CONTRIBUTING.md).

- **Start path:** preferred is domain owner pull request; minimum is a tracked issue that maintainers can route through standard workflow and automation.
- **Risk path:** explicit approval is required for `framework/` changes, naming/terminology changes, broad multi-page claims, governance/rules changes, launch-sensitive content, and new canonical markdown files.
- **Low-risk path:** typo/link/format fixes and low-risk clarifications can use lightweight review, but still land through the normal issue + pull request flow.

## GitHub pre-launch staging workflow

Use this pattern when content must be reviewed before launch but should not be canonical yet:

- **Stage in draft PR:** keep launch-ready content in a draft pull request (or release-prep branch) until go-live.
- **Signal readiness clearly:** use labels and optional milestones (for example `ready-for-launch`, `go-live:YYYY-MM-DD`) so status is visible without merging.
- **Merge at go-live:** keep `main` as canonical by merging only when content is live-ready; branch protection and required reviews remain enforced on `main`.

## Participation and code of conduct

- We follow [Contributor Covenant](https://www.contributor-covenant.org/) standards in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
- This policy aligns with GitHub's recommended repository-community practices, including clear standards and enforcement pathways.
- We welcome employee and external contributions, especially improvements, corrections, and real-world usage stories from users.
- This repository is not the roadmap intake system. If roadmap requests or product questions are submitted here, maintainers triage and route them to the right internal team.
- Reports about conduct concerns should be made privately to repository maintainers. Maintainers review promptly, act proportionally (for example warning, content removal, or access restriction), and escalate to appropriate internal leadership channels when required.
