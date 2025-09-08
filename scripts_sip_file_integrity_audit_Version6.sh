#!/bin/bash
# WOOFY McWOOFSON: SIP File Integrity & Repo Audit Script
# ------------------------------------------------------
# Checks:
#  - All SIP (.zip/.tar.gz) files unzipped in repo
#  - No missing files in /Downloads
#  - No orphaned files in temp or spaghetti dirs
#  - Lists, logs, and generates a checklist for SIP audit

REPO_ROOT="$(pwd)"
SIP_DIRS=("." "./SIP" "./downloads" "./import" "./archives") # Add more as needed
AUDIT_LOG="sip_file_integrity_audit.log"
CHECKLIST_TEMPLATE="SIP_AUDIT_CHECKLIST.md"
DOWNLOADS_DIR="$HOME/Downloads"

echo "🐾 WOOFY: SIP File Integrity Audit"
echo "---------------------------------"
echo "Repo Root: $REPO_ROOT"
echo "Log file: $AUDIT_LOG"
echo ""

# 1. Find all SIP archive files
echo "🔍 Scanning for .zip/.tar.gz files..."
find "${SIP_DIRS[@]}" -type f \( -iname "*.zip" -o -iname "*.tar.gz" \) > all_archives.txt
cat all_archives.txt | tee -a "$AUDIT_LOG"

# 2. Check if each archive has a corresponding extracted folder
echo -e "\n📦 Checking archive extraction status..." | tee -a "$AUDIT_LOG"
while read -r archive; do
  base="${archive%.*}"
  if [[ "$archive" == *.tar.gz ]]; then
    base="${base%.*}"
  fi
  if [ -d "$base" ]; then
    echo "✅ Extracted: $archive --> $base" | tee -a "$AUDIT_LOG"
  else
    echo "❌ NOT EXTRACTED: $archive" | tee -a "$AUDIT_LOG"
  fi
done < all_archives.txt

# 3. List orphaned files in Downloads (not in repo)
echo -e "\n🗂️  Checking $DOWNLOADS_DIR for orphaned files..."
find "$DOWNLOADS_DIR" -type f \( -iname "*.md" -o -iname "*.py" -o -iname "*.js" -o -iname "*.sh" -o -iname "*.zip" -o -iname "*.tar.gz" \) > downloads_files.txt

echo "These files are in Downloads but NOT in repo:" | tee -a "$AUDIT_LOG"
while read -r file; do
  filename=$(basename "$file")
  if ! find "$REPO_ROOT" -type f -name "$filename" | grep -q .; then
    echo "⚠️  Orphaned: $file" | tee -a "$AUDIT_LOG"
  fi
done < downloads_files.txt

# 4. List untracked files in repo (spaghetti check)
echo -e "\n🍝 Checking for untracked/orphaned files in repo..." | tee -a "$AUDIT_LOG"
git status --porcelain | grep '??' | awk '{print $2}' | tee -a "$AUDIT_LOG"

# 5. Optional: List all files for manual cross-check
echo -e "\n📝 Full file manifest:" | tee -a "$AUDIT_LOG"
find "$REPO_ROOT" -type f | tee -a "$AUDIT_LOG"

# 6. Generate SIP Audit Checklist template
cat > "$CHECKLIST_TEMPLATE" <<EOF
# SIP File Integrity Audit Checklist

- [ ] All SIP (.zip/.tar.gz) files are extracted
- [ ] No archives left unextracted
- [ ] Downloads/import folders checked for lost files
- [ ] No orphaned or untracked files in repo
- [ ] Audit log reviewed: $AUDIT_LOG

## Archive Extraction

| Archive File         | Extracted Folder | Status  |
|----------------------|------------------|---------|
$(while read -r archive; do
    base="${archive%.*}"
    if [[ "$archive" == *.tar.gz ]]; then base="${base%.*}"; fi
    if [ -d "$base" ]; then
      echo "| $archive | $base | ✅ |"
    else
      echo "| $archive | (missing) | ❌ |"
    fi
  done < all_archives.txt)

## Orphaned Files (Downloads not in repo)

$(while read -r file; do
    filename=$(basename "$file")
    if ! find "$REPO_ROOT" -type f -name "$filename" | grep -q .; then
      echo "- [ ] $file"
    fi
  done < downloads_files.txt)

## Untracked Files (repo)

$(git status --porcelain | grep '??' | awk '{print "- [ ] " $2}')

---

_Audit run: $(date)_

EOF

echo -e "\n✅ Audit complete! Review $AUDIT_LOG and $CHECKLIST_TEMPLATE for results."