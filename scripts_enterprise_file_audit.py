#!/usr/bin/env python3
"""
🧹 Enterprise File Audit & Archival Script
Scans for versioned/duplicate files, archives old versions, and produces a categorized summary.
"""

import os
import shutil
from datetime import datetime

def find_files(patterns):
    import glob
    files = []
    for pattern in patterns:
        files.extend(glob.glob(pattern))
    return sorted(set(files))

def archive_files(files, archive_dir):
    os.makedirs(archive_dir, exist_ok=True)
    for f in files:
        shutil.move(f, os.path.join(archive_dir, os.path.basename(f)))

def write_summary(summary_path, categories):
    with open(summary_path, "w") as out:
        out.write("# 📁 Enterprise Repo File Summary\n\n")
        for cat, patterns in categories.items():
            out.write(f"## {cat}\n")
            files = find_files(patterns)
            if files:
                for f in files:
                    out.write(f"- {f}\n")
            else:
                out.write("_None found_\n")
            out.write("\n")

if __name__ == "__main__":
    archive_dir = f"archive/{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    summary_file = "ENTERPRISE_FILE_SUMMARY.md"

    # 1. Archive versioned files
    versioned = find_files(["*_Version*.md"])
    if versioned:
        print(f"📦 Archiving {len(versioned)} versioned files to {archive_dir}/")
        archive_files(versioned, archive_dir)
    else:
        print("✅ No versioned files found for archival.")

    # 2. Categorized summary
    categories = {
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
    print(f"📝 Generating categorized file summary: {summary_file}")
    write_summary(summary_file, categories)
    print("✅ Archival and summary complete!")
    print(f"• Archived files: {archive_dir if versioned else 'None'}")
    print(f"• Summary: {summary_file}")