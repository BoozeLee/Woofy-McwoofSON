#!/bin/bash
# 🧹 Enterprise Archival/Cleanup & Categorized File Summary Script
# Usage: ./scripts/enterprise_cleanup_and_summary.sh

set -e

ARCHIVE_DIR="archive/$(date +%Y%m%d_%H%M%S)"
SUMMARY_FILE="ENTERPRISE_FILE_SUMMARY.md"

mkdir -p "$ARCHIVE_DIR"

echo "🔍 Scanning repo for categorized files..."

# ----------- 1. Define file categories & patterns -----------
declare -A categories
categories["Onboarding"]="ONBOARDING|onboard|welcome|getting_started"
categories["Security"]="SECURITY|security|remediation|CREDENTIAL|rotation|audit|token"
categories["CI/CD"]="\\.github\\/workflows|workflow|ci|test|lint|deploy|dependabot"
categories["Integration"]="integration|kilo|grok|perplexity|api|discord|stripe|google|gmail"
categories["Transition"]="transition|handoff|DETAILED_TRANSITION_REPORT|passdown"
categories["Documentation"]="README|docs|guide|playbook|runbook|support|CONTRIBUTING|CODE_OF_CONDUCT"
categories["Versioned/Old"]="Version[0-9]+|_old|archive|deprecated|legacy"
categories["Other"]=".*"  # fallback

# ----------- 2. Find files and categorize -----------
declare -A cat_files
all_files=$(find . -type f \( -name "*.md" -o -name "*.yml" -o -name "*.sh" -o -name "*.py" \) | grep -v "$ARCHIVE_DIR")

for file in $all_files; do
    categorized=0
    for cat in "${!categories[@]}"; do
        if [[ "$file" =~ ${categories[$cat]} ]]; then
            cat_files["$cat"]+="$file"$'\n'
            categorized=1
            break
        fi
    done
    if [[ $categorized -eq 0 ]]; then
        cat_files["Other"]+="$file"$'\n'
    fi
done

# ----------- 3. Archive Versioned/Old Files -----------
echo "📦 Archiving versioned/old files to $ARCHIVE_DIR ..."
IFS=$'\n'
for file in $(echo "${cat_files[Versioned/Old]}"); do
    [ -f "$file" ] && mv "$file" "$ARCHIVE_DIR/" && echo "  - $file"
done
unset IFS

# ----------- 4. Generate categorized summary -----------
echo "📝 Generating categorized summary at $SUMMARY_FILE ..."
echo "# 📂 Enterprise Repo File Summary" > "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"
for cat in "${!categories[@]}"; do
    echo "## $cat" >> "$SUMMARY_FILE"
    files=$(echo "${cat_files[$cat]}" | sed '/^$/d')
    if [[ -z "$files" ]]; then
        echo "_No files found in this category._" >> "$SUMMARY_FILE"
    else
        echo "$files" | sed 's/^/- /' >> "$SUMMARY_FILE"
    fi
    echo "" >> "$SUMMARY_FILE"
done

echo "✅ Cleanup and summary complete!"
echo "  - Archived files: $ARCHIVE_DIR"
echo "  - File summary: $SUMMARY_FILE"