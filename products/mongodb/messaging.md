# Percona for MongoDB: Messaging

## Percona for MongoDB {#percona-for-mongodb}

For organizations running MongoDB workloads requiring performance, reliability, security, sovereignty, and compliance across on-premises, cloud, and hybrid environments, Percona Server for MongoDB provides a production-tested, self-managed platform that extends MongoDB Community Edition with enterprise-grade capabilities.

MongoDB Community Edition is licensed under the Server Side Public License (SSPL) (source-available), and Percona Server for MongoDB inherits this license for the database server. However, Percona-developed technologies and management components around the database, including Percona Backup for MongoDB, Percona ClusterSync for MongoDB, and Percona Operator for MongoDB, are released under the Apache 2.0 open source license. This keeps the operations stack auditable and portable while maintaining compatibility with MongoDB APIs and database clients.

Compared with MongoDB Enterprise Advanced or Atlas, Percona focuses on self-managed deployments backed by Percona's operational tooling and 24×7 support—without requiring Atlas-only integrations for core day‑2 operations (monitoring, backups, automation).

MongoDB's Vector Search and Full-Text Search capabilities are powered by `mongot`, a separate JVM-based service integrated into MongoDB's indexing and query workflows. With upstream Vector Search now source-available under SSPL and in public preview for community usage, Percona's plan is to validate and publish early builds (8.3 as a learning vehicle), then ship a fully integrated, observable experience (Operator + PMM dashboards/metrics, plus operational guidance) aligned to MongoDB 9.0 GA timing (estimated Sep/Oct 2026). Until then, treat Vector Search as Public Preview.

### Customer Challenges and Value Alignment – MongoDB

**Optimized TCO**

- High licensing costs and vendor lock-in: MongoDB Enterprise Advanced and Atlas introduce restrictive licensing and escalating subscription fees. Percona Server for MongoDB removes license cost while retaining major enterprise features, cutting total database spend by up to 50%. BBVA (global bank) chose Percona for its MongoDB workload migration to avoid license costs.

**Performance and Reliability at Scale**

- Operational complexity: Scaling and maintaining HA/DR clusters consumes significant DBA effort. Percona Server for MongoDB includes in-memory storage engine support and file copy-based initial sync, reducing recovery times and operational overhead. The Percona Kubernetes Operator for MongoDB and Percona Backup for MongoDB automate deployment, backups, and failover, while ExpertOps ensures predictable uptime and capacity planning. PBM 2.13.0 (Mar 2026) adds GCS authentication via Workload Identity Federation (eliminating long-lived service account keys), selective backups that include users and roles, storage profile targeting for multi-storage environments, and uninterrupted PITR when running logical backups on external storage profiles.
- Lower migration effort and risk: Percona ClusterSync helps teams migrate to Percona Server for MongoDB by automating data sync and coordinating a controlled cutover. This reduces the downtime window, the manual sequencing work, and the operational risk that can make MongoDB migrations risky and resource intensive. Key capabilities demonstrated at Feb 2026 ACC: near-zero downtime migration between clusters, hybrid cloud deployments, and filtered sync. Roadmap includes replication performance improvements, support for uneven MongoDB versions, and multi-instance support.

**Security, Sovereignty, and Compliance**

- Encrypted open source: Community builds lack enterprise controls for regulated industries. Percona Server for MongoDB includes transparent data-at-rest encryption with external key management (KMIP-compatible providers, HashiCorp Vault, OpenBao), advanced authentication and authorization integrations (LDAP/AD, Kerberos, OpenID Connect, AWS IAM), FIPS 140-2–validated cryptographic mode, auditing, and log redaction to support GDPR, HIPAA, and PCI-DSS requirements.

**Adaptability for Emerging Workloads**

- Multi-environment operations: The Percona Operator for MongoDB automates provisioning and scaling across Kubernetes and multi-cloud environments, while PMM provides cross-cluster observability and performance analytics. Minsait migrated tier-one telecom workloads to MongoDB on Google Cloud using the Percona Operator, achieving significant cost savings and operational freedom across Kubernetes environments. Operator 1.22.0 (Feb 2026) adds service mesh compatibility (Istio), automatic PVC resizing, Vault credential management, restore across different replica set names, native MinIO backup support, and GitOps-friendly CRD Helm chart.
- Vector and full-text search readiness: Percona is preparing a MongoDB Vector Search stack based on upstream `mongot`, focused on packaging, orchestration, and observability for self-managed deployments (aligned to MongoDB 9.0 GA timing).
