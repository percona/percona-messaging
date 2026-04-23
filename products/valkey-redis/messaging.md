# Percona for Valkey and Redis: Messaging

## Percona for Valkey and Redis {#percona-for-valkey-and-redis}

For organizations operating Redis-compatible in-memory workloads requiring sub-millisecond performance, scalability, and open source freedom across on-prem, cloud, and hybrid environments, Percona provides enterprise-grade performance, security, and lifecycle assurance for both Redis and Valkey, without proprietary lock-in or loss of continuity.

Since Valkey's creation in March 2024 as a BSD-licensed fork under the Linux Foundation, Percona engineers have been active contributors and maintainers in key areas like replication and memory management. Percona gives organizations flexibility to maintain current deployments while optionally transitioning to open source Valkey, backed by 24×7 support and PMM observability.

Percona's approach is explicitly customer-first. We provide individualized guidance on whether to remain on Redis, transition to Valkey, or adopt a hybrid posture, based entirely on each customer's stability, cost, and compliance requirements.

### Customer Challenges and Value Alignment – Valkey/Redis

**Optimized TCO**
- Business continuity and cost predictability: Percona ensures continuity by supporting both Redis and Valkey. Customers can maintain existing Redis environments and migrate to Valkey at their own pace with Percona's expert planning and zero-downtime execution. Valkey originated from the Redis 7.2 codebase and preserves the same protocol, RDB snapshot, and AOF persistence formats, allowing drop-in compatibility for most Redis 7.2 deployments. Percona's dual-support model delivers predictable costs and long-term freedom without license risk, vendor dependency, or forced upgrades.
- Eliminating licensing fees: Organizations running Redis Enterprise can reduce operational costs depending on need by transitioning to Percona-supported Valkey, retaining performance and reliability while eliminating proprietary subscription fees.

**Performance and Reliability at Scale**
- Predictable performance: Valkey maintains broad API and protocol compatibility with Redis 7.2, ensuring seamless workload migration and interoperability. Linux Foundation benchmark results (Oct 2025) reported up to 40% higher application throughput with Valkey 9.0 compared to 8.1, extending earlier AWS performance testing findings that Valkey 7.2 achieved equal or slightly higher throughput than Redis 7.1 in Elasticache under identical workloads.
- Operational tuning: Percona Experts apply advanced tuning (memory allocation, connection pooling, replication configuration) to optimize latency and consistent performance under heavy concurrency.

**Security, Sovereignty, and Compliance**
- Governance transparency: Redis 7.4–7.9 remain source-available, following Redis's open source licensing history prior to 7.4; Redis 8+ introduces AGPLv3, an open source license, alongside RSALv2/SSPLv1. Valkey, launched under and governed by the Linux Foundation, continues under the BSD 3-Clause license. Valkey 9 advances that model with a formal, predictable release cadence and Special Interest Groups (SIGs) that maintain public, community-driven roadmaps. Percona supports both Redis and Valkey, offering customers verifiable transparency, configuration control, and a no-lock-in path toward an open future.
- Enterprise controls: Percona extends its managed security framework with TLS encryption, LDAP/SASL authentication, and auditing policies to Valkey deployments for alignment with GDPR, HIPAA, and PCI-DSS. Customers can enforce consistent encryption and access standards across hybrid and multi-cloud architectures, ensuring data sovereignty and regulatory readiness without relying on opaque vendor-managed layers.

**Adaptability for Emerging Workloads**
- AI and vector readiness: Valkey's open development model accelerates innovation, including early support for vector similarity search. Valkey introduced the open source valkey-search module in 2024, supporting vector similarity search and other AI-driven workloads on top of the Valkey 7.2 codebase.
- Hybrid and multi-cloud flexibility: With PMM observability and Kubernetes integration, Percona helps customers operate Redis and Valkey clusters across clouds while preserving visibility, governance, and cost control.
- Future freedom: By supporting both ecosystems in parallel, Percona gives customers a choice-driven path: stay on Redis with support continuity, or migrate to Valkey when ready, without disruption or forced upgrades. Percona's collaboration within the Valkey community ensures stable performance and validated integration for emerging workloads.
