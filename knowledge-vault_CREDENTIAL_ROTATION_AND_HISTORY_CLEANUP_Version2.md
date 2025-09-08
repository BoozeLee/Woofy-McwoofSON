# Credential Rotation & History Cleanup

## Purpose
Procedures for regular credential rotation, secret management, and repository history cleanup to ensure security compliance.

## Steps

1. **Rotate all secrets and tokens (e.g., GitHub PATs, API keys) on a scheduled basis.**
2. **Use tools like git-filter-repo or BFG Repo-Cleaner to scrub secrets from history if exposed.**
3. **Update `.env` files and notify all dependent systems/agents of new credentials.**
4. **Document all rotations in this file with timestamp and responsible agent.**

## Audit Log

- _2025-01-27_ Rotated Amazon Q, Gmail, Discord, GitHub, Stripe credentials after log file exposure; scrubbed repo history; updated all `.env` files and notified all agents – Kilo Code

---

_Fill in new entries for each rotation event. Escalate if any secrets are found exposed or if rotation cannot be completed._