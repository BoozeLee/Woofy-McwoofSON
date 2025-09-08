#!/usr/bin/env python3
"""
🧹 Enterprise File Audit & Archival Script

Scans for versioned/duplicate files, archives old versions (optionally dry-run), and produces a categorized summary.

Features:
- Dry run mode (no changes) with impact preview
- Summary-only mode
- Timestamped archive directories
- Safe move (skips if destination exists)
- Category summary Markdown output

Usage:
  python scripts/file_audit.py --dry-run
  python scripts/file_audit.py --archive
  python scripts/file_audit.py --summary-only

Exit Codes:
  0 success
  2 unexpected error
"""
from __future__ import annotations
import argparse
import os
import shutil
import json as _json
from datetime import datetime
from typing import Dict, List

VERSION_GLOB = "*_Version*.md"
SUMMARY_FILE = "ENTERPRISE_FILE_SUMMARY.md"
DEFAULT_CATEGORIES = {
    "Onboarding & Knowledge Vault": [
        "knowledge-vault/*onboard*", "knowledge-vault/*README*"
    ],
    "Security & Compliance": [
        "knowledge-vault/*SECURITY*", "knowledge-vault/*CREDENTIAL*",
        "SECURITY_REMEDIATION_LOG.md", "SECURITY*.md"
    ],
    "CI/CD & Workflows": [
        ".github/workflows/*.yml", "scripts/*"
    ],
    "Integrations & API": [
        "knowledge-vault/*GMAIL*", "knowledge-vault/*integration*", "*integration*"
    ],
    "Transition & Audit": [
        "*TRANSITION*", "*handoff*", "*AUDIT*", "*REMEDIATION*"
    ],
    "Documentation": [
        "README*", "*.md"
    ]
}


def find_files(patterns: List[str]) -> List[str]:
    import glob
    files: List[str] = []
    for pattern in patterns:
        files.extend(glob.glob(pattern))
    return sorted(set(files))


def archive_files(files: List[str], archive_dir: str, dry_run: bool = False) -> int:
    os.makedirs(archive_dir, exist_ok=True)
    moved = 0
    for f in files:
        dest = os.path.join(archive_dir, os.path.basename(f))
        if os.path.abspath(f) == os.path.abspath(dest):
            continue
        if os.path.exists(dest):
            print(f"[WARN] Skip (exists): {dest}")
            continue
        if dry_run:
            print(f"[DRY-RUN] Would move: {f} -> {dest}")
        else:
            shutil.move(f, dest)
            print(f"[MOVED] {f} -> {dest}")
            moved += 1
    return moved


def write_summary(summary_path: str, categories: Dict[str, List[str]]) -> Dict[str, List[str]]:
    collected: Dict[str, List[str]] = {}
    with open(summary_path, "w", encoding="utf-8") as out:
        out.write("# 📁 Enterprise Repo File Summary\n\n")
        for cat, patterns in categories.items():
            out.write(f"## {cat}\n")
            files = find_files(patterns)
            collected[cat] = files
            if files:
                for f in files:
                    out.write(f"- {f}\n")
            else:
                out.write("_None found_\n")
            out.write("\n")
    print(f"[INFO] Summary written: {summary_path}")
    return collected


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Enterprise file audit & archival")
    p.add_argument("--archive", action="store_true", help="Archive versioned files")
    p.add_argument("--dry-run", action="store_true", help="Preview actions without modifying files")
    p.add_argument("--summary-only", action="store_true", help="Only generate summary (no archival)")
    p.add_argument("--categories-file", help="Path to custom categories YAML/JSON (future use)")
    p.add_argument("--json", action="store_true", help="Emit JSON summary to stdout (machine readable)")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        archive_dir = os.path.join("archive", timestamp)

        versioned = find_files([VERSION_GLOB])
        print(f"[INFO] Found {len(versioned)} versioned file(s).")

        if args.archive and not args.summary_only:
            moved = archive_files(versioned, archive_dir, dry_run=args.dry_run)
            if args.dry_run:
                print("[SUCCESS] Dry run complete (no files moved).")
            else:
                print(f"[SUCCESS] Archived {moved} file(s) to {archive_dir}.")
        else:
            print("[INFO] Archival skipped (use --archive).")

        collected = write_summary(SUMMARY_FILE, DEFAULT_CATEGORIES)
        if args.json:
            print(_json.dumps({
                "versioned_count": len(versioned),
                "archived": bool(args.archive and not args.dry_run),
                "categories": collected
            }, indent=2))
        print("[SUCCESS] Completed audit.")
        return 0
    except Exception as e:  # pragma: no cover (broad catch for CLI)
        print(f"[ERROR] Error: {e}")
        return 2


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
