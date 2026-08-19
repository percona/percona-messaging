# Percona for Redis: Messaging

## Percona for Redis {#percona-for-redis}

For platform, SRE, and DevOps teams running traditional key/value and in-memory workloads on Redis across on-premises, cloud, and hybrid environments, Percona provides Expert Support, Expert Consulting and Services, operational guidance, and PMM observability. Percona supports Redis users with operational expertise; Percona does not contribute to Redis as a maintainer. Staying on Redis is a first-class outcome.

See also the [key/value overview](../messaging.md). Optional open-path messaging lives on [Percona for Valkey](../valkey/messaging.md).

### Customer Challenges and Value Alignment: Redis

**Optimized TCO**

- **Keep using Redis:** Teams that are happy with current Redis operations or run via a managed Redis service can keep Redis as a long-term choice. Percona supports that path with Expert Support, incident escalation help, and PMM observability.
- **Memory pressure still drives cost:** Redis keeps working sets in RAM, which can become expensive at scale. Percona Experts help teams tune memory allocation, eviction, replication, and topology to improve latency and throughput efficiency on Redis estates.

**Performance and Reliability at Scale**

- **Traditional workloads first:** Caching, sessions, pub/sub, queues, rate limiting, and high-throughput key/value work. On important systems, the cache is required for production, not an optional accelerator.
- **Less load on the main database:** Redis often sits in front of or alongside MySQL, PostgreSQL, or MongoDB-compatible systems. A well-tuned cache helps the app handle more traffic and cuts read load on those databases. That can delay expensive scale up.
- **Tuning and high availability:** Percona Experts help stabilize production Redis under heavy use and during failures. Most platform teams do not have deep in-memory ops skills. 24×7 Expert Support and consulting cover escalation, architecture, and health checks.
- **PMM visibility:** PMM has Redis dashboards and metrics across overview, instance, and cluster views, covering commands, clients, memory use, keyspace behavior, latency, replication health, and slowlog analysis so teams can diagnose incidents faster.

**Security, Sovereignty, and Compliance**

- **Support on customer-controlled Redis:** Encryption, access controls, and data location stay on infrastructure the customer runs. Expert Support helps with setup and incident response.
- **Clear licensing, no forced move:** Redis was not open source for several versions; Redis 8 and later provides AGPLv3 (open source) alongside RSALv2/SSPLv1 options. Teams that accept that can stay on Redis without a forced migration.

**Future readiness and portability**

- **Optional open path when the customer asks:** If governance, memory cost, or operating model push a change discussion, Percona can support a paced path to evaluate, validate, and migrate while Redis support continues.

### Sales enablement

**Elevator pitch**

Percona supports Redis for traditional key/value work with Expert Support and PMM on platform-led estates. Staying on Redis is a valid outcome. If a customer later wants an open alternative, Percona can support that transition without forcing it.

**Conversation starters**

- Who runs Redis today: platform engineering, SRE, or a database team?
- Are you embedding or redistributing Redis (product/SaaS), or is it internal-only?
- Are you on self-managed, Redis Enterprise, or a cloud managed service?
- Is Redis fine in day-to-day ops, or is the pressure from cost, governance, support coverage, or managed-service lock-in?
- What is the main pressure this quarter: RAM cost, support coverage, governance / license trust, or vendor relationship?
- Is the cache required for production? How much memory are you buying relative to the traffic it handles?
- Do you need geo-local latency across regions for cache or session workloads?
- Which Redis version are you on?
- For managed Redis or strong vendor-relationship cases, what would "good" look like if you stay on Redis with Percona Expert Support?

**Public resources**

- [Percona Support for Valkey and Redis](https://www.percona.com/valkey-redis/support/)
- [Percona Expert Consulting and Services](https://www.percona.com/services/consulting)
- [PMM Valkey and Redis monitoring](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/connect-database/valkey-redis.html)
