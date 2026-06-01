# Products

This directory contains product and database-specific messaging.

## Structure

Each product area includes `messaging.md` for canonical product framing. Competitive positioning and internal talk tracks belong in private execution systems, not in this repository (see [reference/content-governance.md](../reference/content-governance.md)).

Engine-specific Support, ExpertOps, or Consulting differentiators belong in the relevant product `messaging.md` pillar bullets (what ships in the distribution, what experts cover in production, and customer outcomes). Keep `offerings/` files cross-engine. If a product's expert-coverage scope outgrows `messaging.md`, add a sibling file under that product directory (for example `products/postgresql/expert-coverage.md`) through the new-file gate in [reference/content-governance.md](../reference/content-governance.md).

Current product areas include MySQL, PostgreSQL, MongoDB, Valkey/Redis, PMM, and Operators.
