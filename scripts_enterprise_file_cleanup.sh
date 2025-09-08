#!/bin/bash
# 🧹 Enterprise File Archival & Cleanup Script
# Scans for duplicate/versioned files, archives old versions, and generates a categorized file summary.

ARCHIVE_DIR="archive/$(date +%Y%m%d_%H%M%S)"
SUMMARY_FILE="ENTERPRISE_FILE_SUMMARY.md"
mkdir -p "$ARCHIVE_DIR"

echo "🔍 Scanning for versioned/duplicate docs..."
shopt -s nullglob
VERSIONED_FILES=(*_Version*.md)
if [ ${#VERSIONED_FILES[@]} -gt 0 ]; then
  echo "📦 Archiving versioned files to $ARCHIVE_DIR/"
  for f in "${VERSIONED_FILES[@]}"; do
    mv "$f" "$ARCHIVE_DIR/"
  done
else
  echo "✅ No versioned files found for archival."
fi

echo "📝 Generating categorized file summary: $SUMMARY_FILE"
cat <<EOF > $SUMMARY_FILE
# 📁 Enterprise Repo File Summary

## Onboarding & Knowledge Vault
EOF

ls knowledge-vault/*onboard* knowledge-vault/*README* 2>/dev/null | sed 's/^/- /' >> $SUMMARY_FILE
echo -e "\n## Security & Compliance" >> $SUMMARY_FILE
ls knowledge-vault/*SECURITY* knowledge-vault/*CREDENTIAL* SECURITY_REMEDIATION_LOG.md SECURITY*.md 2>/dev/null | sed 's/^/- /' >> $SUMMARY_FILE
echo -e "\n## CI/CD & Workflows" >> $SUMMARY_FILE
ls .github/workflows/*.yml scripts/* 2>/dev/null | sed 's/^/- /' >> $SUMMARY_FILE
echo -e "\n## Integrations & API" >> $SUMMARY_FILE
ls knowledge-vault/*GMAIL* knowledge-vault/*integration* *integration* 2>/dev/null | sed 's/^/- /' >> $SUMMARY_FILE
echo -e "\n## Transition & Audit" >> $SUMMARY_FILE
ls *TRANSITION* *handoff* *AUDIT* *REMEDIATION* 2>/dev/null | sed 's/^/- /' >> $SUMMARY_FILE
echo -e "\n## Documentation" >> $SUMMARY_FILE
ls README* *.md | grep -v $SUMMARY_FILE | sed 's/^/- /' >> $SUMMARY_FILE

echo "✅ Archival and summary complete!"
echo "• Archived files: $ARCHIVE_DIR"
echo "• Summary: $SUMMARY_FILE"