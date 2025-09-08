#!/usr/bin/env python3
"""
🧹 Enterprise Repo Cleanup & Summary Script (Python)
- Archives old/duplicate/versioned files.
- Produces a categorized Markdown file summary for onboarding, security, CI, integration, etc.
"""

import os
import shutil
import re

ARCHIVE_DIR = "archive"
SUMMARY_FILE = "ENTERPRISE_FILE_SUMMARY.md"
os.makedirs(ARCHIVE_DIR, exist_ok=True)

def archive_files(patterns):
    archived = []
    for root, _, files in os.walk("."):
        for f in files:
            path = os.path.join(root, f)
            if any(re.search(pat, f, re.IGNORECASE) for pat in patterns):
                if not path.startswith(f"./{ARCHIVE_DIR}/"):
                    print(f"Archiving {path}")
                    shutil.move(path, os.path.join(ARCHIVE_DIR, f))
                    archived.append(path)
    return archived

def find_files(patterns, exclude_dir=ARCHIVE_DIR):
    result = []
    for root, _, files in os.walk("."):
        if exclude_dir and exclude_dir in root:
            continue
        for f in files:
            for pat in patterns:
                if re.search(pat, f, re.IGNORECASE):
                    result.append(os.path.join(root, f))
    return sorted(set(result))

def write_section(f, heading, patterns):
    f.write(f"## {heading}\n")
    for file in find_files(patterns):
        f.write(f"- {file}\n")
    f.write("\n")

with open(SUMMARY_FILE, "w") as f:
    f.write("# 🗂️ Enterprise Repo File Summary\n\n")
    # Archive versioned/duplicate files
    archive_patterns = [r"_Version\d+\.md", r"_old\.md", r"-backup.*\.md"]
    archived = archive_files(archive_patterns)
    if archived:
        f.write("### Archived Files\n")
        for path in archived:
            f.write(f"- {path}\n")
        f.write("\n")

    write_section(f, "Onboarding & Knowledge Vault", [r"onboard.*\.md", r"knowledge-vault_.*\.md"])
    write_section(f, "Security, Token, & Compliance", [r"security.*\.md", r"token.*\.md", r"remediation.*\.md", r"audit.*\.md"])
    write_section(f, "CI/CD & GitHub Workflows", [r"\.github/workflows/.*\.yml", r"ci.*\.yml"])
    write_section(f, "Integration & API Docs", [r"integration.*\.md", r"api.*\.md", r"grok.*\.md", r"perplexity.*\.md", r"kilocode.*\.md"])
    write_section(f, "Status, Handoff, Transition, Launch", [r"status.*\.md", r"handoff.*\.md", r"transition.*\.md", r"launch.*\.md"])
    write_section(f, "General Documentation & Other", [r".*\.md"])

print(f"\n✅ Cleanup and summary complete.\nSee '{SUMMARY_FILE}' for categorized Markdown file overview.")
print(f"Old versioned files are moved to '{ARCHIVE_DIR}/'.")