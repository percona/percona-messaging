# Security Assessment

**Fixed-fee SKU:** CONS-SECFF  
**Starting from:** $6,800

Database security gaps rarely come from exotic attacks; they typically come from vulnerability drift. An account that kept its privileges after the project ended, a default nobody hardened, a patch that is still in the backlog. This assessment reviews your configuration, access controls, and operational practices against the specific requirements you are accountable for, whether that is PCI-DSS, HIPAA, or your own internal policy, and gives you a prioritized list of what to fix first.

This is one packaged fixed-fee scope under [Expert Consulting and Services](messaging.md), not the full Consulting catalog. Multi-environment estates, remediation programs, and security work outside this assessment gate are scoped as custom consulting instead.

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

## MySQL Security Assessment

A comprehensive review of your MySQL environment's security posture against the requirements you are actually accountable for: HIPAA, PCI-DSS, or your own internal policy. We cannot guarantee your compliance; that is your responsibility, but we can tell you exactly where the gaps are and what to fix first.

We review your configuration, access controls, and operational practices against the specific requirements you name at kickoff, not a generic compliance template.

### Deliverables

- Discovery session reviewing your specific security requirements and compliance obligations
- Percona Monitoring and Management Advisor configuration with a focused walkthrough of CVE, configuration, authentication, connection, and replication security checks
- Audit of password management and validation, database-user security, patch management, and network security
- Review of privilege grants for over-permissioned accounts and unused or stale user access
- Review of backup and disaster recovery practices, encryption at rest, monitoring and logging, and vendor security considerations
- PDF report with findings and recommendations, delivered 5–7 business days after kickoff
- Live rundown session with open Q&A

### Who it is for

Scoped to a single MySQL deployment (standalone, source-replica, Percona XtraDB Cluster, Group Replication cluster). If implementation of the recommendations is needed afterward, that is available as a separate add-on; an amendment or new SOW may be required depending on the complexity of the change.

### Outcome

A specific list of what is exposed in your MySQL configuration and what to fix first, not a checkbox compliance letter that reads the same for every customer. You will know exactly which gaps map to your actual compliance requirement, and which user accounts have more privilege than your policy actually allows.

**CTA:** Pressure test your MySQL security before an auditor does.

## MariaDB Community Security Assessment

A full review of your MariaDB Community deployment's security configuration, including the Galera-specific exposure (if applicable) that most generic security scans miss entirely, such as inter-node traffic encryption and SST/IST transfer security.

We review your configuration and access controls against the specific compliance requirements you name at kickoff. A cluster is only as secure as its weakest node, so this review treats the cluster as the unit of assessment rather than individual nodes in isolation. Percona supports MariaDB Community versions; Enterprise editions are out of scope.

### Deliverables

- Discovery session reviewing your specific security requirements and compliance obligations
- PMM Advisor configuration with a focused walkthrough of CVE, configuration, authentication, connection, and replication security checks
- Audit of password management and validation, database-user security, patch management, and network security
- Review of inter-node encryption (TLS for wsrep traffic) and SST/IST transfer method security
- Review of backup and disaster recovery practices, encryption at rest, monitoring and logging, and vendor security considerations
- PDF report with findings and recommendations, delivered 5–7 business days after kickoff
- Live rundown session with open Q&A

### Who it is for

Scoped to a single MariaDB Community deployment, including Galera Cluster. Implementation of recommendations afterward is available as a separate add-on; an amendment or new SOW may be required depending on the complexity of the change.

### Outcome

A specific list of exposure points in your cluster configuration, not a generic MySQL-derived checklist that misses Galera entirely, including whether your inter-node traffic is actually encrypted, not just configured to look like it is, and whether your state transfer method is exposing data in transit. You will leave the rundown with a prioritized list your team can act on, not just a catalog of findings.

**CTA:** Pressure test your MariaDB Community environment security.

## PostgreSQL Security Assessment

A full review of your PostgreSQL environment's security configuration against your compliance requirements. Role-based access control, extension risk, and encryption are included. A permissive GRANT structure or an unreviewed extension can undo an otherwise solid security posture.

