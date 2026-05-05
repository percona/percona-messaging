#!/usr/bin/env python3
"""Monitor Percona Documentation 'What's New' RSS and prepare state merges.

Intended as a secondary safety net (catch-all triage signal), not the primary
process for keeping canonical messaging aligned with releases.

The public feed (MkDocs RSS plugin) is stable and preferable to scraping HTML:
https://docs.percona.com/feed_rss_created.xml

Linked from https://docs.percona.com/new/ (see <link rel="alternate" ... rss+xml>).
"""

from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.request import Request, urlopen


def fetch_rss(feed_url: str) -> bytes:
    req = Request(
        feed_url,
        headers={"User-Agent": "percona-messaging-docs-feed-monitor/1.0"},
    )
    with urlopen(req) as response:  # nosec B310
        return response.read()


def parse_rss_items(xml_bytes: bytes) -> list[dict]:
    root = ET.fromstring(xml_bytes)
    channel = root.find("channel")
    if channel is None:
        return []
    out: list[dict] = []
    for el in channel.findall("item"):
        guid_el = el.find("guid")
        title_el = el.find("title")
        link_el = el.find("link")
        desc_el = el.find("description")
        pub_el = el.find("pubDate")
        guid = (guid_el.text or "").strip() if guid_el is not None and guid_el.text else ""
        if not guid:
            continue
        out.append(
            {
                "guid": guid,
                "title": (title_el.text or "").strip() if title_el is not None else "",
                "link": (link_el.text or "").strip() if link_el is not None else "",
                "description": (desc_el.text or "").strip() if desc_el is not None else "",
                "pubDate": (pub_el.text or "").strip() if pub_el is not None else "",
            }
        )
    return out


def load_seen(path: Path) -> set[str]:
    if not path.is_file():
        return set()
    data = json.loads(path.read_text(encoding="utf-8"))
    guids = data.get("guids")
    if not isinstance(guids, list):
        return set()
    return {str(g).strip() for g in guids if str(g).strip()}


def save_seen(path: Path, guids: set[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"guids": sorted(guids)}
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def cmd_bootstrap(args: argparse.Namespace) -> int:
    xml_bytes = fetch_rss(args.feed)
    items = parse_rss_items(xml_bytes)
    guids = {i["guid"] for i in items}
    save_seen(args.state, guids)
    print(f"Wrote {len(guids)} guid(s) to {args.state}", file=sys.stderr)
    return 0


def cmd_prepare(args: argparse.Namespace) -> int:
    xml_bytes = fetch_rss(args.feed)
    items = parse_rss_items(xml_bytes)
    seen = load_seen(args.state)
    new_items = [i for i in items if i["guid"] not in seen]
    out_path = Path(args.output_json)
    out_path.write_text(json.dumps(new_items, indent=2) + "\n", encoding="utf-8")
    print(f"New items (not in state): {len(new_items)}", file=sys.stderr)
    return 0


def cmd_merge(args: argparse.Namespace) -> int:
    processed_path = Path(args.guids_json)
    if not processed_path.is_file():
        print("No guids file; nothing to merge.", file=sys.stderr)
        return 0
    data = json.loads(processed_path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        print("guids_json must be a JSON array of strings.", file=sys.stderr)
        return 1
    to_add = {str(x).strip() for x in data if str(x).strip()}
    seen = load_seen(args.state)
    before = len(seen)
    seen |= to_add
    if len(seen) == before:
        print("State unchanged.", file=sys.stderr)
        return 0
    save_seen(args.state, seen)
    print(f"Merged {len(to_add)} guid(s); state now {len(seen)} total.", file=sys.stderr)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    default_feed = "https://docs.percona.com/feed_rss_created.xml"
    default_state = Path("data/docs_whats_new_seen_guids.json")

    p_boot = sub.add_parser("bootstrap", help="Fetch feed and write state with all current guids (no issues).")
    p_boot.add_argument("--feed", default=default_feed)
    p_boot.add_argument("--state", type=Path, default=default_state)
    p_boot.set_defaults(func=cmd_bootstrap)

    p_prep = sub.add_parser("prepare", help="Write JSON array of feed items whose guid is not in state.")
    p_prep.add_argument("--feed", default=default_feed)
    p_prep.add_argument("--state", type=Path, default=default_state)
    p_prep.add_argument("--output-json", type=Path, required=True)
    p_prep.set_defaults(func=cmd_prepare)

    p_merge = sub.add_parser("merge", help="Union guids from JSON array file into state file.")
    p_merge.add_argument("--state", type=Path, default=default_state)
    p_merge.add_argument("--guids-json", type=Path, required=True)
    p_merge.set_defaults(func=cmd_merge)

    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
