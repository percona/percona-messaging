#!/usr/bin/env python3
"""Report stale canonical messaging docs based on last commit age."""

from __future__ import annotations

import argparse
import json
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

CANONICAL_ROOTS = (
    "framework/",
    "use-cases-value-pillars/",
    "offerings/",
    "products/",
    "reference/",
)


@dataclass
class StaleFile:
    path: str
    age_days: int
    last_commit_iso: str


def tracked_markdown_files() -> list[str]:
    output = subprocess.check_output(["git", "ls-files", "*.md"], text=True)
    files = [line.strip() for line in output.splitlines() if line.strip()]
    return [p for p in files if p.startswith(CANONICAL_ROOTS)]


def last_commit_timestamp(path: str) -> int:
    output = subprocess.check_output(["git", "log", "-1", "--format=%ct", "--", path], text=True).strip()
    return int(output) if output else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build stale content report.")
    parser.add_argument("--days", type=int, default=180)
    parser.add_argument("--output-md", default="staleness-report.md")
    parser.add_argument("--output-json", default="staleness-report.json")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    now = datetime.now(timezone.utc)
    stale: list[StaleFile] = []

    for path in tracked_markdown_files():
        ts = last_commit_timestamp(path)
        if ts <= 0:
            continue
        dt = datetime.fromtimestamp(ts, tz=timezone.utc)
        age_days = (now - dt).days
        if age_days >= args.days:
            stale.append(StaleFile(path=path, age_days=age_days, last_commit_iso=dt.strftime("%Y-%m-%d")))

    stale_sorted = sorted(stale, key=lambda item: item.age_days, reverse=True)
    md_lines = [
        "# Staleness Report",
        "",
        f"- Threshold: {args.days} days",
        f"- Generated at: {now.strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "",
    ]
    if not stale_sorted:
        md_lines.append("No stale canonical markdown files found.")
    else:
        md_lines.append("| File | Age (days) | Last commit |")
        md_lines.append("| --- | --- | --- |")
        for row in stale_sorted:
            md_lines.append(f"| `{row.path}` | {row.age_days} | {row.last_commit_iso} |")
    md_lines.append("")
    md = "\n".join(md_lines)
    Path(args.output_md).write_text(md, encoding="utf-8")

    payload = {
        "threshold_days": args.days,
        "generated_at_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "stale_files": [row.__dict__ for row in stale_sorted],
    }
    Path(args.output_json).write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
