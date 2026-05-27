# Percona Messaging

Percona is an open source company, and we apply open source practices to our messaging as well.

Percona Messaging is the canonical source for reusable messaging, naming guidance, and contribution workflows. It applies the same collaborative principles we use in open source development: versioned content, visible review, and reusable source material across frameworks, offerings, products, and customer narratives.

## Why this repository exists

Messaging becomes inconsistent when source material is scattered, ownership is unclear, and review happens in too many places. This repository applies open source ways of working to messaging with durable files, visible review, explicit ownership, and a clear history of what changed and why.

It keeps durable messaging in tracked markdown so contributors can find the current source, propose changes through pull requests, and understand how decisions are made.

## What this repository is

- A canonical source for framework messaging, product messaging, offering messaging, and reference guidance
- A contribution and governance system for reviewing and approving messaging changes
- Reusable source material that can be adapted into pages, decks, and enablement

## What this repository is not

- A roadmap
- A replacement for subject-matter review, legal review, or launch controls
- A catch-all archive for every downstream deliverable

## Who this repository is for

- Contributors creating or updating messaging
- Domain owners reviewing for accuracy and alignment
- Teams adapting approved messaging into other formats
- Field, marketing, and partners who need readable approved copy without browsing the GitHub file tree

## Reader site (GitHub Pages)

Approved messaging is also available as a browsable site (Docsify on GitHub Pages), built directly from the markdown in this repository.

- **URL (after merge and Pages setup):** [https://percona.github.io/percona-messaging/](https://percona.github.io/percona-messaging/)
- **Setup:** repository Settings → Pages → deploy from `main`, folder `/ (root)`. See [site/README.md](site/README.md).
- **Not search-indexed:** share the link directly; it is not intended for organic search.
- **Changes:** edit markdown here as usual; merging to `main` updates the site.

## Repository map

- `framework/`: company-level positioning, category framing, and "why Percona" narrative
- `use-cases-value-pillars/`: shared value-pillar messaging (cost, performance, security/compliance, future readiness) and cross-product scenarios
- `offerings/`: core services messaging, including Expert Support, Expert Consulting, and managed services (`ExpertOps`)
- `offerings/solution-bundles/`: fixed-scope sold packages that combine services and outcomes
- `products/`: product and database-specific messaging (MySQL, PostgreSQL, MongoDB, Valkey/Redis, PMM, Operators) plus competitive-safe overlays
- `reference/`: canonical naming, banned terms, brand voice, governance references, and decomposition guidance
- `docs/`: portable agent baseline shared across editors and tools (see [docs/agent-guidelines.md](docs/agent-guidelines.md))
- `.cursor/rules/`: Cursor-facing snippets aligned with that baseline
- `automation/`: impact maps and claim categories for CI checks
- `data/`: machine-readable registries used by automation
- `scripts/`: CI and local automation entry points

## How to use this repository

1. Start with `framework/` for the highest-level narrative and reusable positioning.
2. Use `offerings/` and `products/` for domain-specific source material.
3. Use `use-cases-value-pillars/` for value pillars and broader scenario/value-prop messaging.
4. Use `offerings/solution-bundles/` for sold packaged offers.
5. Check `reference/` and `.cursor/rules/` for naming, terminology, style guidance, and decomposition policy.
6. Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes.
7. Read [GOVERNANCE.md](GOVERNANCE.md) when a change affects ownership, approval, or canonical status.
8. Use [reference/decomposition-and-propagation.md](reference/decomposition-and-propagation.md) for the decomposition workflow and propagation checklist.
9. Use [OPEN-SOURCE-MESSAGING-PLAYBOOK.md](OPEN-SOURCE-MESSAGING-PLAYBOOK.md) and [ORIGIN.md](ORIGIN.md) for the operating model and adoption program behind this repository.

## Working with AI assistants

**Claude Code** loads **[CLAUDE.md](CLAUDE.md)** (pointer into AGENTS + baseline). Everyone else should still start from **[AGENTS.md](AGENTS.md)** and **[docs/agent-guidelines.md](docs/agent-guidelines.md)** for portable git boundaries and how messaging rules scope across directories. Cursor loads extra structured snippets from **`.cursor/rules/`**, which must stay aligned with that baseline.

Contributor-facing naming and voice references also live under **`reference/`**.

Marketing teams may use separate internal writing instructions and prompts in tools like Claude. This repository remains the foundational messaging source those workflows should build from.

## Working in the open

Default to working in the open through issues, branches, and pull requests, including planned updates ahead of launch, so changes can be reviewed and propagated early.

For launch-timed content, stage in a draft pull request (or release-prep branch) and merge to `main` at go-live so canonical status stays clear.

Keep content private only when it includes sensitive material, such as:

- Customer-specific confidential information
- Private internal business or legal details
- Competitive intelligence and internal talk tracks
- Other restricted information that should not be public

## Playbook and governance

- `OPEN-SOURCE-MESSAGING-PLAYBOOK.md`: operating order, program delivery and workstreams, stakeholder comms, goals, and control loop
- `reference/content-governance.md`: decomposition, anti-duplication, and private competitive policy
- `reference/decomposition-and-propagation.md`: step-by-step decomposition and propagation workflow
- `AUTOMATION.md`: end-to-end automation map across workflows, scripts, and config
- `CODE_OF_CONDUCT.md`: community standards, reporting, and enforcement expectations

## License

This work is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). See [NOTICES.md](NOTICES.md) for third-party trademark attributions.
