## MongoDB Performance Tuning

Slow MongoDB queries are frequently an indexing or shard key problem wearing a performance costume. This engagement targets up to 5 specific queries or issues you have already identified, and tests every fix in your environment before it goes to production.

We analyze index usage and shard key distribution where applicable, test proposed changes, and verify results before they reach your findings report.

## Deliverables

- Review of up to 5 queries or identified performance issues you specify at kickoff
- Analysis of index usage, query plan (explain output), shard key distribution where applicable, and performance metrics via Percona Monitoring and Management
- Review of aggregation pipeline stages for queries that use them, flagging stages that cannot use an index
- Testing of proposed changes in your provided test environment
- Document detailing suggested changes and results achieved in testing
- Production review of recommended changes with your points of contact, plus a findings and recommendations report
- Optional: assistance implementing recommendations in production during a scheduled time

## Who it is for

Scoped to 1–5 specific queries or issues you can name at kickoff. If the concern is broader (replica set or sharded cluster health generally), our [Health Audit](../health-audit/messaging.md) is the better fit. This engagement assumes that production access and a representative test environment are both available from day one.

## Outcome

Verified fixes for the queries you flagged, with any indexing or sharding root cause called out explicitly, not a generic "add an index" recommendation without knowing whether the index will actually get used. Where aggregation pipelines are involved, you will know which stages are forcing a collection scan and why.

**CTA:** Get your slow queries diagnosed by someone who has read a query plan before.
