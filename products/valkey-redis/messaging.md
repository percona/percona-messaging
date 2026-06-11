# Percona for Valkey and Redis: Messaging

## Percona for Valkey and Redis {#percona-for-valkey-and-redis}

For platform, SRE, and DevOps teams operating Redis-compatible in-memory key/value workloads, predominantly caching layers that hold a small, frequently or critically used data subset and need low latency and high throughput, Percona provides enterprise-grade performance, security, and lifecycle assurance for both Redis and Valkey with open source freedom across on-prem, cloud, and hybrid environments, without proprietary lock-in or loss of continuity. Unlike MySQL, PostgreSQL, and MongoDB systems Percona supports, these clusters are rarely managed by traditional DBAs.

Since Valkey's creation in March 2024 as a BSD-licensed fork under the Linux Foundation, Percona engineers have been active contributors and maintainers in key areas like replication and memory management. Valkey and Redis share a common protocol and remain highly interchangeable for most client software written before 2024. Percona gives organizations flexibility to maintain current deployments while optionally transitioning to open source Valkey, backed by 24×7 Expert Support, Percona Expert Consulting and Services for architecture and design, migration, and health assessments, and PMM observability support.

Percona's approach is explicitly customer-first. We provide individualized guidance on whether to remain on Redis, transition to Valkey, or adopt a hybrid posture, based entirely on each customer's stability, cost, and compliance requirements. Percona supports both Redis and Valkey so customers can choose the right path for their environment, risk profile, and timeline. We help teams maintain current Redis workloads, evaluate Valkey where open governance and licensing clarity matter, and transition incrementally when that creates clear operational or cost benefits.

### Customer Challenges and Value Alignment: Valkey/Redis

**Optimized TCO**

- Business continuity and cost predictability: Percona supports both Redis and Valkey so teams can preserve continuity while choosing the right operating model over time. Valkey originated from the Redis 7.2 codebase and preserves the same protocol, RDB snapshot, and AOF persistence formats, allowing drop-in compatibility for most Redis 7.2 deployments. Percona's dual-support model helps reduce migration friction while preserving predictable costs and long-term freedom without license risk, vendor dependency, or forced upgrades.
- Memory-driven infrastructure spend: Valkey and Redis are among the most expensive databases in common use from an infrastructure perspective because full datasets live in memory. Percona Experts tune memory allocation, eviction policies, and replication topology so teams deliver the same performance on less infrastructure without sacrificing latency targets.
- Eliminating licensing fees: Organizations running Redis Enterprise can reduce operational costs depending on need by transitioning to Percona-supported Valkey, retaining performance and reliability while eliminating proprietary subscription fees.

**Performance and Reliability at Scale**