We review your configuration and access controls against the specific requirements you name at kickoff. Role inheritance in PostgreSQL is easy to get wrong in ways that are not obvious from the role list alone, which is exactly where this review spends its time.

### Deliverables

- Discovery session reviewing your specific security requirements and compliance obligations
- PMM Advisor configuration with a focused walkthrough of CVE, configuration, authentication, connection, and replication security checks
- Audit of role-based access control, including role inheritance and default privilege review
- Audit of patch management and network security, including pg_hba.conf authentication method review
- Review of backup and disaster recovery practices, encryption at rest, monitoring and logging, and vendor security considerations
- PDF report with findings and recommendations, delivered 5–7 business days after kickoff
- Live rundown session with open Q&A

### Who it is for

Scoped to a single PostgreSQL deployment. Implementation of recommendations afterward is available as a separate add-on; an amendment or new SOW may be required depending on the complexity of the change.

### Outcome

A specific list of what is exposed, including which extensions are a risk you have not evaluated yet, and where your role-based access control has drifted from what it was designed to enforce. You will know exactly which pg_hba.conf rules are wider than necessary.

**CTA:** Pressure test your PostgreSQL security posture.

## MongoDB Security Assessment

A full review of your MongoDB deployment's security configuration, authentication, role-based access control, and encryption, against the compliance requirements you are on the hook for.

We review your configuration and access controls against the specific requirements you name at kickoff, not a generic NoSQL security template. Custom roles are where most MongoDB security reviews find the biggest gaps, since it is easy to grant a broader set of actions than the application actually needs.

### Deliverables

- Discovery session reviewing your specific security requirements and compliance obligations
- PMM Advisor configuration with a focused walkthrough of CVE, configuration, authentication, connection, and replication security checks
- Audit of user and role security, including custom role definitions and built-in role usage
- Audit of patch management and network security, including IP binding and auth mechanism review
- Review of backup and disaster recovery practices, encryption at rest, monitoring and logging, and vendor security considerations
- PDF report with findings and recommendations, delivered 5–7 business days after kickoff
- Live rundown session with open Q&A

### Who it is for

Scoped to a single MongoDB replica set or sharded cluster. Implementation of recommendations afterward is available as a separate add-on; an amendment or new SOW may be required depending on the complexity of the change.

### Outcome

A specific list of exposed configuration and access control gaps, not a generic NoSQL security checklist. You will know exactly which role definitions grant more than they should, and whether your network binding is exposing the deployment more broadly than intended. Every finding in the report is tied back to the specific compliance requirement it addresses, rather than to a generic severity label.

**CTA:** Pressure test your MongoDB security.

## Valkey / Redis Security Assessment

A full review of your Redis or Valkey deployment's security configuration, auth, ACLs, and network exposure, against the compliance requirements you are accountable for. Default configurations are notoriously permissive, and most teams never revisit them after initial setup.

We review your configuration and access controls against the specific requirements you name at kickoff. Command-level exposure is a common gap here; a deployment can look secure at the network layer while still allowing destructive commands from any authenticated client.

### Deliverables

- Discovery session reviewing your specific security requirements and compliance obligations
- PMM Advisor configuration with a focused walkthrough of CVE, configuration, authentication, connection, and replication security checks
- Audit of ACL configuration, including command and key-pattern restrictions per user
- Audit of patch management and network security, including bind address and protected-mode configuration
- Review of backup and disaster recovery practices, encryption at rest, monitoring and logging, and vendor security considerations
- PDF report with findings and recommendations, delivered 5–7 business days after kickoff
- Live rundown session with open Q&A

### Who it is for

Scoped to a single Redis or Valkey environment. Implementation of recommendations afterward is available as a separate add-on; an amendment or new SOW may be required depending on the complexity of the change.

### Outcome

A specific list of what is exposed in your ACL and network configuration, not a generic cache-layer security checklist. You will know exactly what data is reachable from where, and whether that matches what you intended, plus a prioritized list your team can act on immediately after the rundown.

**CTA:** Pressure test your Valkey / Redis security.
