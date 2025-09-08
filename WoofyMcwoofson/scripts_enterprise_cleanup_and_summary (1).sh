#!/bin/bash
# 🧹 Enterprise Repo Cleanup & Summary Script
# Scans the repo, archives old/duplicate/versioned files, and produces a categorized summary.

ARCHIVE_DIR="archive"
SUMMARY_FILE="ENTERPRISE_FILE_SUMMARY.md"
mkdir -p "$ARCHIVE_DIR"

echo "# 🗂️ Enterprise Repo File Summary" > "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"

############################################
# 1. ARCHIVE OLD/VERSIONED FILES
############################################
echo "Archiving versioned and duplicate files to '$ARCHIVE_DIR'..."

find . -type f \( \
    -iname "*_Version[0-9]*.md" -o \
    -iname "*_old.md" -o \
    -iname "*-backup*.md" \
    \) | while read file; do
  echo "Archiving $file"
  mv "$file" "$ARCHIVE_DIR/"
done

############################################
# 2. CATEGORIZE FILES
############################################

echo "## Onboarding & Knowledge Vault" >> "$SUMMARY_FILE"
find . -type f -iname "*onboard*.md" -o -iname "knowledge-vault_*.md" | sort | while read file; do
  echo "- $file" >> "$SUMMARY_FILE"
done

echo "" >> "$SUMMARY_FILE"
echo "## Security, Token, & Compliance" >> "$SUMMARY_FILE"
find . -type f \( -iname "*security*.md" -o -iname "*token*.md" -o -iname "*remediation*.md" -o -iname "*audit*.md" \) | sort | while read file; do
  echo "- $file" >> "$SUMMARY_FILE"
done

echo "" >> "$SUMMARY_FILE"
echo "## CI/CD & GitHub Workflows" >> "$SUMMARY_FILE"
find .github/workflows -type f -iname "*.yml" 2>/dev/null | sort | while read file; do
  echo "- $file" >> "$SUMMARY_FILE"
done
find . -type f -iname "*ci*.yml" | sort | while read file; do
  echo "- $file" >> "$SUMMARY_FILE"
done

echo "" >> "$SUMMARY_FILE"
echo "## Integration & API Docs" >> "$SUMMARY_FILE"
find . -type f \( -iname "*integration*.md" -o -iname "*api*.md" -o -iname "*grok*.md" -o -iname "*perplexity*.md" -o -iname "*kilocode*.md" \) | sort | while read file; do
  echo "- $file" >> "$SUMMARY_FILE"
done

echo "" >> "$SUMMARY_FILE"
echo "## Status, Handoff, Transition, Launch" >> "$SUMMARY_FILE"
find . -type f \( -iname "*status*.md" -o -iname "*handoff*.md" -o -iname "*transition*.md" -o -iname "*launch*.md" \) | sort | while read file; do
  echo "- $file" >> "$SUMMARY_FILE"
done

echo "" >> "$SUMMARY_FILE"
echo "## General Documentation & Other" >> "$SUMMARY_FILE"
find . -type f -iname "*.md" ! -path "./$ARCHIVE_DIR/*" | grep -v -E "(onboard|knowledge-vault_|security|token|remediation|audit|ci|integration|api|grok|perplexity|kilocode|status|handoff|transition|launch)" | sort | while read file; do
  echo "- $file" >> "$SUMMARY_FILE"
done

echo ""
echo "✅ Cleanup and summary complete."
echo "See '$SUMMARY_FILE' for a categorized overview of your Markdown files."
echo "Old versioned files are moved to '$ARCHIVE_DIR/'."