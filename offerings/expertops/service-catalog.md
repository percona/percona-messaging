# Percona ExpertOps: service catalog

Subscription and delivery detail for ExpertOps: what is included in a subscription, how work is categorized, service levels, onboarding, and access requirements. Positioning (what ExpertOps is and who it is for) lives in [expertops.md](../expertops.md).

Commercial specifics (hour pools, pricing, and contract terms) are set per agreement. Confirm at quote time.

## Subscription overview

ExpertOps subscriptions package ongoing operations, periodic reviews, and tiered response commitments. Subscriptions are scoped per environment (for example, per cluster or agreed unit of coverage) and align to **Advanced tier** or **Premium tier** service levels.

## Ongoing entitlements

- **24×7×365 proactive monitoring and alerting** through PMM and agreed observability tooling, with alert response included in the subscription
- **Expert DBA hands-on support** for operational tasks within subscription hours
- **Named Service Delivery Manager (SDM)** for coordination, check-ins, customer advocacy, and regular operational reviews
- **Automated incident management** and defined escalation to Percona engineering when software defects or upstream issues require it
- **Root cause analysis (RCA)** for significant incidents, focused on durable fixes
- **Change management** for planned database work so production changes stay controlled and documented
- **Software bug handling** and escalation for Percona software in scope (for example Operators, backup tools, and supported distributions)
- **Collaboration channels:** service portal for tracked requests and scheduled work; dedicated Slack channel for agreed client users; phone for severity-1 coordination when voice contact is required
- **Secure remote access** to customer systems under agreed security controls
- **Basic maintenance**, including critical security patches and defined minor upgrades within subscription scope

## Periodic deliverables

Deliverable cadence depends on tier. Premium tier compresses major reviews into a quarterly rhythm; Advanced tier schedules the same review types annually unless otherwise contracted.

| Cadence | Deliverables |
| --- | --- |
| **Real time** | Critical issue advisory, security patch guidance, known bug alerts for software in scope |
| **Weekly** | Health status summary, defined maintenance and minor upgrades within included hours |
| **Monthly** | SDM check-in, security assessment, monthly report card; Premium tier may include a defined query review hour allocation |
| **Quarterly (Premium tier)** or **annually (Advanced tier)** | Top query review, performance review, business continuity review |

Monthly report cards and health and security reports give stakeholders a consistent view of environment status without waiting for an incident.

## Onboarding and setup

New ExpertOps engagements typically include:

- **Business review** to align on priorities, stakeholders, and success criteria
- **Platform installation** for monitoring, backups, and operational tooling (commonly PMM and engine-appropriate backup and Operator components)
- **Dashboard and internal system access** so Percona and customer teams share the same operational view
- **Alert configuration** aligned to customer severity and business priorities
- **Environment and usage review** with documented risks, improvement opportunities, and operational roadblocks
- **Roadmap review** for planned upgrades, migrations, and capacity changes

## Hours model

| Work type | Examples | Typical billing |
| --- | --- | --- |
| **Responsive** | Alert response, critical service restoration, performance analysis for slowdowns (including RCA), access to on-call experts | Included responsive hours per month (volume varies by tier and contract) |
| **Flexible / periodic** | Monitoring follow-up, defined maintenance, health checks, review preparation, SDM-coordinated operational tasks | Included flexible hours per year (volume varies by tier and contract) |
| **Project-based** | Architectural changes, major version upgrades or downgrades, net-new supported technologies in an existing managed environment | Scoped separately, often through Expert Consulting and Services or add-on hour blocks |

Additional hour blocks are available when teams need capacity beyond the included responsive and flexible pools.

## Service levels

| Severity | Advanced tier (initial response) | Premium tier (initial response) |
| --- | --- | --- |
| **S1** | 30 minutes | 15 minutes |
| **S2** | 90 minutes | 60 minutes |
| **S3** | 24 hours (weekdays) | 4 hours |
| **S4** | 48 hours (weekdays) | 24 hours |

Premium tier also defines **ongoing** response targets for open S1 and S2 incidents (1 hour and 4 hours respectively). Coverage is **24×7, follow-the-sun**.

Initial S1 response times align with Expert Support tiers: 30 minutes on Advanced Support and 15 minutes on Premium Support. ExpertOps adds hands-on restoration and operational ownership on top of those response commitments.

## Access and monitoring requirements

- **Dedicated monitoring footprint**, commonly a separate node or host for PMM and platform tooling, so observability does not compete with production database workloads
- **Agreed access levels**, typically sudo on the monitoring host, sudo on database nodes, and full database privileges needed for operational tasks
- **Secure connectivity**, commonly Tailscale or an equivalent customer-approved method; Premium tier contracts may allow additional connectivity options
- **Customer-side identity and network policy** ownership, with Percona operating within agreed security controls

Requirements are documented during onboarding so security and platform teams can approve access before go-live.
