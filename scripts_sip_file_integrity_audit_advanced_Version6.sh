#!/bin/bash
# WOOFY McWOOFSON: Advanced SIP File Integrity & Repo Audit Script
# ---------------------------------------------------------------
# - Checks for all SIP (.zip/.tar.gz) files
# - Verifies extraction, file count, and SHA256 hashes
# - Audits Downloads for uncommitted or missing files
# - Detects orphaned/untracked ("spaghetti") files
# - Checks for duplicate or conflicting files
# - Generates a comprehensive Markdown audit checklist

REPO_ROOT="$(pwd)"
SIP_DIRS=(. ./SIP ./downloads ./import ./archives)
AUDIT_LOG="sip_file_integrity_audit.log"
CHECKLIST_MD="SIP_AUDIT_CHECKLIST.md"
DOWNLOADS_DIR="$HOME/Downloads"
TMPDIR="$(mktemp -d)"
HASH_TMP="$TMPDIR/hashes.txt"
ERRORS=0

echo "🐾 WOOFY: Advanced SIP Audit" | tee "$AUDIT_LOG"
echo "-----------------------------" | tee -a "$AUDIT_LOG"

# 1. Find all SIP archives
echo -e "🔍 Scanning for .zip/.tar.gz SIP files..." | tee -a "$AUDIT_LOG"
find "${SIP_DIRS[@]}" -type f \( -iname "*.zip" -o -iname "*.tar.gz" \) > $TMPDIR/all_archives.txt
cat $TMPDIR/all_archives.txt | tee -a "$AUDIT_LOG"

# 2. Check extraction and file listing for each archive
echo -e "\n📦 Verifying archive extraction status & file counts..." | tee -a "$AUDIT_LOG"
printf "| Archive | Extracted? | Extracted Path | Files in Archive | Files in Extracted |\n" > $TMPDIR/archive_table.md
printf "|---------|------------|---------------|------------------|--------------------|\n" >> $TMPDIR/archive_table.md

while read -r archive; do
    base="${archive%.*}"
    [ "${archive: -7}" == ".tar.gz" ] && base="${base%.*}"
    extractdir="(none)"
    extracted="❌"
    files_archive="?"
    files_extracted="?"

    # Count files in archive
    if [[ "$archive" =~ \.zip$ ]]; then
        files_archive=$(unzip -l "$archive" | grep -v "Archive:" | grep -c "^[ ]*[0-9]")
    elif [[ "$archive" =~ \.tar\.gz$ ]]; then
        files_archive=$(tar tzf "$archive" | wc -l)
    fi

    # Check extraction
    if [ -d "$base" ]; then
        extracted="✅"
        extractdir="$base"
        files_extracted=$(find "$base" -type f | wc -l)
    fi

    printf "| %s | %s | %s | %s | %s |\n" "$archive" "$extracted" "$extractdir" "$files_archive" "$files_extracted" >> $TMPDIR/archive_table.md

    # Hash comparison if possible
    if [ "$extracted" == "✅" ] && [ "$files_extracted" -ne "$files_archive" ]; then
        echo "⚠️ File count mismatch for $archive ($files_archive in archive, $files_extracted in extracted)" | tee -a "$AUDIT_LOG"
        ((ERRORS++))
    fi
done < $TMPDIR/all_archives.txt

# 3. Hash check for all files
echo -e "\n🔑 Calculating SHA256 hashes for all repo files..." | tee -a "$AUDIT_LOG"
find "$REPO_ROOT" -type f ! -path "$TMPDIR/*" -exec sha256sum {} \; | sort > $HASH_TMP
# Detect duplicates (same hash, different file)
awk '{print $1}' $HASH_TMP | sort | uniq -d | while read hash; do
    echo "⚠️ Duplicate file detected for hash $hash:" | tee -a "$AUDIT_LOG"
    grep "$hash" $HASH_TMP | tee -a "$AUDIT_LOG"
    ((ERRORS++))
done

# 4. Downloads orphan check
echo -e "\n🗂️  Checking for orphaned files in Downloads..." | tee -a "$AUDIT_LOG"
find "$DOWNLOADS_DIR" -type f \( -iname "*.md" -o -iname "*.py" -o -iname "*.js" -o -iname "*.sh" -o -iname "*.zip" -o -iname "*.tar.gz" \) > $TMPDIR/downloads_files.txt
while read -r file; do
    filename=$(basename "$file")
    if ! find "$REPO_ROOT" -type f -name "$filename" | grep -q .; then
        echo "⚠️  Orphaned file in Downloads: $file" | tee -a "$AUDIT_LOG"
        ((ERRORS++))
    fi
done < $TMPDIR/downloads_files.txt

# 5. Untracked files check
echo -e "\n🍝 Scanning for untracked/orphaned files in repo..." | tee -a "$AUDIT_LOG"
git status --porcelain | grep '??' | awk '{print $2}' | tee -a "$AUDIT_LOG"

# 6. File manifest (for manual audit)
echo -e "\n📝 Full file manifest (excluding .git, temp, node_modules, etc.):" | tee -a "$AUDIT_LOG"
find "$REPO_ROOT" -type f ! -path "*/.git/*" ! -path "$TMPDIR/*" ! -path "*/node_modules/*" | tee -a "$AUDIT_LOG"

# 7. Summary & error count
if [ "$ERRORS" -eq 0 ]; then
    echo -e "\n✅ PASSED: No critical errors detected." | tee -a "$AUDIT_LOG"
else
    echo -e "\n❌ DETECTED: $ERRORS potential issues. Review log and checklist." | tee -a "$AUDIT_LOG"
fi

# 8. Generate SIP Audit Checklist template
cat > "$CHECKLIST_MD" <<EOF
# SIP File Integrity Audit Checklist (Advanced)

- [ ] All SIP (.zip/.tar.gz) files are present and extracted
- [ ] File counts match between archives and extracted folders
- [ ] No archives left unextracted
- [ ] Downloads/import folders checked for lost files
- [ ] No orphaned or untracked files in repo
- [ ] No duplicate/conflicting files (hash check)
- [ ] Audit log reviewed: $AUDIT_LOG

## Archive Extraction Table

$(cat $TMPDIR/archive_table.md)

## Orphaned Files (Downloads not in repo)

$(while read -r file; do
    filename=$(basename "$file")
    if ! find "$REPO_ROOT" -type f -name "$filename" | grep -q .; then
      echo "- [ ] $file"
    fi
  done < $TMPDIR/downloads_files.txt)

## Untracked Files (repo)

$(git status --porcelain | grep '??' | awk '{print "- [ ] " $2}')

## Duplicate File Hashes

$(awk '{print $1}' $HASH_TMP | sort | uniq -d | while read hash; do
    echo "### Hash: $hash"
    grep "$hash" $HASH_TMP | awk '{print "- [ ] " $2}'
  done)

---

_Audit run: $(date)_

EOF

echo -e "\n📋 Review $AUDIT_LOG and $CHECKLIST_MD for actionable results."
echo "🧹 To clean temp files: rm -rf $TMPDIR"