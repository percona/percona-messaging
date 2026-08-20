# Architecture and Design

**SKU:** CONS-AD  
**Starting from:** $11,400

Architecture decisions are cheap to make and expensive to undo. Choices that fit today's traffic can fall over at 3x write volume, and by then, every fix is a migration. We review your current or planned architecture against your actual workload, growth numbers, and availability targets, and you walk away with a documented set of options and the trade-offs behind each one.

This is one packaged fixed-fee scope under [Expert Consulting and Services](../messaging.md), not the full Consulting catalog. Implementation happens through Migration, Setup and Configuration, or other custom consulting scope when the need sits outside this design engagement.

## FAQ

### Is this for new deployments or existing ones?

Both. Teams use it to design a new deployment before anything is built, or to review an architecture that has outgrown its original design. Either way, we work from your actual access patterns, growth projections, and availability requirements, not a reference diagram.

### What do we walk away with?

An options document laying out each viable architecture for your use case with the pros and cons of each, plus documented infrastructure requirements, a growth and scalability plan, a monitoring and alerting plan, and a backup policy. It ends with a live Q&A rundown with your team.

### Will you just tell us which architecture to pick?

We will tell you which options hold up against your requirements and which do not, and why. The document records the rationale for what was chosen and what was ruled out, so the decision survives after the engagement ends and your next hire does not have to re-litigate it.

### Do you cover cloud and DBaaS deployments?

Yes. Self-managed, RDS, Aurora, Atlas, and other DBaaS platforms are all in scope. For DBaaS environments the review includes documented scaling and cost considerations, with guidance on controlling cloud spend.

### We already know our target architecture. Is this still useful?

Probably not on its own. If the design decision is already made, pair your project with our Migration or Setup and Configuration engagement instead. This engagement earns its fee when the options are still open. After go-live, a [Health Audit](../health-audit/messaging.md) is usually the better next step.

### Does this include building the architecture?

No. This is the design phase. Implementation happens through Migration or Setup and Configuration engagements, and the options document is written to hand straight into either one.

## Engine variants

Source files are split by engine so tech owners can review only their variant. Engine files on this PR are stubs; full copy lands in follow-up tech PRs (issue #274). On the Docsify site, includes still render below once those PRs land.

| Engine | Source file |
| --- | --- |
| MySQL | [MySQL](mysql.md) |
| MariaDB Server | [MariaDB Server](mariadb.md) |
| PostgreSQL | [PostgreSQL](postgresql.md) |
| MongoDB | [MongoDB](mongodb.md) |
| Valkey / Redis | [Valkey / Redis](valkey-redis.md) |

<!-- docsify assemble: full package page for readers -->

[MySQL](/offerings/expert-consulting/architecture-and-design/mysql.md ':include')

[MariaDB Server](/offerings/expert-consulting/architecture-and-design/mariadb.md ':include')

[PostgreSQL](/offerings/expert-consulting/architecture-and-design/postgresql.md ':include')

[MongoDB](/offerings/expert-consulting/architecture-and-design/mongodb.md ':include')

[Valkey / Redis](/offerings/expert-consulting/architecture-and-design/valkey-redis.md ':include')
