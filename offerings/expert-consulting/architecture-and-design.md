# Architecture and Design

**SKU:** CONS-AD  
**Starting from:** $11,400

Scaling is not just adding read replicas. It is a series of decisions about topology, consistency, and failure modes that get harder to unwind the longer you wait. Teams usually run this review before deploying a new application, or when growth or traffic patterns shift enough that the original design is no longer sufficient. We review your current or planned architecture against your actual workload, growth numbers, and availability targets, and you walk away with a documented set of options and the trade-offs behind each one.

This is one packaged fixed-fee scope under [Expert Consulting and Services](messaging.md), not the full Consulting catalog. Implementation happens through Migration, Setup and Configuration, or other custom consulting scope when the need sits outside this design engagement.

## FAQ

### Is this for new deployments or existing ones?

Both. Teams use it to design a new deployment before anything is built, or to review an architecture that has outgrown its original design. Either way, we work from your actual access patterns, growth projections, and availability requirements, not a reference diagram.

### What do we walk away with?

An options document laying out each viable architecture for your use case with the pros and cons of each, plus documented infrastructure requirements, a growth and scalability plan, a monitoring and alerting plan, and a backup policy. It ends with a live Q&A rundown with your team.

### Will you just tell us which architecture to pick?

We will tell you which options hold up against your requirements and which do not, and why. The document records the rationale for what was chosen and what was ruled out, so the decision survives after the engagement ends and your next hire does not have to re-litigate it.

### Do you cover cloud and DBaaS deployments?

Yes. Self-managed, RDS, Aurora, Atlas, and other DBaaS platforms are all in scope. For DBaaS environments the review includes documented scaling and cost considerations, with guidance on controlling cloud spend.

### We already know our target architecture. Is this still useful?

Probably not on its own. If the design decision is already made, pair your project with our Migration or Setup and Configuration engagement instead. This engagement earns its fee when the options are still open. After go-live, a [Health Audit](health-audit.md) is usually the better next step.

### Does this include building the architecture?

No. This is the design phase. Implementation happens through Migration or Setup and Configuration engagements, and the options document is written to hand straight into either one.

## MySQL Architecture and Design

Scaling MySQL is not just adding read replicas; it is a series of decisions about topology, consistency, and failure modes that get harder to unwind the longer you wait. A replication topology chosen for today's traffic does not automatically hold up at three times the write volume, and most teams do not find out until a failover goes wrong.

We review your current or planned architecture against your actual business objectives, access patterns, and growth trajectory, not a generic reference architecture pulled from documentation.

### Deliverables

- Joint discovery sessions reviewing current and proposed architecture, data access patterns, and methods
- Detailed analysis of performance requirements, scalability concerns, growth projections, HA needs, and maintenance activities
- Validation or invalidation of proposed replication topology (asynchronous, semi-sync, Percona XtraDB Cluster, or Group Replication) against stated availability requirements
- Documented infrastructure requirements based on performance and availability needs, plus a growth and scalability plan
- Monitoring and alerting plan, backup policy, and for DBaaS deployments: documented scaling and cost considerations, plus mitigation guidance to control cloud spend
- A document detailing the pros and cons of each viable architecture for your specific use case, followed by a live Q&A rundown

### Who it is for

Built for teams planning a new MySQL deployment, or reviewing one that has outgrown its original design, whether self-managed, RDS, Aurora, or another DBaaS. If you already know your target architecture and just need implementation, pair this with our Migration or Setup and Configuration engagement instead.

### Outcome

A documented architecture roadmap you can hand to your team or your next hire, tied directly to your growth numbers instead of generic best-guess sizing. You will walk away knowing which architecture options were ruled out, and why, not just which one was picked.

**CTA:** Design it right before you have to redesign it under load.

## MariaDB Community Architecture and Design

Scaling MariaDB Community is not just adding read replicas; it is a series of decisions about topology, consistency, and failure modes that get harder to unwind the longer you wait. A replication topology chosen for today's traffic does not automatically hold up at three times the write volume, and most teams do not find out until a failover goes wrong.

We review your current or planned architecture against your actual business objectives, access patterns, and growth trajectory, not a generic reference architecture pulled from documentation. Percona supports MariaDB Community versions; Enterprise editions are out of scope.

### Deliverables

- Joint discovery sessions reviewing current and proposed architecture, data access patterns, and methods
- Detailed analysis of performance requirements, scalability concerns, growth projections, HA needs, and maintenance activities
- Validation or invalidation of proposed replication topology (asynchronous, semi-sync, Galera) against stated availability requirements
- Documented infrastructure requirements based on performance and availability needs, plus a growth and scalability plan
- Monitoring and alerting plan, backup policy, and for DBaaS deployments: documented scaling and cost considerations, plus mitigation guidance to control cloud spend
- A document detailing the pros and cons of each viable architecture for your specific use case, followed by a live Q&A rundown

### Who it is for

