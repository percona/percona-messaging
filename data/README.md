# Data

This directory stores canonical machine-readable registries used by messaging automation.

## Files

- `case-studies.json`: manual case-study registry updated when maintainers adopt published proof (see monthly [case study maintenance reminder](../.github/workflows/case-study-maintenance-reminder.yml))
- `case-studies.schema.json`: JSON Schema for editor autocomplete and field validation
- `docs_whats_new_seen_guids.json`: RSS item GUIDs already handled by the optional Docs What's New **backup** monitor (issue opened or skipped as duplicate). Updated via automation PRs from the monitor workflow after each run; see [AUTOMATION.md](../AUTOMATION.md).

## Case study registry (`case-studies.json`)

Version **2** registry of published customer stories and whether canonical messaging cites them.

**When to update:** Add or refresh an entry in the same pull request that adopts proof in canonical markdown, or when recording a published story as a `candidate` for future adoption.

**Validation:** Run `python scripts/validate_case_study_registry.py` from the repository root (also exercised in CI when this file changes).

### Top-level fields

| Field | Required | Description |
| --- | --- | --- |
| `version` | yes | Registry schema version (`2`) |
| `last_reviewed_utc` | no | ISO-8601 timestamp of the last catalog review |
| `case_studies` | yes | Array of story entries |

### Entry fields

| Field | Required | Description |
| --- | --- | --- |
| `id` | yes | Stable lowercase slug (for example `optimum-instruments`) |
| `customer` | yes | Display name |
| `title` | yes | Short story headline |
| `url` | yes | Public case study URL |
| `status` | yes | `published`, `adopted_in_messaging`, `candidate`, or `retired` |
| `published_date` | no | Public publish date (`YYYY-MM-DD`) when known |
| `products` | no | Stacks involved: `mysql`, `mongodb`, `postgresql`, `mariadb`, `redis`, `valkey`, `pmm`, `kubernetes` |
| `offerings` | no | `expert_support`, `expertops`, `expert_consulting` |
| `primary_pillar` | no | Lead value pillar slug (matches `use-cases-value-pillars/` filenames) |
| `secondary_pillars` | no | Additional pillar slugs |
| `headline_stats` | no | Short quotable bullets sourced from the public story |
| `use_cases` | no | Free-form tags (for example `migration`, `licensing`, `kubernetes`) |
| `canonical_locations` | when adopted | Repo paths that cite this story (required when `status` is `adopted_in_messaging`) |
| `notes` | no | Internal maintainer notes |
| `last_verified_utc` | no | When stats and URL were last checked |

### Status values

| Status | Meaning |
| --- | --- |
| `candidate` | Published on percona.com or experience.percona.com; not yet cited in canonical messaging |
| `adopted_in_messaging` | Cited in one or more canonical markdown files (`canonical_locations` required) |
| `published` | Tracked for awareness only |
| `retired` | Story removed or no longer approved for use |

## Notes

- Keep this data factual and sourceable.
- `case-studies.json` is updated manually via pull request when proof is adopted or cataloged.
- `docs_whats_new_seen_guids.json` is updated by automation pull requests from the Docs What's New monitor after each run.
