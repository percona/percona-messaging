# Security Assessment

**Fixed-fee SKU:** CONS-SECFF  
**Starting from:** $6,800

Database security gaps rarely come from exotic attacks; they come from drift. An account that kept its privileges after the project ended, a default nobody hardened, a patch that is still in the backlog. This assessment reviews your configuration, access controls, and operational practices against the specific requirements you are accountable for, whether that is PCI-DSS, HIPAA, or your own internal policy, and gives you a prioritized list of what to fix first.

This is one packaged fixed-fee scope under [Expert Consulting and Services](../messaging.md), not the full Consulting catalog. Multi-environment estates, remediation programs, and security work outside this assessment gate are scoped as custom consulting instead.

## FAQ

### Will this make us compliant?

No, and you should be wary of anyone who promises it will. Compliance is your responsibility; what we do is tell you exactly where the gaps are against the requirements you name, and what to fix first. Every finding in the report maps to the specific requirement it addresses rather than a generic severity label.

### Which requirements can you assess against?

The ones you are actually on the hook for. At kickoff we run a discovery session on your security requirements and compliance obligations, whether that is HIPAA, PCI-DSS, or your own internal policy, and the review is built against those. It is not a one-size template with your logo on it.

### What gets reviewed?

Configuration, authentication, connection, and replication security, including PMM Advisor checks for known CVEs. Password management, database-user security, and privilege grants, including over-permissioned and stale accounts. Patch management and network security. And your operational layer: backup and disaster recovery practices, encryption at rest, monitoring and logging, and vendor security considerations. Engine-specific exposure is covered too, like inter-node traffic encryption on Galera clusters or ACL command restrictions on Valkey and Redis.

### What is the scope of the fixed fee?

A single database environment or cluster deployment, regardless of the number of nodes it contains: one MySQL setup, one Galera cluster, one PostgreSQL deployment, one MongoDB replica set or sharded cluster, or one Valkey or Redis cluster or replica set.

### What do we get at the end?

A PDF report with findings and recommendations, 5–7 business days after kickoff, followed by a live rundown with open Q&A. You leave the rundown with a prioritized list your team can act on immediately.

### Will you fix what you find?

Implementation is available as a separate add-on after the assessment; depending on the complexity of the changes, that may need an amendment or a new statement of work. The report itself is written so your own team can act on it without us.

## Engine variants

Source files are split by engine so tech owners can review only their variant. On the Docsify site, those variants render in full below. On GitHub, open the linked file.

| Engine | Source file |
| --- | --- |
| MySQL | [MySQL](mysql.md) |
| MariaDB Server | [MariaDB Server](mariadb.md) |
| PostgreSQL | [PostgreSQL](postgresql.md) |
| MongoDB | [MongoDB](mongodb.md) |
| Valkey / Redis | [Valkey / Redis](valkey-redis.md) |

<!-- docsify assemble: full package page for readers -->

[MySQL](/offerings/expert-consulting/security-assessment/mysql.md ':include')

[MariaDB Server](/offerings/expert-consulting/security-assessment/mariadb.md ':include')

[PostgreSQL](/offerings/expert-consulting/security-assessment/postgresql.md ':include')

[MongoDB](/offerings/expert-consulting/security-assessment/mongodb.md ':include')

[Valkey / Redis](/offerings/expert-consulting/security-assessment/valkey-redis.md ':include')
