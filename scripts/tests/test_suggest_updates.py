"""Regression tests for scripts/suggest_updates.py."""

from __future__ import annotations

from pathlib import Path

import yaml

import suggest_updates

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def test_detect_claim_returns_general_when_no_keyword() -> None:
    claim_map = yaml.safe_load((FIXTURES / "claim_minimal.yml").read_text(encoding="utf-8"))
    assert suggest_updates.detect_claim("no recognizable marketing phrases here", claim_map) == "general"


def test_detect_claim_matches_configured_keyword() -> None:
    claim_map = yaml.safe_load((FIXTURES / "claim_minimal.yml").read_text(encoding="utf-8"))
    assert suggest_updates.detect_claim("We discuss total cost of ownership in depth.", claim_map) == "cost"


def test_build_suggestions_high_confidence_when_target_not_in_diff_files() -> None:
    impact_map = yaml.safe_load((FIXTURES / "suggest_impact_minimal.yml").read_text(encoding="utf-8"))
    claim_map = yaml.safe_load((FIXTURES / "claim_minimal.yml").read_text(encoding="utf-8"))
    files = ["products/fixture-suggest.md"]
    diff_text = "Editing pricing and total cost of ownership narrative."

    rows = suggest_updates.build_suggestions(files, diff_text, impact_map, claim_map)

    assert len(rows) == 1
    row = rows[0]
    assert row["file"] == "framework/fixture-suggest-target.md"
    assert row["claim_trigger"] == "cost"
    assert row["confidence"] == 0.95
    assert row["auto_apply_candidate"] is True


def test_build_suggestions_lower_confidence_when_target_already_touched() -> None:
    impact_map = yaml.safe_load((FIXTURES / "suggest_impact_minimal.yml").read_text(encoding="utf-8"))
    claim_map: dict = {"claim_types": {}}
    files = ["products/fixture-suggest.md", "framework/fixture-suggest-target.md"]
    diff_text = "minor edits"

    rows = suggest_updates.build_suggestions(files, diff_text, impact_map, claim_map)

    assert len(rows) == 1
    assert rows[0]["confidence"] == 0.65
    assert rows[0]["auto_apply_candidate"] is False


def test_build_suggestions_diff_regex_filters_rules() -> None:
    impact_map = {
        "rules": [
            {
                "id": "regex-gated",
                "description": "Only when diff mentions MAGICTOKEN.",
                "triggers": {
                    "file_globs": ["*.md"],
                    "diff_regex": [r"MAGICTOKEN"],
                },
                "must_review": ["other.md"],
            }
        ]
    }
    claim_map: dict = {"claim_types": {}}

    miss = suggest_updates.build_suggestions(["a.md"], "plain diff", impact_map, claim_map)
    assert miss == []

    hit = suggest_updates.build_suggestions(["a.md"], "intro MAGICTOKEN tail", impact_map, claim_map)
    assert len(hit) == 1 and hit[0]["file"] == "other.md"
