# Percona Database Service: Messaging

## Percona Database Service {#percona-database-service}

For organizations running databases across Kubernetes, public clouds, virtual machines, and on-premises infrastructure, Percona Database Service (PDS) is open source software for creating databases on infrastructure you choose.

Unlike a hyperscaler database service, where the provider hosts the database, the database stays on infrastructure you choose.

You open it in the cloud and connect a Kubernetes cluster you already run. Right now, that is MySQL only.

In the future, PDS is designed to help handle everyday operation, with more types of databases, and providing clear next steps once a database is already running.

### Customer Challenges and Value Alignment: Percona Database Service

**Optimized TCO**

- **Fewer steps to create a database:** You connect a cluster you already run and create the database from a template or your own settings.

**Performance and Reliability at Scale**

- **A starting configuration from production experience:** The template is set by people, from Percona Expert Support and Percona Expert Consulting and Services experience, for a stable, high-performing start. The advanced path leaves every setting to the team.

You can operate the database yourself, use Percona Expert Support when you need it, or have Percona ExpertOps take on more of the operational work.

**Security, Sovereignty, and Compliance**

- **Open source keeps an exit:** The creation path is open source software, so it stays independent of a one-way vendor database.

**Adaptability for Emerging Workloads**

- **What comes later:** A specific next action after the database is running comes later. A wider place to run comes after that: a private cloud, more than one provider, and more database technologies. Access through APIs and automation comes with that later work.

On Kubernetes, PDS uses Percona Operators to run the database. Right now, that is the Percona Operator for MySQL. PDS is how you create the database.

Percona Monitoring and Management (PMM) monitors a database. PDS creates one. The two stay separate for now.
