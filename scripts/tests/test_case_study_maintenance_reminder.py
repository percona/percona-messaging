"""Regression tests for scripts/case_study_maintenance_reminder.py."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import case_study_maintenance_reminder as reminder
import case_study_registry as registry


def test_build_body_includes_marker_and_empty_registry_note() -> None:
    now = datetime(2026, 6, 1, 15, 0, tzinfo=timezone.utc)
    body = reminder.build_body({"version": 2, "last_reviewed_utc": "", "case_studies": []}, now)
    assert reminder.MARKER in body
    assert "No case studies tracked yet" in body
    assert "Percona case studies (index)" in body
    assert "Adoption summary" in body


def test_build_body_lists_registry_entries_with_status_groups(tmp_path: Path) -> None:
    registry_path = tmp_path / "case-studies.json"
    registry_path.write_text(
        json.dumps(
            {
                "version": 2,
                "last_reviewed_utc": "2026-05-01T12:00:00Z",
                "case_studies": [
                    {
                        "id": "optimum-instruments",
                        "customer": "Optimum Instruments",
                        "title": "ExpertOps and PMM reduce downtime",
                        "url": "https://experience.percona.com/case-study/optimum-instruments/",
                        "status": "adopted_in_messaging",
                        "primary_pillar": "cost-optimization",
                        "canonical_locations": ["offerings/expertops/messaging.md"],
                    },
                    {
                        "id": "example-candidate",
                        "customer": "Example Corp",
                        "title": "Candidate story",
                        "url": "https://www.percona.com/customer-story/example/",
                        "status": "candidate",
                        "products": ["mysql"],
                    },
                ],
            }
        ),
        encoding="utf-8",
    )
    loaded = registry.load_registry(registry_path)
    body = reminder.build_body(loaded, datetime(2026, 6, 1, tzinfo=timezone.utc))
    assert "Optimum Instruments" in body
    assert "2026-05-01T12:00:00Z" in body
    assert "Adopted in messaging" in body
    assert "Candidates (published, not yet cited)" in body
    assert "Example Corp" in body
    assert "cost-optimization" in body


def test_load_registry_tolerates_invalid_json(tmp_path: Path) -> None:
    registry_path = tmp_path / "case-studies.json"
    registry_path.write_text("{not json", encoding="utf-8")
    loaded = registry.load_registry(registry_path)
    assert loaded["case_studies"] == []
    assert loaded["last_reviewed_utc"] == ""


def test_load_registry_accepts_legacy_last_synced_field(tmp_path: Path) -> None:
    registry_path = tmp_path / "case-studies.json"
    registry_path.write_text(
        json.dumps({"version": 1, "last_synced_utc": "2026-01-01T00:00:00Z", "case_studies": []}),
        encoding="utf-8",
    )
    loaded = registry.load_registry(registry_path)
    assert loaded["last_reviewed_utc"] == "2026-01-01T00:00:00Z"


def test_normalize_entry_infers_legacy_fields() -> None:
    entry = registry.normalize_entry(
        {
            "title": "LeadByte: Aurora migration",
            "url": "https://example.com/leadbyte",
            "canonical_locations": ["framework/why-percona.md"],
        }
    )
    assert entry["id"] == "leadbyte"
    assert entry["customer"] == "LeadByte"
    assert entry["status"] == "adopted_in_messaging"
