"""Shared governance waiver loading for Content Governance gate scripts."""

from __future__ import annotations

import json
from pathlib import Path

CHECK_NEW_FILE_GATE = "new_file_gate"
CHECK_DOC_COVERAGE = "doc_coverage"
CHECK_DUPLICATE_DETECTOR = "duplicate_detector"

KNOWN_CHECKS = frozenset(
    {
        CHECK_NEW_FILE_GATE,
        CHECK_DOC_COVERAGE,
        CHECK_DUPLICATE_DETECTOR,
    }
)

GOVERNANCE_WAIVER_MARKER = "<!-- messaging-governance-waiver-data:v1 -->"


def load_governance_waiver(path: Path | None) -> tuple[bool, frozenset[str], frozenset[str]]:
    """Return (waive_all, waived_checks, reset_checks) from optional waiver JSON."""
    if not path or not path.exists():
        return False, frozenset(), frozenset()
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return False, frozenset(), frozenset()

    waive_all = bool(raw.get("all"))
    checks_raw = raw.get("checks") or []
    reset_raw = raw.get("reset_checks") or []
    checks = frozenset(
        c for c in (str(x).strip() for x in checks_raw) if c in KNOWN_CHECKS
    )
    reset_checks = frozenset(
        c for c in (str(x).strip() for x in reset_raw) if c in KNOWN_CHECKS
    )
    return waive_all, checks, reset_checks


def check_is_waived(
    check_id: str,
    waive_all: bool,
    waived_checks: frozenset[str],
    reset_checks: frozenset[str],
) -> bool:
    if check_id not in KNOWN_CHECKS:
        return False
    if check_id in reset_checks:
        return False
    if waive_all:
        return True
    return check_id in waived_checks


def waiver_note_md(check_id: str) -> str:
    return (
        f"\n\n**Maintainer waiver:** `{check_id}` was waived via `/governance-ok` "
        f"(stored in `{GOVERNANCE_WAIVER_MARKER}`).\n"
    )
