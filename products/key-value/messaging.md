# Percona for key/value workloads: Messaging

## Percona for key/value workloads {#percona-for-key-value}

For platform, SRE, and DevOps teams running traditional key/value and in-memory workloads across on-premises, cloud, and hybrid environments, Percona provides Expert Support, Expert Consulting and Services, migration and readiness guidance, and PMM observability for **Valkey** and **Redis**. Percona meets each estate where it is: support continuity on Redis, an open multi-vendor path on Valkey, or both when that fits stability, cost, and compliance needs.

These clusters are rarely owned by traditional DBAs; buyers are usually platform-led, unlike MySQL, PostgreSQL, and MongoDB estates Percona supports. For the shared use cases below, Valkey and Redis are functionally near-identical. Differences usually show up in governance model, memory economics, module strategy, and migration planning. Percona does not own upstream Valkey or Redis development.

### Shared use cases

These apply to both Valkey and Redis:

- Caching
- Sessions
- Pub/sub
- Queues
- Rate limiting
- High-throughput key/value

### Engines

| Engine | Role | Open when |
| --- | --- | --- |
| **Valkey** | Primary open, multi-vendor path (Linux Foundation, BSD 3-Clause) | Governance and trust, memory and TCO, traditional workloads, self-managed or multi-cloud control matter. See [Percona for Valkey](valkey/messaging.md). |
| **Redis** | Support continuity for Redis estates | Teams want to keep Redis as a long-term choice with Expert Support and PMM. See [Percona for Redis](redis/messaging.md). |

### What Percona delivers

- **One support relationship for key/value:** Expert Support, ExpertOps, and Consulting cover Valkey and Redis so teams consolidate operational risk alongside the rest of the Percona estate, rather than treating cache and session layers as a separate vendor problem.
- **Memory-driven infrastructure spend:** In-memory key/value workloads are among the most infrastructure-expensive databases in common use because working sets live in RAM. Percona Experts tune memory allocation, eviction, replication, and topology so teams improve latency and throughput efficiency on less infrastructure.
- **Caching as operational infrastructure:** On critical workloads, the cache layer is a production requirement, not an optional accelerator. Cache failures and memory pressure hit user-facing latency before primary databases show stress. Production readiness means High Availability, support SLAs, observability, and migration rehearsal, not install-only test usage.
- **Honest routing to the right engine:** Some teams prioritize staying on Redis with Expert Support and PMM, or a managed-service posture, while others prioritize Linux Foundation guided open governance, BSD licensing, open modules, and memory economics in Valkey. When a move is in scope, Percona plans cutovers by version and topology rather than assuming one path for every estate.

### Public resources

- [Percona Support for Valkey and Redis](https://www.percona.com/valkey-redis/support/)
- [Percona Expert Consulting and Services](https://www.percona.com/services/expert-consulting-and-services/)
- [PMM Valkey and Redis monitoring](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/connect-database/valkey-redis.html)
