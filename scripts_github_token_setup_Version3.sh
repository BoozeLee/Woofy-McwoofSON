#!/usr/bin/env bash
set -euo pipefail

echo "[INFO] GitHub Token Secure Setup (no secrets will be written)."

if [[ ! -f .env ]]; then
  echo "GITHUB_TOKEN=" > .env
  echo "[OK] Created .env placeholder."
fi

if ! grep -qE '^\.env$' .gitignore 2>/dev/null; then
  echo ".env" >> .gitignore
  echo "[OK] Added .env to .gitignore."
fi

LOG_FILE="knowledge-vault/CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md"
mkdir -p knowledge-vault
touch "$LOG_FILE"

if ! grep -q "## GitHub Token Rotations" "$LOG_FILE"; then
  {
    echo ""
    echo "## GitHub Token Rotations"
    echo "- $(date -u +"%Y-%m-%dT%H:%M:%SZ") – Initialized rotation log (no token stored)."
  } >> "$LOG_FILE"
  echo "[OK] Initialized rotation log section."
else
  echo "[INFO] Rotation section already present."
fi

echo "[DONE] Scaffold complete. Add real token ONLY as a GitHub secret, never here."