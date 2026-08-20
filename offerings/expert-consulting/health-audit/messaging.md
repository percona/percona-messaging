# Health Audit

**Fixed-fee SKU:** CONS-HAFF  
**Starting from:** $11,400

A database that looks healthy today can be one traffic spike away from an incident. Defaults nobody revisited, replication quietly falling behind, indexes that no longer match the workload: none of it shows up until something breaks. This audit reviews your full stack against how it actually runs in production, and hands your team a scored, prioritized list of what to fix first. The report and a live rundown land 5–7 business days after kickoff.

This is one packaged fixed-fee scope under [Expert Consulting and Services](../messaging.md), not the full Consulting catalog. Larger or multi-cluster environments, and any audit shape outside this gate, are scoped as custom consulting instead.

## FAQ

### What does the health audit actually cover?

The full stack, not just the database config. We review hardware and OS, configuration, schema and index design, replication or cluster topology, and security, all against how your specific workload runs in production. You get three scorecards: overall health, configuration against best-practice baselines, and recommendations ranked by expected impact and implementation effort.

### How large an environment fits the fixed-fee audit?

A single deployment of 1 to 5 servers: a standalone server or source-replica pair, a single Galera cluster, a primary-standby pair, a replica set or single sharded cluster, or a single Valkey or Redis cluster, depending on your engine. MongoDB is the exception: a single replica set or single sharded cluster with 1–6 data-bearing nodes still fits the fixed fee. If you are running above those limits, multiple clusters, or mixed topologies, that is not a problem; it is scoped under our full consulting audit instead.

### What do we receive, and how fast?

A PDF audit report 5–7 business days after kickoff, followed by a live rundown session with open Q&A. The report ranks every recommendation by impact and effort, so your team knows what to fix first and has a chance to ask an expert about the recommendations.

### Do you make changes to our systems during the audit?

No. This is a review. Nothing in your environment changes unless your team changes it.

### Can we run this on a recurring basis?

Yes. The audit is a point-in-time review, but if you want recurring checkpoints, ask about wrapping it into a quarterly wellness plan.

### What happens if we need help fixing what you find?

The report is written so your team can act on it directly. If you would rather have a Percona expert implement the changes, talk to us about a follow-on engagement.

## Engine variants

Source files are split by engine so tech owners can review only their variant. Engine files on this PR are stubs; full copy lands in follow-up tech PRs (issue #274). On the Docsify site, includes still render below once those PRs land.

| Engine | Source file |
| --- | --- |
| MySQL | [MySQL](mysql.md) |
| MariaDB Server | [MariaDB Server](mariadb.md) |
| PostgreSQL | [PostgreSQL](postgresql.md) |
| MongoDB | [MongoDB](mongodb.md) |
| Valkey / Redis | [Valkey / Redis](valkey-redis.md) |

<!-- docsify assemble: full package page for readers -->

[MySQL](/offerings/expert-consulting/health-audit/mysql.md ':include')

[MariaDB Server](/offerings/expert-consulting/health-audit/mariadb.md ':include')

[PostgreSQL](/offerings/expert-consulting/health-audit/postgresql.md ':include')

[MongoDB](/offerings/expert-consulting/health-audit/mongodb.md ':include')

[Valkey / Redis](/offerings/expert-consulting/health-audit/valkey-redis.md ':include')
