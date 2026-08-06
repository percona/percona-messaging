# Performance Tuning

**Fixed-fee SKU:** CONS-PTFF  
**Starting from:** $11,400

Slow queries rarely get fixed; they get worked around. Someone adds an index in production, waits, and hopes. Adding resources may help, but it is not a long-term solution if you care about infrastructure cost. This engagement takes up to five queries or performance issues you have already identified, finds the actual root cause, and tests every proposed fix in your environment before it goes anywhere near production. You get measurable results, not theories.

This is one packaged fixed-fee scope under [Expert Consulting and Services](messaging.md), not the full Consulting catalog. Broader performance work, or six or more distinct issues, is scoped as custom Performance Tuning consulting instead. If you cannot name the problem queries yet, start with a [Health Audit](health-audit.md).

## FAQ

### What is in scope for the fixed fee?

Up to five specific queries or performance issues that you name at kickoff. This is a focused engagement, not a broad review: we analyze each issue, test proposed changes in your test environment, and document what actually improved. If you are carrying six or more distinct issues, our full Performance Tuning consulting engagement is the right shape instead.

### We do not know which queries are the problem. Is this still the right engagement?

Not yet. This engagement works best when you can point at the problem. If you cannot, start with the [Health Audit](health-audit.md); it surfaces the top consumers by execution time and gives you the prioritized list, and then this engagement takes the fixes from there.

### What do you need from us to start?

Two things from day one: production access and a representative test environment. For Galera clusters that means a representative multi-node test cluster, because write-set replication behavior cannot be reproduced on a single node. We will also need named points of contact for the production review at the end.

### How do we know the fixes actually work?

Because we test them in your pre-production environment before you see them. We replicate your issue in the test environment, apply the proposed change, and record the results achieved; the findings report only contains recommendations that were verified against your workload. What we do not do is guarantee a specific performance number up front. Nobody honestly can, and we would rather show you measured results than promise a percentage.

### Will you make the changes in production for us?

That is available as an option: implementation assistance in production during a scheduled time. By default the engagement ends with a production review of the recommended changes alongside your team, plus the findings and recommendations report, and your team applies the changes on its own schedule.

### What if the problem turns out to be configuration, not the queries?

Then that is what the report says. Slow queries are often a symptom. The report separates query-level fixes from configuration-level ones, so your team knows exactly which lever to pull.

## MySQL Performance Tuning

You already know which queries are hurting; you just need someone who has tuned InnoDB under production load to fix them. This is not a broad health review; it is a focused engagement on the specific queries or performance issues you have identified.

We analyze up to 5 queries or issues, test every recommendation in a representative environment, and hand you results, not theory.

### Deliverables

- Review of up to 5 queries or identified performance issues you specify at kickoff
- Analysis of the existing server, InnoDB buffer pool configuration, and performance metrics via Percona Monitoring and Management
- Review of index usage and query execution plans for each identified query
- Testing of proposed changes in your provided test environment, replicating your issue, before recommending a fix
- Document detailing suggested changes and the results actually achieved in testing
- Production review of recommended changes with your points of contact, plus a findings and recommendations report
- Optional: assistance implementing the recommendations in production during a scheduled time

### Who it is for

Scoped to 1–5 specific queries or performance issues you can name at kickoff. If you are dealing with 6 or more distinct issues, or you do not yet know which queries are the problem, talk to us about our full Performance Tuning consulting engagement instead. This engagement assumes that production access and a representative test environment are both available from day one.

### Outcome

Tested, specific fixes for the queries and configuration issues you already flagged, not a generic tuning checklist. This engagement does not guarantee a specific performance improvement, but every recommendation is verified against your workload before it reaches your findings report.

**CTA:** Get your slowest MySQL queries fixed, not just explained.

## MariaDB Community Performance Tuning

You already know which queries are hurting; you just need someone who has tuned the storage engine under production load to fix them. This is not a broad health review; it is a focused engagement on the specific queries or performance issues you have identified.

We analyze up to 5 queries or issues, test every recommendation in a representative environment, and hand you results, not theory. Percona supports MariaDB Community versions; Enterprise editions are out of scope.

### Deliverables

- Review of up to 5 queries or identified performance issues you specify at kickoff
- Analysis of the existing server, storage engine buffer pool configuration, and performance metrics via Percona Monitoring and Management
- Review of index usage and query execution plans for each identified query
- Testing of proposed changes in your provided test environment, replicating your issue, before recommending a fix
- Document detailing suggested changes and the results actually achieved in testing
- Production review of recommended changes with your points of contact, plus a findings and recommendations report
- Optional: assistance implementing the recommendations in production during a scheduled time

### Who it is for

