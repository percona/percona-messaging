#!/usr/bin/env python3
"""Validate data/case-studies.json structure and canonical location links."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from case_study_registry import load_registry, validate_registry


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--registry",
        type=Path,
        default=Path("data/case-studies.json"),
        help="Manual case study registry JSON",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path("."),
        help="Repository root for canonical location checks",
    )
    parser.add_argument(
        "--skip-location-url-check",
        action="store_true",
        help="Validate schema only; do not require URLs inside canonical markdown files",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    registry = load_registry(args.registry)
    issues = validate_registry(
        registry,
        repo_root=None if args.skip_location_url_check else repo_root,
    )

    if issues:
        print(f"Case study registry validation failed ({len(issues)} issue(s)):", file=sys.stderr)
        for issue in issues:
            print(f"- {issue.path}: {issue.message}", file=sys.stderr)
        return 1

    count = len(registry.get("case_studies") or [])
    print(f"OK: validated {count} case study entr{'y' if count == 1 else 'ies'} in {args.registry}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
