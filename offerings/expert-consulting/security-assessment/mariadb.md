## MariaDB Server Security Assessment

A full review of your MariaDB Server deployment's security configuration, including the Galera-specific exposure (if applicable) that most generic security scans miss entirely, such as inter-node traffic encryption and SST/IST transfer security.

We review your configuration and access controls against the specific compliance requirements you name at kickoff. A cluster is only as secure as its weakest node, so this review treats the cluster as the unit of assessment rather than individual nodes in isolation. Percona supports MariaDB Server under standard entitlements; MariaDB Enterprise is out of scope.

## Deliverables

- Discovery session reviewing your specific security requirements and compliance obligations
- PMM Advisor configuration with a focused walkthrough of CVE, configuration, authentication, connection, and replication security checks
- Audit of password management and validation, database-user security, patch management, and network security
- Review of inter-node encryption (TLS for wsrep traffic) and SST/IST transfer method security
- Review of backup and disaster recovery practices, encryption at rest, monitoring and logging, and vendor security considerations
- PDF report with findings and recommendations, delivered 5–7 business days after kickoff
- Live rundown session with open Q&A

## Who it is for

Scoped to a single MariaDB Server deployment, including Galera Cluster. Implementation of recommendations afterward is available as a separate add-on; an amendment or new SOW may be required depending on the complexity of the change.

## Outcome

A specific list of exposure points in your cluster configuration, not a generic MySQL-derived checklist that misses Galera entirely, including whether your inter-node traffic is actually encrypted, not just configured to look like it is, and whether your state transfer method is exposing data in transit. You will leave the rundown with a prioritized list your team can act on, not just a catalog of findings.

**CTA:** Pressure test your MariaDB Server environment security.
