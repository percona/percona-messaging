# Performance Tuning

**Fixed-fee SKU:** CONS-PTFF  
**Starting from:** $11,400

Slow queries rarely get fixed; they get worked around. Someone adds an index in production, waits, and hopes. This engagement takes up to five queries or performance issues you have already identified, finds the actual root cause, and tests every proposed fix in your environment before it goes anywhere near production. You get the results we measured, not a list of theories.

This is one packaged fixed-fee scope under [Expert Consulting and Services](../messaging.md), not the full Consulting catalog. Broader performance work, or six or more distinct issues, is scoped as custom Performance Tuning consulting instead. If you cannot name the problem queries yet, start with a [Health Audit](../health-audit/messaging.md).

## FAQ

### What is in scope for the fixed fee?

Up to five specific queries or performance issues that you name at kickoff. This is a focused engagement, not a broad review: we analyze each issue, test proposed changes in your test environment, and document what actually improved. If you are carrying six or more distinct issues, our full Performance Tuning consulting engagement is the right shape instead.

### We do not know which queries are the problem. Is this still the right engagement?

Not yet. This engagement works best when you can point at the problem. If you cannot, start with the [Health Audit](../health-audit/messaging.md); it surfaces the top consumers by execution time and gives you the prioritized list, and then this engagement takes the fixes from there.

### What do you need from us to start?

Two things from day one: production access and a representative test environment. For Galera clusters that means a representative multi-node test cluster, because write-set replication behavior cannot be reproduced on a single node. We will also need named points of contact for the production review at the end.

### How do we know the fixes actually work?

Because we test them in your pre-production environment before you see them. We replicate your issue in the test environment, apply the proposed change, and record the results achieved; the findings report only contains recommendations that were verified against your workload. What we do not do is guarantee a specific performance number up front. Nobody honestly can, and we would rather show you measured results than promise a percentage.

### Will you make the changes in production for us?

That is available as an option: implementation assistance in production during a scheduled time. By default the engagement ends with a production review of the recommended changes alongside your team, plus the findings and recommendations report, and your team applies the changes on its own schedule.

### What if the problem turns out to be configuration, not the queries?

Then that is what the report says. Slow queries are often a symptom: stale statistics, autovacuum falling behind, flow control reacting to write contention, or an eviction policy fighting your working set. The report separates query-level fixes from configuration-level ones, so your team knows exactly which lever to pull.

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

[MySQL](/offerings/expert-consulting/performance-tuning/mysql.md ':include')

[MariaDB Server](/offerings/expert-consulting/performance-tuning/mariadb.md ':include')

[PostgreSQL](/offerings/expert-consulting/performance-tuning/postgresql.md ':include')

[MongoDB](/offerings/expert-consulting/performance-tuning/mongodb.md ':include')

[Valkey / Redis](/offerings/expert-consulting/performance-tuning/valkey-redis.md ':include')
