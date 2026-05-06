"""Regression tests for scripts/impact_check.py (fixture-driven)."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

import impact_check

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _impact_rules() -> list:
    raw = yaml.safe_load((FIXTURES / "impact_minimal.yml").read_text(encoding="utf-8"))
    return raw["rules"]


def test_should_trigger_respects_diff_regex() -> None:
    rule = {
        "triggers": {
            "file_globs": ["products/*.md"],
            "diff_regex": [r"NEVER_MATCH_THIS_MARKER_XYZ"],
        }
    }
    assert impact_check.should_trigger(rule, ["products/a.md"], "ordinary diff body") is False


def test_should_trigger_matches_when_regex_hits() -> None:
    rule = {
        "triggers": {
            "file_globs": ["products/*.md"],
            "diff_regex": [r"(?i)hello"],
        }
    }
    assert impact_check.should_trigger(rule, ["products/a.md"], "Say Hello in the release notes") is True


def test_build_report_required_rule_blocks_when_companion_missing() -> None:
    rules = _impact_rules()
    files = ["products/fixture-trigger.md"]
    diff_text = "+fixture change"
    report, has_blocker = impact_check.build_report(rules, files, diff_text, False, frozenset(), frozenset())

    assert has_blocker is True
    triggered = report["triggered_rules"]
    assert len(triggered) == 1
    row = triggered[0]
    assert row["id"] == "fixture-required-companion"
    assert row["severity"] == "required"
    assert row["missing_for_block"] == ["framework/fixture-companion.md"]


def test_build_report_warn_rule_does_not_block() -> None:
    rules = _impact_rules()
    files = ["products/fixture-warn.md"]
    diff_text = "+warn fixture"
    report, has_blocker = impact_check.build_report(rules, files, diff_text, False, frozenset(), frozenset())

    assert has_blocker is False
    row = report["triggered_rules"][0]
    assert row["severity"] == "warn"
    assert row["missing_for_block"]


def test_build_report_waive_all_clears_blocker() -> None:
    rules = _impact_rules()
    files = ["products/fixture-trigger.md"]
    diff_text = "+fixture"
    report, has_blocker = impact_check.build_report(rules, files, diff_text, True, frozenset(), frozenset())

    assert has_blocker is False
    assert report["triggered_rules"][0]["missing_for_block"] == []


def test_load_waiver_state_reads_paths(tmp_path: Path) -> None:
    waiver = tmp_path / "waiver.json"
    waiver.write_text(
        json.dumps({"all": False, "paths": ["framework/fixture-companion.md"], "reset_paths": []}),
        encoding="utf-8",
    )
    waive_all, paths, reset_paths = impact_check.load_waiver_state(waiver)
    assert waive_all is False
    assert paths == frozenset({"framework/fixture-companion.md"})
    assert reset_paths == frozenset()


def test_markdown_report_includes_blocking_label_when_required() -> None:
    rules = _impact_rules()
    files = ["products/fixture-trigger.md"]
    report, _has_blocker = impact_check.build_report(rules, files, "+x", False, frozenset(), frozenset())
    md = impact_check.markdown_report(report)
    assert "fixture-required-companion" in md
    assert "(BLOCKING)" in md
    assert "`framework/fixture-companion.md`" in md
