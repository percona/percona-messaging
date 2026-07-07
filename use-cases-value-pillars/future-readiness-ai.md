# Future Readiness (AI, Emerging Workloads)

As AI, real-time analytics, and hybrid data pipelines reshape enterprise workloads, most organizations face a familiar tension: adopt faster, or lose control. [According to IDC](https://my.idc.com/getdoc.jsp?containerId=prAP53268725), 75% of enterprise AI workloads will be deployed on hybrid fit-for-purpose infrastructure by 2027, yet many are locked into proprietary ecosystems that tie "AI enablement" to license upgrades or vendor-specific APIs.

Percona's open source foundation and consistent operational model give customers freedom to evolve. From AI pipelines to vector search and hybrid-cloud deployments, Percona helps teams adopt emerging workloads securely, efficiently, and without losing architectural independence.

### The Problem: Innovation Trapped by Proprietary Design

AI, ML, and real-time analytics depend on data mobility and trust, but current database ecosystems often limit both. Proprietary vendors package "AI readiness" behind gated features or closed infrastructure, fragmenting governance and inflating costs.

- **Feature lock-in:** Capabilities like vector search, model inference, or embeddings are increasingly tied to enterprise SKUs, forcing migrations or premium pricing. [Vector databases](https://en.wikipedia.org/wiki/Vector_database) (engines for embeddings and similarity search) now span many vendors and packaging models, so buyers should weigh architectural fit and lock-in, not feature checklists alone.
- **RAG on databases teams already run:** Retrieval-augmented generation grounds LLM outputs in proprietary data at inference time. [Stack Overflow Developer Survey 2025](https://survey.stackoverflow.co/2025/technology#1-databases) reports PostgreSQL at 55.6% developer adoption, so many teams add RAG on PostgreSQL they already operate instead of procuring a separate vector database product.
- **Fragmented data architectures:** AI pipelines must bridge structured (SQL) and unstructured (NoSQL, key-value, or document) data ([IDC](https://www.netapp.com/media/110879-idc-workload-impacts-storage-info-brief.pdf)). Maintaining separate engines for training, inference, and analytics increases latency and operational complexity.
- **Compliance drag:** Using regulated or customer data in AI training pipelines adds exposure if encryption, audit trails, and access policies differ across environments. 70% of organizations report data-governance difficulties in their AI efforts ([McKinsey](https://www.mckinsey.de/capabilities/quantumblack/our-insights/the-state-of-ai-2024)).
- **Unpredictable scaling costs:** Elastic AI workloads spike compute and storage demand, and per-core or per-query pricing models compound waste. [Deloitte](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/ai-infrastructure-compute-strategy.html) reports many organizations reevaluate cloud API and inference spend when cloud costs approach 60% to 70% of equivalent on-premises hardware for steady-state workloads.
- **Operational silos:** Specialized AI databases create skills gaps, slowing deployment and increasing dependency on vendor-specific expertise.
- **Spend concentrates on AI-ready platforms:** By **2028**, [Gartner expects **80%** of GenAI business applications to be developed on **existing data management platforms**](https://www.gartner.com/en/newsroom/press-releases/2025-06-02-gartner-predicts-by-2028-80-percent-of-genai-business-apps-will-be-developed-on-existing-data-management-platforms). Enterprises reduce duplicate tooling and governance overhead when they plan vector retrieval, security, and lifecycle operations on standardized database estates instead of expanding parallel niche engines.

### The Solution: Open Infrastructure for AI Evolution

Percona enables AI, vector search, and hybrid data workloads through open, secure, and portable database architectures. Customers can modernize existing systems for emerging workloads without replatforming or lock-in.

- **AI-ready databases:** Vector and retrieval support differs by engine.
  - **PostgreSQL:** Percona packages [pgvector](https://www.percona.com/blog/pgvector-the-critical-postgresql-component-for-your-enterprise-ai-strategy/) alongside other tested distribution components ([third-party components](https://docs.percona.com/postgresql/18/third-party.html)). Percona Expert Support includes advisory guidance for pgvector and pgvectorscale production tuning. Percona focuses on PostgreSQL performance, scalability, and security for vector workloads, not embedding-model or LLM application design. pgvectorscale is not packaged in Percona Distribution for PostgreSQL.
  - **MySQL (self-managed):** Percona is adding `VECTOR_DISTANCE()` to Percona Server for MySQL and Percona XtraDB Cluster as a Tech Preview (8.4.11 / 9.7.2 est.). Indexing and full vector search are planned for a later release.
  - **Valkey:** Valkey includes the open source valkey-search module for vector similarity search. Percona Expert Support and PMM cover Valkey and Redis in customer-controlled deployments.
- **Hybrid and multi-cloud flexibility:** Percona Operators orchestrate consistent deployments across on-prem and cloud clusters, enabling AI pipelines to train or infer near the data source while maintaining governance.
- **Data integrity and compliance:** Encryption, RBAC, and transparent audit logs preserve control over sensitive data used in AI training, supporting GDPR, HIPAA, and ISO 27001 alignment.
- **Predictable performance and cost:** ExpertOps tuning and rightsized infrastructure optimize indexing, caching, and query execution for AI workloads.
- **Guardrails that scale with the stack:** PMM supports custom Percona Advisor checks so organizations can extend bundled Security, Configuration, Performance, and Query coverage when new services, engines, or internal policies appear, keeping operational standards aligned with hybrid and polyglot data architectures.

### Use cases

- **RAG on PostgreSQL:** Grounding LLM answers in proprietary relational data often means a second database contract and a second ops boundary for embeddings. Percona supports retrieval on PostgreSQL teams already run, with Expert Support for database-layer tuning.
- **Self-managed MySQL without managed vector:** Teams running MySQL on their own infrastructure cannot use HeatWave or MySQL AI and may not want a separate vector database yet. Percona lets them test vector-related SQL on that MySQL estate before they lock in architecture.
- **MySQL with a separate vector store:** Pairing MySQL with a standalone vector database adds two backup models, two access-control stacks, and sync work between transactional and retrieval data. Percona's roadmap targets vector search on self-managed MySQL so teams can plan one database instead of two.
- **Similarity lookup next to transactional data:** Search and recommendation features need fast vector lookup beside relational or document stores. Teams want that layer under the same Percona support and PMM coverage as their primary databases, not a separate vendor relationship.