Built for teams planning a new MariaDB Community deployment, or reviewing one that has outgrown its original design, whether self-managed, RDS, or another DBaaS. If you already know your target architecture and just need implementation, pair this with our Migration or Setup and Configuration engagement instead.

### Outcome

A documented architecture roadmap you can hand to your team or your next hire, tied directly to your growth numbers instead of generic best-guess sizing. You will walk away knowing which architecture options were ruled out, and why, not just which one was picked.

**CTA:** Design it right before you have to redesign it under load.

## PostgreSQL Architecture and Design

Whether you are planning a new PostgreSQL deployment or reviewing one that has outgrown its original design, the decisions that matter are about replication topology, partitioning strategy, and extension choices, not generic sizing guides that ignore your actual access patterns.

We review your architecture against your stated performance, growth, and availability requirements, and validate whether your planned approach actually holds up.

### Deliverables

- Joint discovery sessions reviewing current and proposed architecture and data access patterns
- Detailed collection of performance requirements, scalability concerns, HA needs, and maintenance activities
- Validation or invalidation of streaming replication, logical replication, or partitioning strategy against your stated requirements
- Documented infrastructure requirements, growth and scalability plan, monitoring/alerting plan, and backup policy
- Review of connection pooling strategy (PgBouncer or similar) against your expected connection volume
- For DBaaS/Aurora/RDS environments: documented scaling and cost guidance specific to the platform, plus mitigation recommendations
- Options document with pros and cons of viable architectures, plus a live Q&A rundown

### Who it is for

Built for teams planning a new PostgreSQL deployment or reviewing one that has outgrown its original design, self-managed, RDS, Aurora, or another DBaaS. Extension compatibility is reviewed as part of the architecture discussion where relevant, along with how connection pooling interacts with your planned replication topology.

### Outcome

A defensible architecture decision, documented with the trade-offs you actually care about, not a slide that says "use read replicas." You will know whether your partitioning strategy holds up at your projected table size before you have built it.

**CTA:** Get a PostgreSQL architecture that survives your next growth curve.

## MongoDB Architecture and Design

Sharding decisions made early (shard key selection, chunk distribution strategy, replica set topology) are expensive to reverse later. A shard key that looked reasonable at launch can turn into an unbalanced cluster and a re-sharding project a year in.

We review your current or planned architecture against your actual access patterns and growth trajectory, and validate whether your shard key and topology choices will hold up.

### Deliverables

- Joint discovery sessions reviewing current and proposed architecture and data access patterns
- Detailed collection of performance requirements, scalability concerns, HA needs, and maintenance activities
- Validation or invalidation of shard key selection and sharded cluster or replica set topology against stated access patterns
- Documented infrastructure requirements, growth and scalability plan, monitoring/alerting plan, and backup policy
- Review of read/write concern settings against your consistency and durability requirements
- For Atlas/DBaaS environments: documented scaling and cost guidance, plus mitigation recommendations
- Options document with pros and cons of viable architectures, plus a live Q&A rundown

### Who it is for

Built for teams planning a new MongoDB deployment or reviewing a replica set or sharded cluster that has outgrown its original design, self-managed, Atlas, or another DBaaS. Covers how your shard key choice interacts with query routing and targeted versus scatter-gather operations.

### Outcome

A shard key and topology decision backed by your actual data access patterns, not a guess you will have to migrate away from in a year. You will leave with a documented rationale for the shard key you chose, and the ones you ruled out, along with read/write concern settings that match what you actually need, not the defaults.

**CTA:** Pick your shard key once. Get it right.

## Valkey / Redis Architecture and Design

Cluster topology, persistence strategy, and data structure choices determine whether your Valkey or Redis deployment holds up under real production load. Most of these decisions get made once, at launch, and never revisited against actual traffic.

We review your current or planned architecture end to end: cluster topology, hash slot distribution, and persistence configuration against your actual durability and availability requirements.

### Deliverables

- Joint discovery sessions reviewing current and proposed architecture and data access patterns
- Detailed collection of performance requirements, scalability concerns, HA needs, and maintenance activities
- Validation or invalidation of cluster topology, hash slot distribution, and persistence configuration
- Documented infrastructure requirements, growth and scalability plan, monitoring/alerting plan, and backup policy
- Review of client-side routing and connection handling against your planned cluster topology
- For DBaaS/AWS ElastiCache environments: documented scaling and cost guidance, plus mitigation recommendations
- Options document with pros and cons of viable architectures, plus a live Q&A rundown

### Who it is for

Built for teams planning a new Valkey or Redis deployment, or reviewing a cluster that has outgrown its original topology, self-managed or DBaaS. Module compatibility and Valkey migration considerations are reviewed where relevant, including how your client library's cluster awareness behaves during resharding.

### Outcome

A cluster and persistence design that matches your actual durability requirements, not the defaults it shipped with. You will know precisely what happens to your data during a node failure before it happens in production, and whether your client library will follow a hash slot migration without dropped connections.

**CTA:** Design cluster topology and persistence for the load you actually run.
