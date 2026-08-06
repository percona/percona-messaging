# Health Audit

**Fixed-fee SKU:** CONS-HAFF  
**Starting from:** $11,400

A database that looks healthy today can be one traffic spike away from an incident. Defaults nobody revisited, replication quietly falling behind, indexes that no longer match the workload: none of it shows up until something breaks. This audit reviews your full stack against how it actually runs in production, and hands your team a scored, prioritized list of what to fix first. The report and a live rundown land 5–7 business days after kickoff.

This is one packaged fixed-fee scope under [Expert Consulting and Services](messaging.md), not the full Consulting catalog. Larger or multi-cluster environments, and any audit shape outside this gate, are scoped as custom consulting instead.

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

## MySQL Health Audit

Your MySQL environment runs the business, but nobody has looked under the hood since it went into production. Most teams only find out their replication topology or InnoDB configuration was wrong when something breaks at 2 a.m., not before.

This audit is a full pass over the stack: hardware and OS, InnoDB configuration, schema and index design, replication topology, and security. We review the environment the way a Percona expert would review a system they were about to get paged for, tracing how your specific workload interacts with your configuration rather than running through a generic checklist.

### Deliverables

- Overall Health Scorecard covering hardware/OS, data design, workload and configuration, high availability, and security
- Report Scorecard evaluating configuration against best-practice baselines, flagging where defaults are quietly working against you
- Ranking of recommendations by expected impact and implementation effort
- Review of replication topology, including failover behavior
- Query review covering top queries by execution time, lock contention, and index usage
- Infrastructure and OS-level metrics review, including storage I/O and memory allocation against InnoDB buffer pool sizing
- PDF audit report delivered 5–7 business days after kickoff, plus a live rundown session with open Q&A

### Who it is for

Built for a single standalone MySQL server or source and its replicas, or synchronous clusters (Group Replication, InnoDB Cluster, Percona XtraDB Cluster), 1–5 servers. Larger or more complex environments should be scoped under our full consulting audit instead of the fixed-fee engagement.

### Outcome

You leave with a documented, prioritized list of what is misconfigured, what is about to become a problem at scale, and what to fix first. Every recommendation is tied to your actual workload, so your team can act on it without re-litigating whether it applies to your environment.

**CTA:** See what can be improved in your MySQL stack.

## MariaDB Community Health Audit

Your MariaDB Community environment runs the business, but nobody has looked under the hood since it went into production. Most teams only find out their replication topology or storage engine configuration was wrong when something breaks at 2 a.m., not before.

This audit is a full pass over the stack: hardware and OS, storage engine configuration, schema and index design, replication topology, and security. We review the environment the way a Percona expert would review a system they were about to get paged for, tracing how your specific workload interacts with your configuration, rather than running through a generic checklist. Percona supports MariaDB Community versions; Enterprise editions are out of scope.

### Deliverables

- Overall Health Scorecard covering hardware/OS, data design, workload and configuration, high availability, and security
- Report Scorecard evaluating configuration against best-practice baselines, flagging where defaults are quietly working against you
- Ranking of recommendations by expected impact and implementation effort
- Review of replication topology, including failover behavior
- Query review covering top queries by execution time, lock contention, and index usage
- Infrastructure and OS-level metrics review, including storage I/O and memory allocation against buffer pool sizing
- PDF audit report delivered 5–7 business days after kickoff, plus a live rundown session with open Q&A

### Who it is for

Built for a single standalone MariaDB Community server or source and its replicas, or synchronous clusters (Galera Cluster), 1–5 servers. Larger or more complex environments should be scoped under our full consulting audit instead of the fixed-fee engagement.

### Outcome

You leave with a documented, prioritized list of what is misconfigured, what is about to become a problem at scale, and what to fix first. Every recommendation is tied to your actual workload.

**CTA:** See what can be improved in your MariaDB Community stack.

## PostgreSQL Health Audit

Autovacuum, WAL retention, and replication lag are the three things that quietly wreck PostgreSQL deployments, and they rarely show up until they already have: usually as bloat nobody budgeted for, or a standby that has fallen far enough behind that failover is no longer safe.

