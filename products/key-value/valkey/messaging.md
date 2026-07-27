# Percona for Valkey: Messaging

## Percona for Valkey {#percona-for-valkey}

For platform, SRE, and DevOps teams running traditional key/value and in-memory workloads that need sub-millisecond performance, production High Availability, and open governance across on-premises, cloud, and hybrid environments, Percona helps teams run **Valkey** with Expert Support, Expert Consulting and Services, migration and readiness guidance, and PMM observability. Unlike proprietary Redis offerings or a single-vendor key/value stack, Valkey under Linux Foundation governance and a BSD 3-Clause license gives teams a multi-vendor open path with memory-efficient operations and Percona support on infrastructure they control. Percona contributes upstream and publishes operational packaging; Percona does not own the Valkey project.

Lead reasons to evaluate Valkey are memory efficiency and TCO, governance and trust, and traditional key/value workloads, with optional digital sovereignty and multi-cloud control for teams that prefer not to lock key/value estates to a single hyperscaler managed service.

See also the [key/value overview](../messaging.md). For Redis support and transition messaging, see [Percona for Redis](../redis/messaging.md).

### Customer Challenges and Value Alignment: Valkey

**Optimized TCO**

- **Memory savings when RAM is expensive:** In-memory tiers cost a lot because the working set lives in RAM. Valkey’s hash-table redesign shows about a 20% smaller memory footprint in customer and community evidence. That edge, plus Expert tuning of allocation, eviction, and replication, can mean smaller instances and denser cache and session estates.
- **Cost after install, not just install:** A lot of Valkey use starts in development and test, with no support relationship. Production readiness means high availability design, support SLAs, observability, and a migration rehearsal. Installing Valkey is not enough.
- **Open model, no proprietary subscription:** Teams leaving Redis Enterprise or other paid Redis products can keep performance and reliability on Percona-supported Valkey and drop proprietary subscription fees when that is the savings driver. After Redis returned to AGPLv3 in 2025, governance and operating cost still matter. The main reasons to evaluate Valkey remain memory efficiency, fit for traditional workloads, and multi-vendor trust.

**Performance and Reliability at Scale**

- **Traditional workloads first:** Caching, sessions, pub/sub, queues, rate limiting, and high-throughput key/value remain the default Valkey lane. These patterns work much the same on Redis. On important systems, the cache is crucial for production.
- **Less load on the main database:** Valkey often sits in front of MySQL, PostgreSQL, or MongoDB-compatible systems. A well-tuned cache helps the app handle more traffic and cuts read load on those databases. That can delay expensive scale-out.
- **Familiar protocol for Redis 7.2 and earlier:** Valkey started from the Redis 7.2 codebase. It keeps broad API and protocol compatibility for that generation, so teams can rehearse cutovers with familiar client behavior. Most client software written before 2024 still works the same at the protocol layer.
- **Migration gate (RDB/AOF):** Persistence formats split at the Redis 7.2.4 fork. Redis 7.4 and later cannot cleanly file-copy into Valkey. The clean path is a replication cutover from Redis 7.2 or earlier. Percona Experts help teams check version boundaries, rehearse cutover, and confirm high availability before production moves.
- **Operational tuning:** Percona Experts tune production Valkey for high availability and steady latency under load. Most platform teams do not have deep in-memory ops skills. 24×7 Expert Support and consulting cover escalation, architecture, migration, and health checks.
- **See Valkey in PMM:** PMM has Valkey dashboards for commands, memory, clients, latency, replication, and slowlog.

**Security, Sovereignty, and Compliance**

- **Governance and trust:** Valkey is community-led under the Linux Foundation. It uses a BSD 3-Clause license and publishes Special Interest Group (SIG) roadmaps. That multi-vendor model gives teams a clear view of the roadmap and lowers single-vendor control risk for the key/value tier.
- **Digital sovereignty and multi-cloud:** Teams that need self-managed or multi-cloud key/value, especially in the EU and other sovereignty-sensitive settings, can keep Valkey on infrastructure they control. AWS has named Percona as a partner path for ElastiCache/Valkey customers who also want self-managed or multi-cloud options. Google offers managed Valkey. Azure does not. Percona supports the self-managed and multi-cloud posture when managed Valkey is missing or not enough.
- **Enterprise controls:** TLS encryption, LDAP/SASL authentication, and an audit path help organizations align with GDPR, HIPAA, and PCI-DSS requirements on customer-operated infrastructure without opaque vendor-managed layers.


**AI and Future Readiness**
- **AI and vector readiness:** Valkey's open development model accelerates innovation, including early support for vector similarity search. Valkey introduced the open source valkey-search module in 2024, supporting vector similarity search and other AI-driven workloads on top of the Valkey 7.2 codebase.
- **Expansion across the Percona estate:** Valkey often sits next to existing MySQL, PostgreSQL, or MongoDB work. Percona can expand across those technologies when key/value is part of a larger estate.

### Sales enablement

**Elevator pitch**

Percona helps platform and SRE teams run open Valkey for traditional key/value work with production high availability, Expert Support, and PMM. Teams get Linux Foundation governance, memory-efficient operations when RAM is expensive, and a clear migration path from Redis 7.2 and earlier when they choose to move.

**Purpose**

Valkey is the open, multi-vendor path for traditional key/value work. Percona adds the ops depth that makes production work: support SLAs, high availability, migration rehearsal, and observability.

**Conversation starters**

- Who runs Valkey today: platform engineering, SRE, or a database team?
- Is Valkey in production with an SLA, or only in lab / staging today? If it is not in production yet, what has to be true before it can be?
- When Valkey or Redis fails at 2 a.m., who gets paged, and what support path exists today?
- Where does RAM cost show up in your cache or session tier today? Have you measured working-set density on Valkey versus your current engine?
- Is your cache tier a hard production dependency, and are primary databases carrying read load that better cache design could offload?
- Do you need Linux Foundation multi-vendor governance and BSD licensing for the key/value tier?
- Are Search, JSON, or active-active geo hard requirements, or is the workload in the traditional cache and session lane?
- Which Redis major or minor are you on today? (Replication cutover from Redis 7.2 or earlier is the clean Valkey path; Redis 7.4+ is not a clean file-copy migrate.)
- Are you on ElastiCache, Memorystore, Azure Cache, Redis Enterprise, or self-managed?
- Do you already use PMM or another monitoring stack for the cache tier?
- Do you already run MySQL, PostgreSQL, or MongoDB with Percona or another vendor?
- Do you need self-managed or multi-cloud Valkey rather than a single hyperscaler managed service?

**Public resources**

- [Percona Support for Valkey and Redis](https://www.percona.com/valkey-redis/support/)
- [Percona Expert Consulting and Services](https://www.percona.com/services/consulting)
- [PMM Valkey and Redis monitoring](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/connect-database/valkey-redis.html)
