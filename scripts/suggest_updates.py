#!/usr/bin/env python3
"""Generate deterministic suggestion candidates from a PR diff and impact map."""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import subprocess
from pathlib import Path

import yaml


def git_diff(base_ref: str, head_ref: str) -> tuple[list[str], str]:
    try:
        files = subprocess.check_output(
            ["git", "diff", "--name-only", f"{base_ref}...{head_ref}"],
            text=True,
            stderr=subprocess.STDOUT,
        ).splitlines()
        diff_text = subprocess.check_output(
            ["git", "diff", f"{base_ref}...{head_ref}"],
            text=True,
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError:
        files = subprocess.check_output(["git", "diff", "--name-only"], text=True).splitlines()
        diff_text = subprocess.check_output(["git", "diff"], text=True)
    return [f.strip() for f in files if f.strip()], diff_text


def matches_any(path: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


def detect_claim(diff_text: str, claim_map: dict) -> str:
    claim_types = claim_map.get("claim_types", {})
    lowered = diff_text.lower()
    for claim_name, payload in claim_types.items():
        for keyword in payload.get("keywords", []):
            if keyword.lower() in lowered:
                return claim_name
    return "general"


def build_suggestions(files: list[str], diff_text: str, impact_map: dict, claim_map: dict) -> list[dict]:
    """Produce suggestion rows from a file list, diff text, and loaded YAML configs."""
    claim = detect_claim(diff_text, claim_map)
    suggestions: list[dict] = []
    for rule in impact_map.get("rules", []):
        file_globs = rule.get("triggers", {}).get("file_globs", [])
        diff_regex = rule.get("triggers", {}).get("diff_regex", [])
        path_hit = any(matches_any(path, file_globs) for path in files) if file_globs else True
        regex_hit = (
            any(re.search(pattern, diff_text, flags=re.IGNORECASE) for pattern in diff_regex) if diff_regex else True
        )
        if not (path_hit and regex_hit):
            continue

        for target in rule.get("must_review", []):
            touched = target in files
            confidence = 0.95 if not touched else 0.65
            suggestions.append(
                {
                    "file": target,
                    "why_impacted": rule.get("description", "Related by impact map rule"),
                    "claim_trigger": claim,
                    "confidence": round(confidence, 2),
                    "auto_apply_candidate": confidence >= 0.9,
                }
            )
    return suggestions


def main() -> int:
    parser = argparse.ArgumentParser(description="Suggest related file updates for PR reviewers.")
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--impact-map", default="automation/messaging-impact-map.yml")
    parser.add_argument("--claim-types", default="automation/claim-types.yml")
    parser.add_argument("--output", default="suggestions.json")
    args = parser.parse_args()

    files, diff_text = git_diff(args.base, args.head)
    impact_map = yaml.safe_load(Path(args.impact_map).read_text(encoding="utf-8")) or {}
    claim_map = yaml.safe_load(Path(args.claim_types).read_text(encoding="utf-8")) or {}
    suggestions = build_suggestions(files, diff_text, impact_map, claim_map)

    Path(args.output).write_text(json.dumps({"suggestions": suggestions}, indent=2), encoding="utf-8")
    print(json.dumps({"suggestions": suggestions}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
