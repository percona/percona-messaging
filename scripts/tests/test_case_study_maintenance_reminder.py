"""Regression tests for scripts/case_study_maintenance_reminder.py."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import case_study_maintenance_reminder as reminder

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def test_build_body_includes_marker_and_empty_registry_note() -> None:
    now = datetime(2026, 6, 1, 15, 0, tzinfo=timezone.utc)
    body = reminder.build_body({"version": 1, "last_reviewed_utc": "", "case_studies": []}, now)
    assert reminder.MARKER in body
    assert "No case studies tracked yet" in body
    assert "Percona case studies (index)" in body


def test_build_body_lists_registry_entries(tmp_path: Path) -> None:
    registry_path = tmp_path / "case-studies.json"
    registry_path.write_text(
        json.dumps(
            {
                "version": 1,
                "last_reviewed_utc": "2026-05-01T12:00:00Z",
                "case_studies": [
                    {
                        "title": "Optimum Instruments",
                        "url": "https://experience.percona.com/case-study/optimum-instruments/",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    registry = reminder.load_registry(registry_path)
    body = reminder.build_body(registry, datetime(2026, 6, 1, tzinfo=timezone.utc))
    assert "Optimum Instruments" in body
    assert "2026-05-01T12:00:00Z" in body


def test_load_registry_accepts_legacy_last_synced_field(tmp_path: Path) -> None:
    registry_path = tmp_path / "case-studies.json"
    registry_path.write_text(
        json.dumps({"version": 1, "last_synced_utc": "2026-01-01T00:00:00Z", "case_studies": []}),
        encoding="utf-8",
    )
    registry = reminder.load_registry(registry_path)
    assert registry["last_reviewed_utc"] == "2026-01-01T00:00:00Z"
