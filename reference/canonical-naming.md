# Canonical Naming References

**Values**

| Core value            | Full pillar label                  | Common shorthand | How to use                                                                                                                                        |
| --------------------- | ---------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Open source           | **Open Source Commitment**         | Open source      | Use this phrasing for the pillar label. In body copy, feel free to reference open source, source-available, licensing, or transparency as needed. |
| Freedom / portability | **Vendor Freedom to Run Anywhere** | Vendor freedom   | Use the full label in headings or diagrams. In narrative text, "run anywhere," "multi-cloud," or "platform freedom" are fine.                     |
| Expertise             | **Expertise on Call**              | Expertise        | Use as the pillar name. In explanations, you can say "upstream-level engineers," "experts on call," or similar.                                   |

**Offerings**

| Type             | Full name                                   | Acceptable short form                                            | Guidance                                                                                                                                                                                                                                                                                   |
| ---------------- | ------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Commercial offer | **Percona Expert Support**                  | Expert Support, Percona Support, Support                         | Use the full name on first mention in a section; shorthand is fine afterward. Use "support" only when context is clear, with no ambiguity between general, community, or other non-commercial help.                                                                                        |
| Commercial offer | **Percona ExpertOps**                       | Percona ExpertOps, ExpertOps, Proactive Database Management      | Primary name for proactive, hands-on operations. It is OK to reference "managed services" once for historical context if helpful, but the name was changed away from "managed services" because it is often used to describe SaaS offerings, and is used in that way in the messaging doc. |
| Commercial offer | **Percona Expert Consulting and Services**  | Consulting and Services, Percona Consulting, or Percona Services | Use when referring to project-based or specialized engagements; shorthand is acceptable after first mention.                                                                                                                                                                               |
| Product          | **Percona Monitoring and Management (PMM)** | PMM                                                              | Treat as a product or capability used across offerings rather than part of an offer name.                                                                                                                                                                                                  |
| Lifecycle model  | **Run / Operate / Observe**                 | None                                                             | **Internal only.** Used to describe the software lifecycle framing.                                                                                                                                                                                                                        |
| Support tiers    | **Advanced Support**, **Premium Support**   | None                                                             | Keep "Support" attached for clarity when referencing SLAs or response times.                                                                                                                                                                                                               |

## Extended Lifecycle Support program naming (ELS)

Percona's paid program for continuity after a database version reaches End of Life (EOL) is **Extended Lifecycle Support (ELS)**. Use this name for MySQL and MongoDB in customer-facing copy. For **MariaDB Server**, use ELS only where Percona publishes coverage; keep MariaDB Server-only scope, and never imply Percona ships MariaDB database software. Retain **End of Life (EOL)** only for deadline state (community or vendor EOL dates), not as a program label.

| Context | Use this | Not this |
| --- | --- | --- |
| Percona post-EOL program (MySQL, MongoDB; MariaDB Server where published) | **Extended Lifecycle Support (ELS)** | Extended Life Support, post-EOL support, Post-EOL Support, Percona EOL Support |
| Third-party vendor extended support | vendor extended support, RDS extended support | (Do not relabel as Percona ELS) |
| EOL as a date or state | End of Life (EOL), community EOL, reached end of life | EOL Support (as a program SKU) |

Live web paths and legacy PDFs may still say post-EOL support until commercial assets are updated. Canonical messaging in this repo should use **Extended Lifecycle Support (ELS)** so future edits do not drift back to deprecated program names.

## MariaDB edition and entity naming

Percona does not ship MariaDB database software. Under standard **Expert Support** entitlements, coverage is **MariaDB Server** only: the open source edition maintained by the **MariaDB Foundation**, contrasted with **MariaDB Enterprise**. **Expert Consulting and Services** may apply to other MariaDB versions and complex environments.

| Context | Use this | Not this |
| --- | --- | --- |
| Open source edition covered by Expert Support | **MariaDB Server** | MariaDB Community (as the product edition name) |
| Commercial edition (outside standard Expert Support) | MariaDB Enterprise | Implying standard Support covers Enterprise |
| Short product lists where Server and Enterprise may both appear | MariaDB | Required when the line must stay edition-neutral (for example home product lists) |
| Upstream open source steward | MariaDB Foundation | |
| Commercial entity | MariaDB Corporation or MariaDB plc | |

Prefer **MariaDB Server** over bare "MariaDB" when the sentence means the supported open source database software. Keep the Foundation / Corporation (or plc) distinction when the steward or commercial entity matters.

**MaxScale:** MariaDB **MaxScale** is database proxy / routing middleware from MariaDB plc, typically under BSL terms for current commercial access. In sales and discovery copy, ask whether MaxScale is load-bearing in the estate. Do not imply MaxScale is included in standard MariaDB Server Expert Support, and do not claim Percona ships or forks MaxScale until product publishes that coverage. Complex MaxScale-heavy estates may need consulting scope.

## PACE and migration program naming

- **Capability:** Database modernization and migration
- **Program:** PACE (Percona Assisted Cutover Engine)
- **Partner:** HexaCluster (migration software and services; customers contract with Percona)

Full copy blocks: [migration-program/messaging.md](../offerings/migration-program/messaging.md).

## Community program naming

These are community participation programs, not commercial offerings. Keep them distinct from Expert Support, ExpertOps, and Consulting. Positioning lives under Deep Ecosystem participation in [why-percona.md](../framework/why-percona.md).

| Name | Use for | Notes |
| --- | --- | --- |
| **Percona Community** | The overall community home and programs | Public hub: [percona.community](https://percona.community/) |
| **Basecamp** | The entry point on the community climb | Starting rung; not a product or SKU |
| **Community Ascent** | The contribution climb and public dashboards | Program home: [percona.community/ascent](https://percona.community/ascent/) |
| **Mountaineers** | Recognition and rewards for top contributors | Code, forum help, content, and direct product feedback |
| **Community Writers Program** | Paid community-authored technical posts | Publish on the community blog under the author’s name |
| **Percona Community Slack** | Peer conversation space | Complements forums; does not replace them for support |
| **Percona Live** | Flagship Percona conference | Event details on [perconalive.com](https://perconalive.com/) |

## MongoDB wording in capability copy

- For generic capability coverage, use "MongoDB-compatible environments" or "MongoDB services monitored by PMM."
- For product-specific copy, use the exact product name, for example "Percona Server for MongoDB" or "Percona Operator for MongoDB."
- When a capability does not apply across engines, state scope directly, for example "MongoDB only" and "not MySQL or PostgreSQL."
