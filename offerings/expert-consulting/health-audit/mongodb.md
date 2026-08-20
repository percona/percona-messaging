## MongoDB Health Audit

Replica set health and sharded cluster balance do not announce themselves; they show up as latency spikes, oplog rollover, or a chunk migration that has been stuck for three days during your busiest week.

This audit reviews your deployment's configuration, replica set or sharded cluster topology, chunk distribution, and query patterns end to end, before any of that reaches production impact.

## Deliverables

- Overall Health Scorecard covering hardware/OS, data design, workload and configuration, high availability, and security
- Report Scorecard evaluating configuration against replica set or sharded cluster best practices
- Recommendation Scorecard ranking fixes by impact and effort
- Replica set status and stats review, including oplog window, election configuration, and write concern behavior under load
- Sharded cluster chunk balancing and shard key review, where applicable, including hotspot analysis and jumbo chunk detection
- Query review flagging inefficient patterns, missing indexes, and collection scan frequency (recommendations only)
- Review of WiredTiger cache sizing and its relationship to your working set size
- PDF report delivered 5–7 business days after kickoff, plus a live rundown with Q&A

## Who it is for

Scoped to a single replica set or a single sharded cluster (1–6 data-bearing nodes; the fixed-fee size exception for MongoDB). Multi-region deployments, cross-region topologies, or environments with 7+ nodes should be scoped under our full consulting audit.

## Outcome

A specific, prioritized view of what is misconfigured in your replica set or sharded cluster, and what happens to it under next quarter's growth. You will know whether your shard key is actually distributing writes evenly before it becomes the reason for an emergency re-sharding project, and whether your WiredTiger cache is sized for the working set you actually have, not the one you started with.

**CTA:** Know your shard key choices before they choose your outage.
