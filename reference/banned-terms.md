# Banned Terms and Terminology Corrections

This is the tool-agnostic reference for terms that must never appear in Percona messaging, plus corrections for commonly misused terminology. The same rules are encoded in `.cursor/rules/terminology-and-naming.mdc` for AI editor users.

## Banned terms

Never use in any Percona content:
- **Everest**: remove entirely, rewrite surrounding sentence
- **ProBuilds**: remove entirely, rewrite surrounding sentence

## Deprecated terminology (replace on sight)

| Old term | Current term | Notes |
| --- | --- | --- |
| Managed Services | Percona ExpertOps | "Managed Services" acceptable only for historical context ("formerly Managed Services") |
| Percona Link | Percona ClusterSync | "Previously Percona Link" acceptable for historical context |
| GR ticket / GR | Jira ticket / Jira design ticket | Always use Jira terminology |

## Formatting rules

- **"Open source"**: always two words, never hyphenated. Never write "open-source."
- **No em dashes**: use commas, periods, colons, or parentheses instead of — or --

## Licensing accuracy

- Only call software **open source** if it uses an OSI-approved license
- If not OSI-approved, call it **source available**
- Percona Server for MongoDB is **source available** (SSPL), never "open source"
