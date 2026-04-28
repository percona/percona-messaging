#!/usr/bin/env python3
"""Rules-based impact checker for messaging repository pull requests."""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

WAIVER_MARKER = "<!-- messaging-impact-waiver-data:v1 -->"


def run_git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git command failed")
    return result.stdout


def changed_files(base_ref: str, head_ref: str) -> list[str]:
    try:
        output = run_git(["diff", "--name-only", f"{base_ref}...{head_ref}"])
    except RuntimeError:
        output = run_git(["diff", "--name-only"])
    return [line.strip() for line in output.splitlines() if line.strip()]


def changed_diff(base_ref: str, head_ref: str) -> str:
    try:
        return run_git(["diff", f"{base_ref}...{head_ref}"])
    except RuntimeError:
        return run_git(["diff"])


def any_file_matches(files: list[str], patterns: list[str]) -> bool:
    return any(any(fnmatch.fnmatch(path, pattern) for pattern in patterns) for path in files)


def file_touched(files: list[str], expected_path: str) -> bool:
    return expected_path in files


def should_trigger(rule: dict[str, Any], files: list[str], diff_text: str) -> bool:
    triggers = rule.get("triggers", {})
    globs = triggers.get("file_globs", [])
    regexes = triggers.get("diff_regex", [])

    files_match = any_file_matches(files, globs) if globs else True
    regex_match = any(re.search(pattern, diff_text, flags=re.MULTILINE) for pattern in regexes) if regexes else True
    return files_match and regex_match


def load_waiver_state(path: Path | None) -> tuple[bool, frozenset[str], frozenset[str]]:
    """Return (waive_all, waived_paths, reset_paths) from optional waiver JSON."""
    if not path or not path.exists():
        return False, frozenset(), frozenset()
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return False, frozenset(), frozenset()
    waive_all = bool(raw.get("all"))
    paths_raw = raw.get("paths") or []
    reset_raw = raw.get("reset_paths") or []
    paths = frozenset(str(p).strip() for p in paths_raw if str(p).strip())
    reset_paths = frozenset(str(p).strip() for p in reset_raw if str(p).strip())
    return waive_all, paths, reset_paths


def build_report(
    rules: list[dict[str, Any]],
    files: list[str],
    diff_text: str,
    waive_all: bool,
    waived_paths: frozenset[str],
    reset_paths: frozenset[str],
) -> tuple[dict[str, Any], bool]:
    triggered: list[dict[str, Any]] = []
    has_blocker = False

    for rule in rules:
        if not should_trigger(rule, files, diff_text):
            continue

        must_review = rule.get("must_review", [])
        touched = [path for path in must_review if file_touched(files, path)]
        missing = [path for path in must_review if path not in touched]
        waived_base = list(missing) if waive_all else [path for path in missing if path in waived_paths]
        waived = [path for path in waived_base if path not in reset_paths]
        missing_for_block = [path for path in missing if path not in waived]

        severity = (rule.get("severity") or "warn").lower()
        if severity == "required" and missing_for_block:
            has_blocker = True

        triggered.append(
            {
                "id": rule.get("id"),
                "description": rule.get("description", ""),
                "severity": severity,
                "must_review": must_review,
                "touched": touched,
                "missing": missing,
                "waived": waived,
                "missing_for_block": missing_for_block,
                "suggest_globs": rule.get("suggest_globs", []),
            }
        )

    return {"changed_files": files, "triggered_rules": triggered}, has_blocker


def markdown_report(report: dict[str, Any]) -> str:
    lines = []
    lines.append("## Messaging Impact Check")
    lines.append("")
    changed = report.get("changed_files", [])
    if changed:
        lines.append(f"- Changed files: {len(changed)}")
    else:
        lines.append("- No changed files detected by diff range.")
    lines.append("")

    rules = report.get("triggered_rules", [])
    if not rules:
        lines.append("No impact rules were triggered.")
        lines.append("")
        lines.append("Manual waiver commands (maintainers):")
        lines.append("- `/impact-ok all`")
        lines.append("- `/impact-ok <exact missing path>`")
        lines.append("- `/impact-reset all`")
        lines.append("- `/impact-reset <exact missing path>`")
        return "\n".join(lines)

    for rule in rules:
        missing_for_block = set(rule.get("missing_for_block", []))
        missing = set(rule.get("missing", []))
        waived = set(rule.get("waived", []))
        status = "BLOCKING" if rule["severity"] == "required" and missing_for_block else "WARN"
        lines.append(f"### {rule['id']} ({status})")
        if rule["description"]:
            lines.append(rule["description"])
        lines.append("")
        lines.append("Required review files:")
        for path in rule["must_review"]:
            if path in rule["touched"]:
                lines.append(f"- [x] `{path}`")
            elif path in missing and path in waived:
                lines.append(f"- [x] `{path}` *(waived — /impact-ok)*")
            else:
                lines.append(f"- [ ] `{path}`")
        if rule["suggest_globs"]:
            lines.append("")
            lines.append("Suggested additional scan:")
            for pattern in rule["suggest_globs"]:
                lines.append(f"- `{pattern}`")
        lines.append("")

    lines.append("Manual waiver commands (maintainers):")
    lines.append("- `/impact-ok all`")
    lines.append("- `/impact-ok <exact missing path>`")
    lines.append("- `/impact-reset all`")
    lines.append("- `/impact-reset <exact missing path>`")
    lines.append("")
    lines.append(f"Waiver state is stored in `{WAIVER_MARKER}`.")

    return "\n".join(lines).strip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check messaging impact rules against a PR diff.")
    parser.add_argument("--map", default="automation/messaging-impact-map.yml", dest="map_path")
    parser.add_argument("--base", default="origin/main", dest="base_ref")
    parser.add_argument("--head", default="HEAD", dest="head_ref")
    parser.add_argument("--waiver-file", default="", help="Optional waiver JSON path")
    parser.add_argument("--output-json", default="impact-report.json")
    parser.add_argument("--output-md", default="impact-report.md")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    map_path = Path(args.map_path)
    if not map_path.exists():
        print(f"Impact map not found: {map_path}", file=sys.stderr)
        return 2

    with map_path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle) or {}
    rules = config.get("rules", [])
    waiver_path = Path(args.waiver_file) if args.waiver_file else None
    waive_all, waived_paths, reset_paths = load_waiver_state(waiver_path)

    files = changed_files(args.base_ref, args.head_ref)
    diff_text = changed_diff(args.base_ref, args.head_ref)
    report, has_blocker = build_report(rules, files, diff_text, waive_all, waived_paths, reset_paths)
    report_md = markdown_report(report)

    Path(args.output_json).write_text(json.dumps(report, indent=2), encoding="utf-8")
    Path(args.output_md).write_text(report_md, encoding="utf-8")
    print(report_md)

    return 1 if has_blocker else 0


if __name__ == "__main__":
    raise SystemExit(main())
