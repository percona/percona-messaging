# Banned Terms and Terminology Corrections

This is the tool-agnostic reference for terms that must never appear in Percona messaging, plus corrections for commonly misused terminology. The same rules are encoded in `.cursor/rules/terminology-and-naming.mdc` for AI editor users.

## Banned terms

<!-- vale off -->

Never use in any Percona content:

- **Everest**: remove entirely, rewrite surrounding sentence
- **ProBuilds**, **Pro Builds**, and **Pro build** (any spacing, as a Percona delivery program or SKU label): remove entirely; use the canonical product name and public documentation for the capability
- **Pro** as a Percona product tier or suffix on database software (for example Percona Server for MySQL Pro, Percona Server for MongoDB Pro): remove; use the canonical product name only. No Pro tier exists on Percona database products

**Not banned:** third-party names such as Ubuntu 22.04 Pro, and **ExpertOps Proactive** Database Management.

## Deprecated terminology (replace on sight)

| Old term         | Current term                     | Notes                                                                                   |
| ---------------- | -------------------------------- | --------------------------------------------------------------------------------------- |
| Managed Services | Percona ExpertOps                | "Managed Services" acceptable only for historical context ("formerly Managed Services") |
| Percona Link     | Percona ClusterSync              | "Previously Percona Link" acceptable for historical context                             |
| GR ticket / GR   | Jira ticket / Jira design ticket | Always use Jira terminology                                                             |
| post-EOL support, Post-EOL Support, Percona EOL Support, Extended Life Support | **Extended Lifecycle Support (ELS)** | Program name for MySQL and MongoDB post-EOL coverage. EOL alone is deadline state, not the program SKU. |

## Formatting rules

- **"Open source"**: always two words, never hyphenated. Never write "open-source."
- **No em dashes**: use commas, periods, colons, or parentheses instead of — or --

## Licensing accuracy

- Only call software **open source** if it uses an OSI-approved license
- If not OSI-approved, call it **source available**
- Percona Server for MongoDB is **source available** (SSPL), never "open source"

<!-- vale on -->

## Automation (Vale)

[Vale](https://vale.sh/) rules under [`.vale/styles/Percona/`](../.vale/styles/Percona/) mirror this page for CI (see [`.github/workflows/terminology-check.yml`](../.github/workflows/terminology-check.yml)). When you change policy here, update the matching YAML rules. The `<!-- vale off -->` / `<!-- vale on -->` comments scope off the glossary so literal examples are not treated as violations.

Local check (from repo root): install the [Vale CLI](https://vale.sh/docs/install) and run `vale --minAlertLevel=error .` (blocking rules only) or `vale --minAlertLevel=warning .` to include warnings such as em dashes and Managed Services phrasing.
