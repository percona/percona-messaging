# Instructions for coding agents

Read the portable baseline first: **[docs/agent-guidelines.md](docs/agent-guidelines.md)** (git boundaries, how repo-wide rules differ from canonical messaging-only rules, and pointers into contributor docs).

**Cursor** loads extra snippets from **`.cursor/rules/`**. Those files must stay aligned with the baseline and must not contradict it on commit/push/merge/PR policy or on which directories carry canonical messaging guardrails.

For role-aware execution support (call prep, persona-targeted email, campaign variants), use `data/personas-inventory.json` as the persona source and follow `.cursor/rules/persona-routing.mdc` for routing behavior.
