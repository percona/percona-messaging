#!/usr/bin/env python3
"""Sync external case-study registry into data/case-studies.json."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen


def load_remote(source_url: str) -> list[dict]:
    with urlopen(source_url) as response:  # nosec B310
        payload = json.loads(response.read().decode("utf-8"))
    if isinstance(payload, dict):
        return payload.get("case_studies", [])
    if isinstance(payload, list):
        return payload
    return []


def normalize(items: list[dict]) -> list[dict]:
    normalized = []
    seen = set()
    for item in items:
        url = (item.get("url") or "").strip()
        if not url or url in seen:
            continue
        seen.add(url)
        normalized.append(
            {
                "title": (item.get("title") or "").strip(),
                "url": url,
                "published_at": (item.get("published_at") or "").strip(),
                "tags": item.get("tags") or [],
            }
        )
    return normalized


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync case studies from external JSON feed.")
    parser.add_argument("--source-url", required=True, help="Public JSON feed URL")
    parser.add_argument("--output", default="data/case-studies.json")
    args = parser.parse_args()

    current_path = Path(args.output)
    current = {}
    if current_path.exists():
        current = json.loads(current_path.read_text(encoding="utf-8"))

    remote_items = normalize(load_remote(args.source_url))
    current_urls = {item.get("url") for item in current.get("case_studies", [])}
    merged = list(current.get("case_studies", []))
    added = 0
    for item in remote_items:
        if item["url"] in current_urls:
            continue
        merged.append(item)
        current_urls.add(item["url"])
        added += 1

    payload = {
        "version": 1,
        "last_synced_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "case_studies": merged,
    }
    current_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Synced case studies. Added {added} new entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
