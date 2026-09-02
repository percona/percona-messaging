# Percona for MariaDB: Messaging

## Percona for MariaDB {#percona-for-mariadb}

For organizations running **MariaDB Server** in production, Percona helps teams get more value from that stack. That means steadier day-to-day operations, clearer cost and support boundaries, stronger performance and reliability practices, and security that fits how the estate already runs. Percona does this with **Expert Support**, **Expert Consulting and Services** for complex environments, and **Percona ExpertOps** when teams want operational ownership. Teams do not need to change platforms to start.

MariaDB Server is a strong fit when teams use what MariaDB Server already does well: Galera-style clustering they already know, **ColumnStore** for analytics next to everyday transaction work (OLTP), MariaDB backup and audit tools, **MaxScale** when it sits in the data path, and software versions that match apps already built on MariaDB Server. Many organizations run MariaDB Server **alongside** MySQL because different jobs needed different databases for real reasons.

MariaDB Server is a production path for important open source workloads. Teams need production Expert Support that is clear about MariaDB Server entitlement limits, consulting when the setup is larger or more mixed, and operators who know MariaDB-specific parts and use cases. Percona fills that gap without claiming to build MariaDB software, and without treating MariaDB Server as a short stop on the way to MySQL.

Percona does not ship MariaDB database software. Percona supports **MariaDB Server** in production with the same upstream-level engineering depth applied across MySQL, PostgreSQL, MongoDB, and Valkey. **Expert Support** covers **MariaDB Server versions only**, not MariaDB Enterprise editions under standard Support entitlements. **Expert Consulting and Services** may apply to other MariaDB versions and complex environments. See [MariaDB support](https://www.percona.com/mariadb-support/).

### Customer Challenges and Value Alignment – MariaDB

**Optimized TCO**

- **MySQL Galera Cluster end of life (adjacent estates):** What is ending is **MySQL Galera Cluster**, not Galera in MariaDB Server. MariaDB has announced 2026-09-30 as the end of life for maintenance and regular binary releases of MySQL Galera Cluster. Galera-style clustering remains available in **MariaDB Server**. For teams on MySQL Galera Cluster who want a Galera-to-Galera path on MySQL-compatible software, **Percona XtraDB Cluster** is available ([continued commitment to Percona XtraDB Cluster](https://www.percona.com/blog/continued-commitment-to-percona-xtradb-cluster/)). Teams already on MariaDB Server stay in the MariaDB Support and consulting motion above.
- **Multi-database vendor consolidation:** Teams already working with Percona for MySQL, PostgreSQL, MongoDB-compatible environments, Valkey, or Redis can add **MariaDB Server** Expert Support without a separate database vendor relationship, duplicate SLAs, or slower handoffs when incidents cross engines.

**Performance and Reliability at Scale**

- **Faster recovery when production breaks:** Percona Expert Support and ExpertOps give MariaDB Server environments 24×7 upstream-level help for incidents, upgrades, replication, and performance problems on the stack teams run today. That helps restore service and reduce repeat risk without waiting on a platform change.
- **Reliability without forced re-architecture:** Teams keep existing HA, backup, and ops patterns while Percona helps diagnose root causes, reduce repeat incidents, and harden recovery practices.
- **Workload-shaped tuning:** OLTP, analytics (including ColumnStore where in use), and clustering patterns get guidance matched to how the application actually behaves. Prefer "evaluate for the workload" over unverified head-to-head claims.
- **Keep MariaDB Server when components are load-bearing:** Keep MariaDB Server when Galera-style clustering, ColumnStore, MaxScale, MariaDB backup and audit tooling, or app assumptions built on MariaDB Server are load-bearing. Keep MySQL or Percona Server for MySQL when that stack is already the estate standard. Both can be valid; match the engine to the workload and ops constraints without ranking the engines.

**Security, Sovereignty, and Compliance**

- **Hardening on the estate in operation:** Expert Support and consulting help teams strengthen configuration, access controls, audit posture, backup encryption practices, and upgrade discipline on MariaDB Server running on customer-controlled infrastructure.
- **Clear entitlement boundaries:** MariaDB Server Support coverage is spelled out. Environments outside MariaDB Server (including Enterprise-adjacent estates) need a consulting scope so security and compliance work is not assumed under the wrong entitlement.
- **Controls matched to how MariaDB Server is run:** Focus on what the team can enforce on MariaDB Server today (process, config, patch cadence, audit retention) rather than pitching a different engine as the default compliance answer.

**Adaptability for Emerging Workloads**

- **Evolve on MariaDB Server:** Consulting and Support help teams plan upgrades, topology changes, and stronger day-to-day ops while applications remain on MariaDB Server.
- **Analytics and AI-adjacent use cases:** Some environments already use ColumnStore or are evaluating newer MariaDB Server capabilities next to OLTP. Treat fit as workload-specific; prefer "evaluate for the workload" over unverified vector or performance claims.
- **Multi-engine future without a conversion narrative:** Teams often keep MariaDB Server where it fits and run other databases elsewhere. Percona helps MariaDB Server stay healthy in that mix rather than framing every roadmap talk as a move off MariaDB Server.

### Sales enablement

**Elevator pitch**

Percona helps MariaDB Server environments run in production with Expert Support and optional ExpertOps. Consulting covers complex environments or estates outside MariaDB Server entitlements. Teams get more reliability, clarity, and operational depth on MariaDB Server, without Percona claiming to ship MariaDB software.

**Purpose**

MariaDB Server is a lasting production path, not a short stop on the way to MySQL. Teams need honest MariaDB Server Support scope, consulting when the environment is broader or outside MariaDB Server entitlements, and ExpertOps when teams want operational ownership. Percona meets those needs on MariaDB Server with clear boundaries: MariaDB Server-only Expert Support, no Percona MariaDB database software, and engine-change work only when the customer asks for a different home.

**Conversation starters**

- Are you running MariaDB Server or Enterprise in production today, and which versions matter for Support scope? (Expert Support covers MariaDB Server only; surfaces outside MariaDB Server need consulting scope so entitlements stay honest.)
- Which MariaDB Server versions are approaching or past End of Life (EOL), and do you need an upgrade plan on your timeline? (Support and consulting help plan upgrades and reduce rush risk; do not invent MariaDB ELS coverage until product publishes terms.)
- Which MariaDB-specific components are load-bearing today: Galera patterns, ColumnStore, MaxScale, backup, audit, or app assumptions built on MariaDB Server? (Stay-and-stabilize is the default when those pieces are central; MaxScale is MariaDB plc BSL middleware, so confirm it is in the path and whether consulting scope is needed; engine-change only if the customer asks.)
- Do you already buy Percona Support for other engines while MariaDB Server sits on a separate vendor relationship? (Same Support relationship and SLAs across engines without forcing one database.)
- What are the top recurring MariaDB Server incidents (replication, failover, upgrades, query regressions), and how are they handled today? (Expert Support and optional ExpertOps reduce repeat fire drills on the stack you run now.)
- If you run Galera or similar clustering, what do failover and recovery look like under real failure drills? (Harden HA and recovery practices in place; match guidance to the clustering model you already operate.)
- Are you on MySQL Galera Cluster (not Galera in MariaDB Server) with a 2026 maintenance cliff in view? (Adjacent estate only: MySQL Galera Cluster is what is ending; Galera remains in MariaDB Server. For teams who want a Galera-to-Galera path on MySQL-compatible software, PXC is available. MariaDB Server stays on the MariaDB Support and consulting motion.)
- Which audit, identity, encryption, or evidence requirements must the MariaDB Server layer meet, and who owns keys, audit retention, and patch cadence? (Harden MariaDB Server in place with clear ownership; separate Support vs consulting if versions outside MariaDB Server are in the estate.)
- Which workloads on MariaDB Server are latency-sensitive, write-heavy, or analytics-heavy (including ColumnStore where used)? (Tune and capacity-plan for how the app behaves; evaluate fit per workload rather than engine rankings.)
- What emerging work (analytics, AI-assisted features, Kubernetes ops) are you placing near MariaDB Server in the next 12 months, and what must stay true for MariaDB Server to remain the right home? (Grow on MariaDB Server with Support and consulting when MariaDB-specific pieces stay central; multi-engine estates are normal.)
- Would you rather keep day-to-day MariaDB Server operations on your team with Expert Support, or hand defined operational ownership to Percona? (ExpertOps is optional; Support alone is a complete starting point.)

**Situation talk tracks**

- **EOL upgrade planning on MariaDB Server:** Version is near or past EOL, MariaDB-specific components still matter, and the team needs an upgrade plan. Use Support and consulting; do not invent MariaDB ELS coverage until product publishes terms.
- **Unify Support across engines:** Multi-engine estate, MariaDB Server is staying, buyer wants one Support relationship and clear MariaDB Server entitlements.
- **Stabilize on MariaDB Server:** Recurring incidents or HA drill gaps are the pain; Expert Support and optional ExpertOps deepen operations without a platform change.
- **Harden MariaDB Server in place:** Audit, identity, encryption, or evidence requirements can be met on the current MariaDB Server estate with Support and consulting.
- **Multi-engine stay:** MariaDB Server keeps workloads where its components are load-bearing; MySQL or Percona Server for MySQL stays where that stack is the estate standard. No conversion narrative.

**Public resources**

- [MariaDB support](https://www.percona.com/mariadb-support/)
- [Compare MySQL, MongoDB, PostgreSQL, and MariaDB](https://www.percona.com/compare-mysql-mongodb-postgresql-mariadb)
- [Percona Expert Consulting and Services](https://www.percona.com/services/expert-consulting-and-services/)
- [Continued commitment to Percona XtraDB Cluster](https://www.percona.com/blog/continued-commitment-to-percona-xtradb-cluster/) (for MySQL Galera Cluster EOL estates who want a Galera-to-Galera path)
- [How to migrate from MariaDB to Percona Server for MySQL](https://www.percona.com/resources/how-to-migrate-from-mariadb-to-percona-server-for-mysql) (customer-requested engine change only)
- [Open source migration](https://www.percona.com/services/open-source-migration) (customer-requested engine change only)
