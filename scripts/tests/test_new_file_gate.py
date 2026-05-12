"""Regression tests for scripts/new_file_gate.py."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

import new_file_gate

COMPLETE_PR_BODY = """### Existing files reviewed first

- Reviewed `products/pmm/messaging.md` for overlap and confirmed this topic stays distinct after edits.

### Exact gap not covered by existing files

- Existing hubs explain adjacent positioning but omit the fixture scenario exercised only in this draft path.

### Why this must be a new canonical file

- Consolidating into an existing hub would overload scope and blur ownership between teams maintaining those surfaces.

### Owner and maintenance plan

- Primary owner is the messaging automation fixture reviewer updating quarterly or whenever upstream pillars shift materially.

### Decomposition and propagation plan

- Downstream decks and web snippets referencing this module should be checked during the next quarterly propagation sweep.
"""

WEAK_PR_BODY = """### Existing files reviewed first

TBD

### Exact gap not covered by existing files

- Existing hubs explain adjacent positioning but omit the fixture scenario exercised only in this draft path.

### Why this must be a new canonical file

- Consolidating into an existing hub would overload scope and blur ownership between teams maintaining those surfaces.

### Owner and maintenance plan

- Primary owner is the messaging automation fixture reviewer updating quarterly or whenever upstream pillars shift materially.

### Decomposition and propagation plan

- Downstream decks and web snippets referencing this module should be checked during the next quarterly propagation sweep.
"""


def test_section_content_extracts_under_heading() -> None:
    body = "### Heading one\n\nBody line.\n\n### Heading two\n\nSecond."
    assert new_file_gate.section_content(body, "### Heading one") == "Body line."
    assert new_file_gate.section_content(body, "### Heading two") == "Second."


def test_is_meaningful_rejects_short_or_placeholder() -> None:
    assert new_file_gate.is_meaningful("") is False
    assert new_file_gate.is_meaningful("tbd") is False
    assert new_file_gate.is_meaningful("ok") is False
    assert new_file_gate.is_meaningful("This sentence is long enough for the gate to accept as substantive text.") is True


def test_main_passes_when_sections_complete(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    body_path = tmp_path / "pr_body.md"
    body_path.write_text(COMPLETE_PR_BODY, encoding="utf-8")
    out_path = tmp_path / "gate-out.md"

    monkeypatch.setattr(
        new_file_gate,
        "git_added_markdown",
        lambda _base, _head: ["products/fixture-new-doc.md"],
    )
    monkeypatch.setattr(
        sys,
        "argv",
        ["new_file_gate.py", "--pr-body-file", str(body_path), "--output-md", str(out_path)],
    )

    assert new_file_gate.main() == 0
    report = out_path.read_text(encoding="utf-8")
    assert "All required justification sections are present" in report


def test_main_fails_when_section_weak(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    body_path = tmp_path / "pr_body.md"
    body_path.write_text(WEAK_PR_BODY, encoding="utf-8")
    out_path = tmp_path / "gate-out.md"

    monkeypatch.setattr(
        new_file_gate,
        "git_added_markdown",
        lambda _base, _head: ["products/fixture-new-doc.md"],
    )
    monkeypatch.setattr(
        sys,
        "argv",
        ["new_file_gate.py", "--pr-body-file", str(body_path), "--output-md", str(out_path)],
    )

    assert new_file_gate.main() == 1
    report = out_path.read_text(encoding="utf-8")
    assert "Missing or insufficient required sections" in report
    assert "### Existing files reviewed first" in report


@pytest.mark.integration
def test_git_added_markdown_detects_added_markdown(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Requires a writable git workspace (skipped in environments that block `.git`, such as some sandboxes)."""
    monkeypatch.chdir(tmp_path)
    tpl = tmp_path / "empty_git_template"
    tpl.mkdir()
    init = subprocess.run(["git", "init", f"--template={tpl}"], capture_output=True, text=True)
    if init.returncode != 0:
        pytest.skip(f"git init unavailable in this environment: {init.stderr.strip()}")

    subprocess.run(["git", "config", "user.email", "fixture-test@example.com"], check=True, capture_output=True)
    subprocess.run(["git", "config", "user.name", "Fixture Test"], check=True, capture_output=True)

    (tmp_path / "baseline.md").write_text("baseline\n", encoding="utf-8")
    subprocess.run(["git", "add", "baseline.md"], check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", "base"], check=True, capture_output=True)

    (tmp_path / "added.md").write_text("new\n", encoding="utf-8")
    subprocess.run(["git", "add", "added.md"], check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", "add doc"], check=True, capture_output=True)

    added = new_file_gate.git_added_markdown("HEAD~1", "HEAD")
    assert added == ["added.md"]
