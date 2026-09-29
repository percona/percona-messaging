# Percona Expert Consulting and Services

**Project-based execution and specialized expertise for major architectural changes, deep technical analysis, and complex edge-case resolution.**

Designed for teams tackling the hardest database work. Get expert-led architecture, migrations, upgrades, and deep technical execution across MySQL, PostgreSQL, MongoDB, Valkey/Redis, and MariaDB Server. Consulting handles the hard, high-skill, complex work, like setting up new environments, migrations, upgrades, architecture, deep performance tuning, security and compliance reviews, and similar engagements, typically delivered as defined projects. Percona experts design solutions, execute critical tasks, or provide structured assessments with defined deliverables across open source database stacks.

- **Who Expert Consulting is for:** Teams preparing for major changes, organizations with strong internal talent that need expert assistance for the hardest or highest-risk work, companies modernizing architectures or preparing for audits.
- **Problems Expert Consulting solves:** Complex migrations or upgrades, scaling and performance bottlenecks, architecture uncertainty or decisions with high long-term impact, security or compliance gaps, and unclear patterns in query performance or storage behavior.
- **Outcomes Expert Consulting delivers:** Expert-built migration or upgrade plans, faster performance through schema/query/configuration tuning, secure and well-architected environments, clear recommendations and action plans, reduced risk during critical transitions, and structured modernization paths across cloud, on-premises, hybrid, and Kubernetes environments as needed.

Consulting is project-based and time-boxed. It complements steady-state [Expert Support](../expert-support/messaging.md) or [ExpertOps](../expertops/messaging.md); it does not replace either. Pre-packaged Consulting + Support engagements are [solution bundles](../solution-bundles/messaging.md).

## Common scenarios

- **Migrations and upgrades:** Planned version, platform, or topology changes when source, target, and timing are largely set; delivered as defined projects with planning and hands-on execution where scoped. When End of Life (EOL) timing drives the case, assessment can also scope Extended Lifecycle Support (ELS) alongside the upgrade or migration path. Fixed-scope migration engagements live under [Migration and Modernization](../migration-program/messaging.md), not as peer fixed-fee Consulting SKUs here.
- **Legacy exit and modernization:** When license, renewal, or vendor pressure drives a move to open source targets, assessment scopes how complex the move is for the chosen target. Percona delivers scoped work directly or through a **Migration and Modernization** engagement with the Percona + HexaCluster partnership for proprietary exits such as Oracle to PostgreSQL. The customer contracts with Percona for the full engagement. Optional post-migration Expert Support follows cutover.
- **Assessments:** Structured health, performance, security, or compliance reviews with clear recommendations and deliverables.
- **Architecture and modernization:** Major design decisions and modernization paths across cloud, on-premises, hybrid, and Kubernetes environments.
- **Deep performance work:** Schema, query, configuration, and scaling work when bottlenecks or unclear storage and query behavior exceed advisory support scope.

## Fixed-fee scopes (a subset, not the full catalog)

These five engagements are **packaged fixed-fee scopes**: common, well-bounded work with a defined SKU and starting price. They are **not** the full Expert Consulting catalog.

Expert Consulting also covers custom, time-boxed projects outside these gates: larger or multi-cluster environments, six or more distinct performance issues, Setup and Configuration, upgrades, edge-case remediation, extended assessments, and other scoped delivery. If the need does not fit a fixed-fee gate below, that is normal; we scope a custom consulting engagement instead.

| Engagement | SKU | Starting from |
| --- | --- | --- |
| Health Audit | CONS-HAFF | $11,400 |
| Architecture and Design | CONS-AD | $11,400 |
| Performance Tuning | CONS-PTFF | $11,400 |
| Database Monitoring QuickStart | CONS-PMM | $4,500 |
| Security Assessment | CONS-SECFF | $6,800 |

### Health Audit

**SKU:** CONS-HAFF  
**Starting from:** $11,400

A database that looks healthy today can be one traffic spike away from an incident. Defaults nobody revisited, replication quietly falling behind, indexes that no longer match the workload: none of it shows up until something breaks. This audit reviews your full stack against how it actually runs in production, and hands your team a scored, prioritized list of what to fix first. The report and a live rundown land 5–7 business days after kickoff.

Larger or multi-cluster environments, and any audit shape outside this gate, are scoped as custom consulting instead.

### Architecture and Design

**SKU:** CONS-AD  
**Starting from:** $11,400

Architecture decisions are cheap to make and expensive to undo. Choices that fit today's traffic can fall over at 3x write volume, and by then, every fix is a migration. We review your current or planned architecture against your actual workload, growth numbers, and availability targets, and you walk away with a documented set of options and the trade-offs behind each one.

Implementation happens through Migration, Setup and Configuration, or other custom consulting scope when the need sits outside this design engagement.

### Performance Tuning

**SKU:** CONS-PTFF  
**Starting from:** $11,400

Slow queries rarely get fixed; they get worked around. Someone adds an index in production, waits, and hopes. This engagement takes up to five queries or performance issues you have already identified, finds the actual root cause, and tests every proposed fix in your environment before it goes anywhere near production. You get the results we measured, not a list of theories.

Broader performance work, or six or more distinct issues, is scoped as custom Performance Tuning consulting instead. If you cannot name the problem queries yet, start with a Health Audit.

### Database Monitoring QuickStart

**SKU:** CONS-PMM  
**Starting from:** $4,500

Most monitoring rollouts stall the same way: the server goes up, the default dashboards go unread, and the alerts never get tuned, so nobody trusts them. This engagement deploys Percona Monitoring and Management (PMM) against your environment and, more to the point, teaches your team to use it: reading query analytics, setting alert thresholds your team has actually agreed to, and owning upgrades going forward. PMM is open source; this is how it becomes useful in days instead of quarters. The packaged QuickStart covers MySQL, MariaDB Server, PostgreSQL, and MongoDB.

PMM Customization, multi-environment rollouts, and other monitoring work outside this QuickStart are scoped separately.

### Security Assessment

**SKU:** CONS-SECFF  
**Starting from:** $6,800

Database security gaps rarely come from exotic attacks; they come from drift. An account that kept its privileges after the project ended, a default nobody hardened, a patch that is still in the backlog. This assessment reviews your configuration, access controls, and operational practices against the specific requirements you are accountable for, whether that is PCI-DSS, HIPAA, or your own internal policy, and gives you a prioritized list of what to fix first.

Multi-environment estates, remediation programs, and security work outside this assessment gate are scoped as custom consulting instead.

For migration cutovers, proprietary-to-PostgreSQL assessment, and Galera-to-Percona XtraDB Cluster moves, see [Migration and Modernization](../migration-program/messaging.md). Those migration engagements are likewise a subset of what Migration and Modernization can cover.
