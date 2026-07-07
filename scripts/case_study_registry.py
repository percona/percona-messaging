"""Load and validate the manual case study registry in data/case-studies.json."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REGISTRY_VERSION = 2

STATUSES = ("published", "adopted_in_messaging", "candidate", "retired")

PILLARS = (
    "cost-optimization",
    "performance-reliability",
    "security-sovereignty-compliance",
    "future-readiness-ai",
)

PRODUCTS = (
    "mysql",
    "mongodb",
    "postgresql",
    "mariadb",
    "redis",
    "valkey",
    "pmm",
    "kubernetes",
)

OFFERINGS = (
    "expert_support",
    "expertops",
    "expert_consulting",
)

_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


@dataclass(frozen=True)
class ValidationIssue:
    path: str
    message: str


def load_registry(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": REGISTRY_VERSION, "last_reviewed_utc": "", "case_studies": []}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"version": REGISTRY_VERSION, "last_reviewed_utc": "", "case_studies": []}
    if not isinstance(payload, dict):
        return {"version": REGISTRY_VERSION, "last_reviewed_utc": "", "case_studies": []}

    studies = payload.get("case_studies")
    if not isinstance(studies, list):
        studies = []

    last_reviewed = str(payload.get("last_reviewed_utc") or payload.get("last_synced_utc") or "").strip()
    normalized_studies = [normalize_entry(item) for item in studies if isinstance(item, dict)]

    return {
        "version": payload.get("version", REGISTRY_VERSION),
        "last_reviewed_utc": last_reviewed,
        "case_studies": normalized_studies,
    }


def normalize_entry(item: dict[str, Any]) -> dict[str, Any]:
    entry = dict(item)
    title = str(entry.get("title") or "")
    customer_hint = str(entry.get("customer") or "").strip() or title.split(":", 1)[0].strip()
    if not entry.get("id"):
        entry["id"] = slug_from_title(customer_hint or title or "untitled")
    if not entry.get("customer") and title:
        entry["customer"] = title.split(":", 1)[0].strip()
    if entry.get("canonical_locations") and not entry.get("status"):
        entry["status"] = "adopted_in_messaging"
    return entry


def slug_from_title(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "untitled"


def validate_registry(registry: dict[str, Any], *, repo_root: Path | None = None) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    version = registry.get("version")
    if version not in (1, 2):
        issues.append(ValidationIssue("version", f"unsupported registry version: {version!r}"))

    studies = registry.get("case_studies")
    if not isinstance(studies, list):
        issues.append(ValidationIssue("case_studies", "must be a list"))
        return issues

    seen_ids: set[str] = set()
    for index, raw in enumerate(studies):
        prefix = f"case_studies[{index}]"
        if not isinstance(raw, dict):
            issues.append(ValidationIssue(prefix, "entry must be an object"))
            continue

        entry = normalize_entry(raw)
        entry_id = str(raw.get("id") or entry.get("id") or "").strip()
        if not entry_id:
            issues.append(ValidationIssue(f"{prefix}.id", "required"))
        elif not _ID_RE.match(entry_id):
            issues.append(ValidationIssue(f"{prefix}.id", "must be lowercase slug (a-z, 0-9, hyphens)"))
        elif entry_id in seen_ids:
            issues.append(ValidationIssue(f"{prefix}.id", f"duplicate id: {entry_id}"))
        else:
            seen_ids.add(entry_id)

        customer = str(raw.get("customer") or "").strip()
        if not customer:
            issues.append(ValidationIssue(f"{prefix}.customer", "required"))

        title = str(raw.get("title") or "").strip()
        if not title:
            issues.append(ValidationIssue(f"{prefix}.title", "required"))

        url = str(entry.get("url") or "").strip()
        if not url:
            issues.append(ValidationIssue(f"{prefix}.url", "required"))
        elif not url.startswith(("http://", "https://")):
            issues.append(ValidationIssue(f"{prefix}.url", "must be an http(s) URL"))

        status = str(entry.get("status") or "").strip()
        if status and status not in STATUSES:
            issues.append(ValidationIssue(f"{prefix}.status", f"must be one of: {', '.join(STATUSES)}"))

        published_date = entry.get("published_date")
        if published_date is not None and published_date != "":
            if not _ISO_DATE_RE.match(str(published_date)):
                issues.append(ValidationIssue(f"{prefix}.published_date", "must be YYYY-MM-DD or omitted"))

        primary_pillar = entry.get("primary_pillar")
        if primary_pillar is not None and primary_pillar != "":
            if primary_pillar not in PILLARS:
                issues.append(
                    ValidationIssue(f"{prefix}.primary_pillar", f"must be one of: {', '.join(PILLARS)}")
                )

        for field_name, allowed in (
            ("secondary_pillars", PILLARS),
            ("products", PRODUCTS),
            ("offerings", OFFERINGS),
            ("use_cases", None),
        ):
            values = entry.get(field_name)
            if values is None:
                continue
            if not isinstance(values, list):
                issues.append(ValidationIssue(f"{prefix}.{field_name}", "must be a list"))
                continue
            for value_index, value in enumerate(values):
                text = str(value).strip()
                if not text:
                    issues.append(ValidationIssue(f"{prefix}.{field_name}[{value_index}]", "must not be empty"))
                elif allowed is not None and text not in allowed:
                    issues.append(
                        ValidationIssue(
                            f"{prefix}.{field_name}[{value_index}]",
                            f"must be one of: {', '.join(allowed)}",
                        )
                    )

        headline_stats = entry.get("headline_stats")
        if headline_stats is not None:
            if not isinstance(headline_stats, list):
                issues.append(ValidationIssue(f"{prefix}.headline_stats", "must be a list"))
            else:
                for stat_index, stat in enumerate(headline_stats):
                    if not str(stat).strip():
                        issues.append(
                            ValidationIssue(f"{prefix}.headline_stats[{stat_index}]", "must not be empty")
                        )

        locations = entry.get("canonical_locations")
        if locations is not None:
            if not isinstance(locations, list):
                issues.append(ValidationIssue(f"{prefix}.canonical_locations", "must be a list"))
            else:
                for loc_index, location in enumerate(locations):
                    loc = str(location).strip()
                    if not loc:
                        issues.append(
                            ValidationIssue(f"{prefix}.canonical_locations[{loc_index}]", "must not be empty")
                        )
                    elif repo_root is not None:
                        path = repo_root / loc
                        if not path.is_file():
                            issues.append(
                                ValidationIssue(
                                    f"{prefix}.canonical_locations[{loc_index}]",
                                    f"file not found: {loc}",
                                )
                            )
                        else:
                            body = path.read_text(encoding="utf-8")
                            customer = str(entry.get("customer") or "").strip()
                            has_url = bool(url and url in body)
                            has_customer = bool(customer and customer.lower() in body.lower())
                            if not has_url and not has_customer:
                                issues.append(
                                    ValidationIssue(
                                        f"{prefix}.canonical_locations[{loc_index}]",
                                        f"neither URL nor customer name found in {loc}",
                                    )
                                )

        if status == "adopted_in_messaging":
            if not locations or not isinstance(locations, list) or not any(str(x).strip() for x in locations):
                issues.append(
                    ValidationIssue(
                        f"{prefix}.canonical_locations",
                        "required when status is adopted_in_messaging",
                    )
                )

    return issues


def status_summary(studies: list[dict[str, Any]]) -> dict[str, int]:
    counts = {status: 0 for status in STATUSES}
    for item in studies:
        if not isinstance(item, dict):
            continue
        status = str(normalize_entry(item).get("status") or "published").strip()
        if status not in counts:
            status = "published"
        counts[status] += 1
    return counts
