# Percona for Valkey: Messaging

## Percona for Valkey {#percona-for-valkey}

For platform, SRE, and DevOps teams running traditional key/value and in-memory workloads that need sub-millisecond performance, production High Availability, and open governance across on-premises, cloud, and hybrid environments, Percona helps teams run **Valkey** with Expert Support, Expert Consulting and Services, migration and readiness guidance, and PMM observability. Unlike a proprietary single-vendor key/value stack, Valkey under Linux Foundation governance and a BSD 3-Clause license gives teams a multi-vendor open path with memory-efficient operations and Percona support on infrastructure they control. Percona contributes upstream, including Valkey Technical Steering Committee leadership participation, and publishes operational packaging, but does not own the Valkey project.

Lead reasons to evaluate Valkey are memory efficiency and TCO, governance and trust, and traditional key/value workloads, with optional digital sovereignty and hybrid or multi-cloud control for teams that prefer not to lock key/value estates to a single hyperscaler managed service.

See also the [key/value overview](../messaging.md). For Redis support continuity, see [Percona for Redis](../redis/messaging.md).

### Customer Challenges and Value Alignment: Valkey

**Optimized TCO**

- **Memory savings when RAM is expensive:** In-memory workloads cost a lot because the working set lives in RAM. Valkey’s hash-table redesign shows about a 20% smaller memory footprint in customer and community evidence. That edge, plus Expert tuning of allocation, eviction, and replication, can mean smaller instances and denser cache and session estates.
- **Cost after install, not just install:** A lot of Valkey use starts in development and test, with no support relationship. Production readiness means high availability design, support SLAs, observability, and a migration rehearsal. Installing Valkey is not enough.
- **Open model without proprietary lock-in:** Valkey uses a permissive BSD 3-Clause license and open community governance. For organizations that cannot accept AGPL for legal reasons, that licensing model is often decisive. Teams leaving proprietary paid key/value products can keep performance and reliability on Percona-supported Valkey and drop proprietary subscription fees when that is the savings driver. The main reasons to evaluate Valkey remain memory efficiency, fit for traditional workloads, and multi-vendor trust.

**Performance and Reliability at Scale**

- **Traditional workloads first:** Caching, sessions, pub/sub, queues, rate limiting, and high-throughput key/value remain the default Valkey lane. On important systems, the cache is crucial for production.
- **Less load on the main database:** Valkey often sits in front of or alongside MySQL, PostgreSQL, or MongoDB-compatible systems. A well-tuned cache helps the app handle more traffic and cuts read load on those databases. That can delay expensive scale up.
- **Familiar clients and wire protocol:** The RESP wire protocol remains 100% compatible with existing clients used for this workload family. API differences are extremely minimal, and no backward-incompatible API changes have been made.
- **Migration planning when needed:** Not every Valkey deployment is a migration from another engine. When a move is in scope, version and topology determine the safest path. Percona Experts plan replication- or service-level cutovers, validate rollback, and confirm High Availability before production moves.
- **Operational tuning:** Percona Experts tune production Valkey for high availability and steady latency under load. Most platform teams do not have deep in-memory ops skills. 24×7 Expert Support and consulting cover escalation, architecture, migration, and health checks.
- **See Valkey in PMM:** PMM has Valkey dashboards and metrics across overview, instance, and cluster views, covering commands, clients, memory use, keyspace behavior, latency, replication health, and slowlog analysis so teams can diagnose incidents faster.

**Security, Sovereignty, and Compliance**

- **Governance and trust:** Valkey is community-led under the Linux Foundation. It uses a BSD 3-Clause permissive license, no contributor license agreement requirement, and an open contribution model. That multi-vendor model gives teams a clear view of project direction and lowers single-vendor control risk for key/value infrastructure.
- **Digital sovereignty, hybrid, and multi-cloud:** Teams that need self-managed, hybrid, or multi-cloud key/value, especially in the EU and other sovereignty-sensitive settings, can keep Valkey on infrastructure they control. Google offers managed Valkey. Azure does not. Percona supports the self-managed, hybrid, and multi-cloud posture when managed Valkey is missing or not enough.
- **Enterprise controls:** TLS encryption, LDAP authentication, and an audit path help organizations align with GDPR, HIPAA, and PCI-DSS requirements on customer-operated infrastructure without opaque vendor-managed layers.

**Future readiness**

- **JSON and search modules:** Valkey includes open modules for JSON and full-text workloads under the same open contribution model as core Valkey.
- **Expansion across the Percona estate:** Valkey often sits next to existing MySQL, PostgreSQL, or MongoDB work. Percona can expand across those technologies when key/value is part of a larger estate.

### Sales enablement

**Elevator pitch**

Percona helps platform and SRE teams run open Valkey for traditional key/value work with production high availability, Expert Support, and PMM. Teams get Linux Foundation governance, memory-efficient operations when RAM is expensive, and clear production readiness for greenfield Valkey and for migrations when a move is in scope.

**Purpose**

Valkey is the open, multi-vendor path for traditional key/value work. Percona adds the ops depth that makes production work: support SLAs, high availability, migration rehearsal when needed, and observability.

**Conversation starters**

- Who runs Valkey today: platform engineering, SRE, or a database team?
- Is Valkey already in production with an SLA, or only in lab / staging today? If it is not in production yet, what has to be true before it can be?
- When the cache layer fails at 2 a.m., who gets paged, and what support path exists today?
- Where does RAM cost show up in your cache or session layer today? Have you measured working-set density on Valkey versus your current engine?
- Is your cache layer a hard production dependency, and are primary databases carrying read load that better cache design could offload?
- Do AGPL constraints or open-contribution requirements matter for this estate’s legal or procurement posture?
- Are Search and JSON requirements covered by Valkey’s open modules, including full-text search?
- Do you need geo-local latency across regions for cache or session workloads, and if so, what replication and failover model is required?
- Is this greenfield Valkey, or a migration from another engine? If a move is in scope, what cutover method fits the topology?
- Are you on a managed cache service, an enterprise key/value product, self-managed Valkey, or another path today?
- Do you already use PMM or another monitoring stack for the cache layer?
- Do you already run MySQL, PostgreSQL, or MongoDB with Percona or another vendor?
- Do you need self-managed, hybrid, or multi-cloud Valkey rather than a single hyperscaler managed service?

**Public resources**

- [Percona Support for Valkey and Redis](https://www.percona.com/valkey-redis/support/)
- [Percona Expert Consulting and Services](https://www.percona.com/services/consulting)
- [PMM Valkey and Redis monitoring](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/connect-database/valkey-redis.html)
- [Valkey project leadership](https://valkey.io/leadership/)
