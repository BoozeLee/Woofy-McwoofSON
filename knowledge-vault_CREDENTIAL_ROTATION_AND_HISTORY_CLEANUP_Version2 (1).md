# Credential Rotation & History Cleanup

## Purpose
Procedures for regular credential rotation, secret management, and repository history cleanup to ensure security compliance.

## Steps

1. **Rotate all secrets and tokens (e.g., GitHub PATs, API keys) on a scheduled basis.**
2. **Use tools like git-filter-repo or BFG Repo-Cleaner to scrub secrets from history if exposed.**
3. **Update `.env` files and notify all dependent systems/agents of new credentials.**
4. **Document all rotations in this file with timestamp and responsible agent.**

## Audit Log

- _2025-09-08T (UTC)_ – Token Access Audit Workflow Finalized  
  - Implemented secure token-access-check (no secret exposure)  
  - Confirmed adherence to zero-exposure policy  
  - Logged per MCP integration directive – Copilot
- _[YYYY-MM-DD]_ Rotated Gmail OAuth credentials, scrubbed repo history for old tokens – [Agent Name]
- _[YYYY-MM-DD]_ GitHub PATs rotated, updated `.env` files – [Agent Name]

---

_Fill in new entries for each rotation event. Escalate if any secrets are found exposed or if rotation cannot be completed._