This audit reviews your full PostgreSQL stack against how it is actually being used: hardware and OS, autovacuum and WAL configuration, schema design, replication, and security, scoped to a single standalone instance or primary and its replicas.

### Deliverables

- Overall Health Scorecard covering hardware/OS, data design, workload and configuration, high availability, and security
- Report Scorecard evaluating configuration against workload-specific baselines, not generic postgresql.conf defaults
- Ranking of recommendations by impact and effort
- Review of streaming and logical replication setup
- Query review to flag top consumers by total time and call count
- Autovacuum and bloat analysis across your largest tables
- PDF report delivered 5–7 business days after kickoff, plus a live rundown with Q&A

### Who it is for

Scoped to a single standalone PostgreSQL instance or primary and its replicas, 1–5 servers. Multi-region topologies, sharded (for example Citus) deployments, or 6+ server environments should be scoped under the custom consulting audit.

### Outcome

You will know which settings are fighting your workload and which schema decisions will cost you at your next order-of-magnitude growth point, including whether your hardware can keep up with your growing TPS rate.

**CTA:** Get ahead of the autovacuum problem you do not know you have.

## MongoDB Health Audit

Replica set health and sharded cluster balance do not announce themselves; they show up as latency spikes, oplog rollover, or a chunk migration that has been stuck for three days during your busiest week.

This audit reviews your deployment's configuration, replica set or sharded cluster topology, chunk distribution, and query patterns end to end, before any of that reaches production impact.

### Deliverables

- Overall Health Scorecard covering hardware/OS, data design, workload and configuration, high availability, and security
- Report Scorecard evaluating configuration against replica set or sharded cluster best practices
- Recommendation Scorecard ranking fixes by impact and effort
- Replica set status and stats review, including oplog window, election configuration, and write concern behavior under load
- Sharded cluster chunk balancing and shard key review, where applicable, including hotspot analysis and jumbo chunk detection
- Query review flagging inefficient patterns, missing indexes, and collection scan frequency (recommendations only)
- Review of WiredTiger cache sizing and its relationship to your working set size
- PDF report delivered 5–7 business days after kickoff, plus a live rundown with Q&A

### Who it is for

Scoped to a single replica set or a single sharded cluster (1–6 data-bearing nodes; the fixed-fee size exception for MongoDB). Multi-region deployments, cross-region topologies, or environments with 7+ nodes should be scoped under our full consulting audit.

### Outcome

A specific, prioritized view of what is misconfigured in your replica set or sharded cluster, and what happens to it under next quarter's growth. You will know whether your shard key is actually distributing writes evenly before it becomes the reason for an emergency re-sharding project, and whether your WiredTiger cache is sized for the working set you actually have, not the one you started with.

**CTA:** Know your shard key choices before they choose your outage.

## Valkey / Redis Health Audit

Most Redis and Valkey deployments are still running on defaults nobody revisited after the initial rollout: cluster topology, eviction policy, and data structure choices included. That is fine until a node suffers a significant latency spike.

This audit reviews the deployment against how it is actually used in production: hardware and OS, cluster configuration, data structure design, and security, scoped to a single cluster or replica set.

### Deliverables

- Overall Health Scorecard covering hardware/OS, data structure design, workload and configuration, high availability, and security
- Report Scorecard evaluating configuration against durability and availability requirements you have actually stated
- Ranking of recommendations by impact and effort
- Stats review, cluster hash slot distribution and shard balancing review
- Persistence configuration review against your actual durability requirements
- Eviction policy and memory management review against your actual key expiration and working set patterns
- Migration-to-Valkey options review, where applicable, including module compatibility considerations
- PDF report delivered 5–7 business days after kickoff, plus a live rundown with Q&A

### Who it is for

Scoped to a single Redis or Valkey environment (standalone, primary/replica, sentinel, cluster mode). Multi-region deployments should be scoped under our custom consulting audit.

### Outcome

Clarity on whether your cluster configuration matches your actual durability and availability requirements, not just what shipped by default. You will know exactly what data survives a node failure and what does not, before you find out the hard way, and whether your eviction policy is quietly dropping keys your application still expects to find.

**CTA:** Check whether your durability and eviction settings match production reality.
