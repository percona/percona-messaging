# Percona Kubernetes Operators: Messaging

## Operate and Observe {#operate-and-observe}

As organizations move stateful databases into Kubernetes and hybrid-cloud environments, the challenge shifts from simply running systems to observing and operating them efficiently and in real time. Percona's open source operations stack unifies automation and observability across MySQL, PostgreSQL, and MongoDB clusters, reducing hands-on overhead and eliminating vendor lock-in.

Percona Operators define database clusters as Kubernetes Custom Resources (CRDs), automating common Day-1 and Day-2 operations (like deployment, scaling, backups, and failover) with declarative precision. After establishing a production foundation, the next challenge is operational scale and visibility. Percona Monitoring and Management (PMM) extends that automation with database-native observability, surfacing query analytics, system metrics, and performance trends through integrated Prometheus and Grafana dashboards.

Together, these components deliver a transparent, cloud-neutral operations layer that complements Percona's production-hardened databases, completing the lifecycle from run to optimize.

---

## Percona Kubernetes Operators (MySQL, PostgreSQL, MongoDB) {#percona-kubernetes-operators}

For engineering organizations managing stateful workloads across Kubernetes and hybrid infrastructures, Percona Kubernetes Operators provide a production-grade automation framework built for consistency and control. According to the Data on Kubernetes 2024 survey, databases remain the most common workload running on Kubernetes for the third year in a row. In Data on Kubernetes 2021 survey, operators were cited as the key automation mechanism for hybrid and multi-cloud deployments. Each Operator defines MySQL, PostgreSQL, and MongoDB clusters as Kubernetes Custom Resources (CRDs), integrating lifecycle management (provisioning, scaling, upgrades, backups, and failover) into the same declarative model developers already use for application workloads.

Unlike proprietary DBaaS platforms that hide configuration behind managed abstractions, Percona's Operators preserve transparency, portability, and governance. Civo, a cloud-native provider, launched its DBaaS using the Percona Operator for MySQL rather than developing its own, accelerating time-to-market and cutting engineering overhead while maintaining open source flexibility. The result is deterministic operations, predictable performance, and full sovereignty over database environments across any cloud or on-prem infrastructure.

**Optimized TCO**

- Operational efficiency through automation: Managing database clusters manually in Kubernetes often consumes excessive engineering hours for deployment, scaling, and failover management. Percona Operators automate operations like backups, upgrades, and recovery through declarative Kubernetes Custom Resources (CRDs). This ensures every operation follows a consistent, version-controlled process, reducing manual error and stabilizing lifecycle costs. A 2024 DoK survey found that organizations running 75%+ of their data workloads in production on Kubernetes reported significant productivity gains when using operators.
- Freedom from DBaaS markup: Proprietary managed services like RDS or Atlas add convenience but impose per-instance fees and license gating. With Percona Operators, organizations can deploy production-grade databases on any Kubernetes environment, maintaining automation benefits without recurring license or subscription costs.

**Performance and Reliability at Scale**

- Predictable high availability: Each Operator embeds replication and failover logic tuned to its database engine: synchronous, multi-master replication via Percona XtraDB Cluster (PXC) for MySQL, Patroni-coordinated failover for PostgreSQL, and replica set automation for MongoDB. Rolling upgrades and automated node recovery preserve uptime during maintenance and scaling, keeping applications online through node failures, upgrades, and peak traffic without manual intervention.
- Elastic scaling without disruption: Operators dynamically scale clusters using Kubernetes StatefulSets and engine-specific replication, so workloads grow or contract automatically without risking downtime, data loss, or emergency reconfiguration. Starting with Operator for MongoDB 1.22.0, automatic PVC resizing based on usage thresholds prevents disk-full outages without manual intervention.
- Service mesh compatibility: Operators support the Kubernetes `appProtocol` field (e.g., `appProtocol: mongo`), enabling correct traffic recognition in service meshes like Istio. This ensures reliable cluster formation and secure mTLS connections in enterprise Kubernetes environments without manual configuration. *(Added in Operator for MongoDB 1.22.0.)*

**Security, Sovereignty and Compliance**

- Unified and auditable policy automation: Percona Operators enforce consistent encryption, access, and backup policies across all clusters, with configurations stored as declarative code in Kubernetes CRDs, so security and compliance controls stay aligned across environments and can be proven during audits. This supports GitOps workflows, version control, and full auditability across hybrid and regulated environments while preventing configuration drift. Industry analysis of persistent data on Kubernetes notes that configuration drift and lack of standardization remain significant barriers to production scaling of stateful workloads.
- HashiCorp Vault integration: The Operator for MongoDB (1.22.0+) integrates with HashiCorp Vault for system user credential management. The Operator authenticates to Vault (via Kubernetes auth or token), retrieves passwords during cluster creation, and periodically syncs changes. This enables centralized credential governance, auditable password rotation, and separation of duties between DBA and security teams.
- Consistent governance across clouds: Operators use open Kubernetes APIs and RBAC integration for centralized policy enforcement, giving organizations confidence that compliance frameworks such as GDPR, HIPAA, and PCI-DSS are applied uniformly, regardless of where data resides.

**Adaptability for Emerging Workloads**

- Multi-cloud and hybrid portability: Percona Operators run on any CNCF-conformant Kubernetes, including OpenShift, Amazon EKS, Google GKE, Azure AKS, and on-prem clusters. Teams can move workloads freely without rewriting automation or getting trapped by a single cloud vendor.
- MySQL operator path and current release context: Percona maintains separate operator lines for Percona XtraDB Cluster (mature production HA focus, including fixes such as the ProxySQL cross-site crash-loop scenario in 1.19.1) and Percona Server for MySQL (production-grade automation on Kubernetes, with PITR and incremental backups in technical preview in releases such as 1.1.0).
- Integration with cloud-native toolchains: Operators expose APIs for CI/CD pipelines and policy engines, with support for Prometheus, Grafana, and PMM (Percona Monitoring and Management), so database operations fit naturally into platform engineering workflows and support rapid, reliable delivery. A dedicated CRD Helm chart (Operator for MongoDB 1.22.0+) improves compatibility with GitOps tools like ArgoCD and FluxCD by letting Helm manage all resources, including CRDs.
