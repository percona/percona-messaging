# Percona ExpertOps

**Proactive, hands-on database management partnership for teams that want Percona to operate part or all of their day-to-day operations.**

ExpertOps is Percona's proactive operations offering. Percona engineers provide hands-on database management with complete care for your database infrastructure, similar to an in-house DBA team, while reducing total cost of ownership. You can augment your current team with seasoned database administrators who care for your infrastructure 24/7 and keep databases performing at their best. Deep operational knowledge across MySQL, MariaDB, PostgreSQL, MongoDB-compatible environments, and Valkey/Redis keeps systems in expert hands so you can focus on your business.

Percona engineers perform operational work directly in your environment: monitoring, tuning, patching, automation, backup validation, and routine maintenance, using PMM for observability and Operators plus engine-appropriate tooling for execution. Unlike [Expert Support](../expert-support/messaging.md), ExpertOps is proactive and hands-on: Percona executes operational work rather than advising your team to execute it.

- **Who ExpertOps is for:** Teams with limited staff or time to manage databases, companies that need 24×7 operational coverage, organizations that want to prevent incidents instead of reacting to them, environments where uptime is business-critical.
- **Problems ExpertOps solves:** Operational noise and alert fatigue, manual or inconsistent scaling, maintenance and tuning, downtime from preventable issues, operational backlog, staffing limitations, and "day two" risk after migrations or upgrades (inconsistent backups, policy drift, weak monitoring).
- **Outcomes ExpertOps delivers:** Proactive issue prevention, stable and predictable performance, reduced operational burden on engineering teams, faster incident response from engineers already familiar with the environment, and lower infrastructure waste through rightsizing and standardized operations.

## Operating model

ExpertOps combines **people** (named experts and multidisciplinary DBAs), **process** (documented operations and change control), and **platform** (PMM, Operators, and backup tooling) so work is repeatable rather than reactive. That model targets compliance and reliability alongside continuous improvement as environments grow.

## Partnership scope

ExpertOps is flexible: Percona can own monitoring, tuning, patching, backup validation, and day-to-day database operations while you retain application logic, release cadence, and infrastructure choices where you prefer it.

| Layer | Often managed by ExpertOps | Often retained by the customer |
| --- | --- | --- |
| Underlying infrastructure | Rightsizing guidance, capacity reviews, failover and DR automation support | Cloud account ownership, cluster provisioning policy, network design |
| Database platform | Operator or instance configuration, patching, backup jobs, HA behavior | Major architecture decisions, vendor selection |
| Monitoring and alerting | PMM deployment, alert tuning, 24×7 alert response | Business priority definitions for alert thresholds |
| Tuning and performance | Query review, index and configuration tuning, proactive capacity checks | Application query design, schema ownership |
| Access and security | Secure remote access, patch and security advisory response | Identity policy, application credentials |
| Application | Incident coordination when database symptoms affect apps | Application code, feature releases |

Exact boundaries are agreed at onboarding and recorded in the subscription.

## Common scenarios

- **Seasonal or event traffic:** Dedicated operational coverage during spikes and steady-state tuning afterward.
- **Post-migration day-two operations:** Consistent backup behavior, policy alignment, and monitoring after cutover (for example, migration to Percona Operator for MongoDB on Kubernetes).
- **Staffing gaps:** 24/7 operational coverage without full-time hires.
- **Operator fleet operations:** Hands-on monitoring, backup validation, tuning, patching, and upgrade execution for MySQL, PostgreSQL, and MongoDB clusters on Percona Operators when customers want Percona to run Day-2 work instead of advising on it.
- **Operator migration and cutover (scoped):** Percona-led moves to operator-managed clusters from VMs, managed services, or legacy StatefulSets, plus post-cutover stabilization, when migration and operational hours are defined in the agreement.
- **DBaaS exit or hybrid operations:** Operational partnership after moving from managed database services to customer-controlled infrastructure while retaining expert coverage.

## Customer evidence

- **[Optimum Instruments](https://experience.percona.com/case-study/optimum-instruments/):** ~250 MySQL servers; Percona ExpertOps and PMM reduced downtime incidents, reclaimed 20+ engineer hours per month on manual backups, and avoided a DBA hire.
- **Minsait (telecom, Spain):** Tier-one workloads migrated to Percona Server for MongoDB on Google Cloud with the Percona Operator for MongoDB; ExpertOps operational assistance supported a business-critical billing platform with significant cost savings versus prior DBaaS deployment.

Use public case study links when available; do not invent metrics for customers without published proof.