Scoped to 1–5 specific queries or performance issues you can name at kickoff. If you are dealing with 6 or more distinct issues, or you do not yet know which queries are the problem, talk to us about our full Performance Tuning consulting engagement instead. This engagement assumes that production access and a representative test environment are both available from day one.

### Outcome

Tested, specific fixes for the queries and configuration issues you already flagged, not a generic tuning checklist. This engagement does not guarantee a specific performance improvement, but every recommendation is verified against your workload before it reaches your findings report.

**CTA:** Get your slowest MariaDB Community queries fixed, not just explained.

## PostgreSQL Performance Tuning

Slow PostgreSQL queries are usually a symptom of something else: a missing index, stale statistics, or autovacuum falling behind on a hot table. This engagement targets up to 5 specific queries or issues you have already identified, and gets to the actual root cause.

We use pg_stat_statements data and query plans to diagnose, test proposed fixes in your environment, and verify results before they reach your findings report.

### Deliverables

- Review of up to 5 queries or identified performance issues, using pg_stat_statements and EXPLAIN plan analysis
- Analysis of autovacuum behavior, server configuration, and performance metrics via Percona Monitoring and Management (PMM)
- Review of the table and index statistics accuracy for each identified query
- Testing of proposed changes in your provided test environment
- Document detailing suggested changes and results achieved in testing
- Production review of recommended changes with your points of contact, plus a findings and recommendations report
- Optional: assistance implementing recommendations in production during a scheduled time

### Who it is for

Scoped to 1–5 specific queries or issues you can name at kickoff. If performance across the whole schema is the concern rather than specific queries, our [Health Audit](health-audit.md) is the better starting point. This engagement assumes that production access and a representative test environment are both available from day one.

### Outcome

Tested fixes for the queries you flagged, with the actual root cause identified, not just an index suggestion pulled from a query plan. You will know whether the fix is the query, the statistics, or the vacuum settings behind it, and you will have test results showing the fix actually worked before it goes anywhere near production.

**CTA:** Find out why the query plan changed and what to do about it.

## MongoDB Performance Tuning

Slow MongoDB queries are frequently an indexing or shard key problem wearing a performance costume. This engagement targets up to 5 specific queries or issues you have already identified, and tests every fix in your environment before it goes to production.

We analyze index usage and shard key distribution where applicable, test proposed changes, and verify results before they reach your findings report.

### Deliverables

- Review of up to 5 queries or identified performance issues you specify at kickoff
- Analysis of index usage, query plan (explain output), shard key distribution where applicable, and performance metrics via Percona Monitoring and Management
- Review of aggregation pipeline stages for queries that use them, flagging stages that cannot use an index
- Testing of proposed changes in your provided test environment
- Document detailing suggested changes and results achieved in testing
- Production review of recommended changes with your points of contact, plus a findings and recommendations report
- Optional: assistance implementing recommendations in production during a scheduled time

### Who it is for

Scoped to 1–5 specific queries or issues you can name at kickoff. If the concern is broader (replica set or sharded cluster health generally), our [Health Audit](health-audit.md) is the better fit. This engagement assumes that production access and a representative test environment are both available from day one.

### Outcome

Verified fixes for the queries you flagged, with any indexing or sharding root cause called out explicitly, not a generic "add an index" recommendation without knowing whether the index will actually get used. Where aggregation pipelines are involved, you will know which stages are forcing a collection scan and why.

**CTA:** Get your slow queries diagnosed against your real explain plans and shard key.

## Valkey / Redis Performance Tuning

Latency spikes in Redis or Valkey are usually about data structure choice or persistence overhead, not the command itself. A command that is fast in isolation can still cause latency spikes if it is colliding with an AOF rewrite or a poorly sized eviction policy.

This engagement targets up to 5 specific issues you have already identified, and tests every fix in your environment before it goes to production.

### Deliverables

- Review of up to 5 identified performance issues or command patterns you specify at kickoff
- Analysis of data structure usage, eviction policy, persistence configuration (RDB/AOF), and metrics via PMM
- Review of command complexity (O(N) operations on large collections) contributing to latency
- Testing of proposed changes in your provided test environment
- Document detailing suggested changes and results achieved in testing
- Production review of recommended changes with your points of contact, plus a findings and recommendations report
- Optional: assistance implementing recommendations in production during a scheduled time

### Who it is for

Scoped to 1–5 specific performance issues you can name at kickoff. If you do not yet know what is causing the latency, our [Health Audit](health-audit.md) is a better starting point. This engagement assumes that production access and a representative test environment are both available from day one.

### Outcome

Specific, tested fixes for the latency or memory issues you flagged. You will know whether the spike is a data structure choice, a persistence operation colliding with your traffic, or a command that is O(N) on a collection that has grown past what it was designed for.

**CTA:** Fix the latency spike before it becomes a pattern.