- Caching as operational infrastructure: On critical workloads, the cache tier is an operational requirement, not an optional accelerator. Teams need Valkey and Redis available, correctly sized, and tunable under load because cache failures and memory pressure hit latency and throughput before primary databases show stress.
- Predictable performance: Valkey maintains broad API and protocol compatibility with Redis 7.2, ensuring seamless workload migration and interoperability. Linux Foundation benchmark results (Oct 2025) reported up to 40% higher application throughput with Valkey 9.0 compared to 8.1, extending earlier AWS performance testing findings that Valkey 7.2 achieved equal or slightly higher throughput than Redis 7.1 in Elasticache under identical workloads.
- Operational tuning and services split guardrails: Percona Experts apply advanced tuning (memory allocation, connection pooling, replication configuration) to optimize latency and consistent performance under heavy concurrency. Production deployments are usually caching tiers in front of MySQL, PostgreSQL, or MongoDB systems; applications can serve requests from cache without round-tripping to those stores, raising throughput while well-tuned caches reduce read pressure and defer costly scale-out. Deep in-memory operations expertise is uncommon on platform teams, so Percona Expert Support covers 24×7 escalation with operational and development experience at any scale, while Expert Consulting and Services handles architecture and design reviews, migration projects, and structured health assessments, with advisory guidance on when to keep Redis, move to Valkey, or run both in parallel.
- Security controls and throughput efficiency: Valkey 9.0 includes SAFE, LDAP integration, TLS certificate authentication, and AVX512-oriented performance optimizations. Together, these capabilities improve deployment consistency, strengthen enterprise access controls, and increase throughput efficiency for compute-intensive in-memory workloads.
- PMM visibility scope: PMM provides dedicated Valkey and Redis dashboards for commands, memory, clients, latency, replication, and slowlog (Source: [https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/connect-database/valkey-redis.html](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/connect-database/valkey-redis.html); Date: 2026-04-27). QAN stored metrics remain scoped to MySQL, PostgreSQL, and MongoDB (Source: [https://docs.percona.com/percona-monitoring-and-management/3/use/qan/QAN-stored-metrics.html](https://docs.percona.com/percona-monitoring-and-management/3/use/qan/QAN-stored-metrics.html); Date: 2026-04-27). This gives teams full PMM dashboard visibility for Valkey and Redis operations while keeping a clear engine boundary for QAN.

**Security, Sovereignty, and Compliance**

- Governance transparency: Redis 7.4–7.9 remain source-available, following Redis's open source licensing history prior to 7.4; Redis 8+ introduces AGPLv3, an open source license, alongside RSALv2/SSPLv1. Valkey, launched under and governed by the Linux Foundation, continues under the BSD 3-Clause license. Valkey 9 advances that model with a formal, predictable release cadence and Special Interest Groups (SIGs) that maintain public, community-driven roadmaps. Percona supports both Redis and Valkey, offering customers verifiable transparency, configuration control, and a no-lock-in path toward an open future.
- Enterprise controls: Valkey supports TLS encryption, LDAP/SASL authentication, and auditable access patterns that help organizations align with GDPR, HIPAA, and PCI-DSS requirements. Customers can enforce consistent encryption and access standards across hybrid and multi-cloud architectures, improving data sovereignty and regulatory readiness without opaque vendor-managed layers.

**Adaptability for Emerging Workloads**

- AI and vector readiness: Valkey's open development model accelerates innovation, including early support for vector similarity search. Valkey introduced the open source valkey-search module in 2024, supporting vector similarity search and other AI-driven workloads on top of the Valkey 7.2 codebase.
- Hybrid and multi-cloud flexibility: With PMM observability and Kubernetes integration, Percona helps customers operate Redis and Valkey clusters across clouds while preserving visibility, governance, and cost control.
- Future freedom: By supporting both ecosystems in parallel, Percona gives customers a choice-driven path: stay on Redis with support continuity, or migrate to Valkey when ready, without disruption or forced upgrades. Redis and Valkey are highly adopted across the industry, whether teams adopt through packaged integrations or custom applications that embed them deeply. Percona's collaboration within the Valkey community ensures stable performance and validated integration for emerging workloads.

### Sales enablement

**Conversation starters**

- Who operates Valkey or Redis in your organization: platform engineering, SRE, or a database team? (Unlike other engines Percona supports, DBAs rarely own these clusters; Percona aligns escalation and consulting to platform-led operations.)
- Is your cache tier a hard production dependency, not an optional accelerator? (Expert Support provides 24×7 escalation when cache outages would hit latency or availability directly.)
- Are MySQL, PostgreSQL, or MongoDB instances carrying read load that better cache design could offload? (Tuned Valkey and Redis deployments can extend headroom on primary data stores.)
- How much memory are you provisioning for Valkey or Redis relative to the throughput you need? (Expert tuning often rightsizes clusters without sacrificing latency targets.)
- Are you weighing Valkey against Redis, or planning to stay on Redis? (Percona supports both and helps teams choose based on stability, cost, and compliance requirements.)

**Public resources**

- [Percona Support for Valkey and Redis](https://www.percona.com/valkey-redis/support/)
- [Percona Expert Consulting and Services](https://www.percona.com/services/consulting)
- [PMM Valkey and Redis monitoring](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/connect-database/valkey-redis.html)
