## PostgreSQL Performance Tuning

Slow PostgreSQL queries are usually a symptom of something else: a missing index, stale statistics, or autovacuum falling behind on a hot table. This engagement targets up to 5 specific queries or issues you have already identified, and gets to the actual root cause.

We use pg_stat_statements data and query plans to diagnose, test proposed fixes in your environment, and verify results before they reach your findings report.

## Deliverables

- Review of up to 5 queries or identified performance issues, using pg_stat_statements and EXPLAIN plan analysis
- Analysis of autovacuum behavior, server configuration, and performance metrics via Percona Monitoring and Management (PMM)
- Review of the table and index statistics accuracy for each identified query
- Testing of proposed changes in your provided test environment
- Document detailing suggested changes and results achieved in testing
- Production review of recommended changes with your points of contact, plus a findings and recommendations report
- Optional: assistance implementing recommendations in production during a scheduled time

## Who it is for

Scoped to 1–5 specific queries or issues you can name at kickoff. If performance across the whole schema is the concern rather than specific queries, our [Health Audit](../health-audit/messaging.md) is the better starting point. This engagement assumes that production access and a representative test environment are both available from day one.

## Outcome

Tested fixes for the queries you flagged, with the actual root cause identified, not just an index suggestion pulled from a query plan. You will know whether the fix is the query, the statistics, or the vacuum settings behind it, and you will have test results showing the fix actually worked before it goes anywhere near production.

**CTA:** Find out why the query plan changed and what to do about it.
