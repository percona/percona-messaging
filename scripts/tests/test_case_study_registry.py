"""Regression tests for scripts/case_study_registry.py and validate_case_study_registry.py."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import case_study_registry as registry

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_validate_live_registry_passes() -> None:
    path = REPO_ROOT / "data" / "case-studies.json"
    loaded = registry.load_registry(path)
    issues = registry.validate_registry(loaded, repo_root=REPO_ROOT)
    assert issues == []


def test_validate_registry_flags_missing_customer(tmp_path: Path) -> None:
    payload = {
        "version": 2,
        "case_studies": [
            {
                "id": "missing-customer",
                "customer": "",
                "title": "Example",
                "url": "https://example.com/story",
                "status": "candidate",
            }
        ],
    }
    issues = registry.validate_registry(payload)
    assert any(issue.path.endswith(".customer") for issue in issues)


def test_validate_registry_requires_locations_for_adopted_status(tmp_path: Path) -> None:
    payload = {
        "version": 2,
        "case_studies": [
            {
                "id": "adopted-without-locations",
                "customer": "Example",
                "title": "Example story",
                "url": "https://example.com/story",
                "status": "adopted_in_messaging",
            }
        ],
    }
    issues = registry.validate_registry(payload)
    assert any("canonical_locations" in issue.path for issue in issues)


def test_validate_cli_against_live_registry() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/validate_case_study_registry.py"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr


def test_validate_registry_accepts_customer_name_without_url(tmp_path: Path) -> None:
    md_path = tmp_path / "proof.md"
    md_path.write_text("BBVA chose Percona for migration.\n", encoding="utf-8")
    payload = {
        "version": 2,
        "case_studies": [
            {
                "id": "bbva",
                "customer": "BBVA",
                "title": "MongoDB migration",
                "url": "https://www.percona.com/customer-story/bbva/",
                "status": "adopted_in_messaging",
                "canonical_locations": ["proof.md"],
            }
        ],
    }
    issues = registry.validate_registry(payload, repo_root=tmp_path)
    assert issues == []
