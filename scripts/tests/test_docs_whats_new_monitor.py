"""Regression tests for scripts/docs_whats_new_monitor.py."""

from __future__ import annotations

import json
from argparse import Namespace
from pathlib import Path

import docs_whats_new_monitor as monitor

SAMPLE_GUID = "https://docs.percona.com/new/2026/04/24/patroni-412-update-for-percona-distribution-for-postgresql/"


def test_feed_marker_hash_is_stable() -> None:
    assert monitor.feed_marker_hash(SAMPLE_GUID) == monitor.feed_marker_hash(SAMPLE_GUID)
    assert len(monitor.feed_marker_hash(SAMPLE_GUID)) == 16


def test_feed_marker_html_matches_workflow_format() -> None:
    h = monitor.feed_marker_hash(SAMPLE_GUID)
    assert monitor.feed_marker_html(SAMPLE_GUID) == f"<!-- whatsnew-feed:{h} -->"


def test_feed_marker_search_token_avoids_html_comment_syntax() -> None:
    token = monitor.feed_marker_search_token(SAMPLE_GUID)
    assert token == f"whatsnew-feed:{monitor.feed_marker_hash(SAMPLE_GUID)}"
    assert "<" not in token


def test_merge_records_guids(tmp_path: Path) -> None:
    state = tmp_path / "seen.json"
    guids_file = tmp_path / "processed.json"
    guids_file.write_text(json.dumps([SAMPLE_GUID]) + "\n", encoding="utf-8")

    args = Namespace(state=state, guids_json=guids_file, print_changed=False)
    assert monitor.cmd_merge(args) == 0
    assert SAMPLE_GUID in monitor.load_seen(state)

    assert monitor.cmd_merge(args) == 0
