## MySQL Health Audit

Your MySQL environment runs the business, but nobody has looked under the hood since it went into production. Most teams only find out their replication topology or InnoDB configuration was wrong when something breaks at 2 a.m., not before.

This audit is a full pass over the stack: hardware and OS, InnoDB configuration, schema and index design, replication topology, and security. We review the environment the way a Percona expert would review a system they were about to get paged for, tracing how your specific workload interacts with your configuration rather than running through a generic checklist.

## Deliverables

- Overall Health Scorecard covering hardware/OS, data design, workload and configuration, high availability, and security
- Report Scorecard evaluating configuration against best-practice baselines, flagging where defaults are quietly working against you
- Ranking of recommendations by expected impact and implementation effort
- Review of replication topology, including failover behavior
- Query review covering top queries by execution time, lock contention, and index usage
- Infrastructure and OS-level metrics review, including storage I/O and memory allocation against InnoDB buffer pool sizing
- PDF audit report delivered 5–7 business days after kickoff, plus a live rundown session with open Q&A

## Who it is for

Built for a single standalone MySQL server or source-replica pair, 1–5 servers. Teams running MySQL synchronous clusters (Group Replication, InnoDB Cluster) get a scoped single-node review under this same engagement. Larger or more complex environments (6+ servers, multiple clusters, or mixed topologies) should be scoped under our full consulting audit instead of the fixed-fee engagement.

## Outcome

You leave with a documented, prioritized list of what is misconfigured, what is about to become a problem at scale, and what to fix first. Every recommendation is tied to your actual workload, so your team can act on it without re-litigating whether it applies to your environment.

**CTA:** See what can be improved in your MySQL stack.
