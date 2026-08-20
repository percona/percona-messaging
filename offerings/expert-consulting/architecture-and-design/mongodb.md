## MongoDB Architecture and Design

Sharding decisions made early (shard key selection, chunk distribution strategy, replica set topology) are expensive to reverse later. A shard key that looked reasonable at launch can turn into an unbalanced cluster and a re-sharding project a year in.

We review your current or planned architecture against your actual access patterns and growth trajectory, and validate whether your shard key and topology choices will hold up.

## Deliverables

- Joint discovery sessions reviewing current and proposed architecture and data access patterns
- Detailed collection of performance requirements, scalability concerns, HA needs, and maintenance activities
- Validation or invalidation of shard key selection and sharded cluster or replica set topology against stated access patterns
- Documented infrastructure requirements, growth and scalability plan, monitoring/alerting plan, and backup policy
- Review of read/write concern settings against your consistency and durability requirements
- For Atlas/DBaaS environments: documented scaling and cost guidance, plus mitigation recommendations
- Options document with pros and cons of viable architectures, plus a live Q&A rundown

## Who it is for

Built for teams planning a new MongoDB deployment or reviewing a replica set or sharded cluster that has outgrown its original design, self-managed, Atlas, or another DBaaS. Covers how your shard key choice interacts with query routing and targeted versus scatter-gather operations.

## Outcome

A shard key and topology decision backed by your actual data access patterns, not a guess you will have to migrate away from in a year. You will leave with a documented rationale for the shard key you chose, and the ones you ruled out, along with read/write concern settings that match what you actually need, not the defaults.

**CTA:** Pick your shard key once. Get it right.
