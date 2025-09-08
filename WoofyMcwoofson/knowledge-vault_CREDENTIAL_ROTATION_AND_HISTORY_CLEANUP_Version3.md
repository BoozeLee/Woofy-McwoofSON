# Credential Rotation & History Cleanup

## Purpose
Procedures for regular credential rotation, secret management, and repository history cleanup to ensure security compliance.

## Steps

1. **Rotate all secrets and tokens (e.g., GitHub PATs, API keys) on a scheduled basis.**
2. **Use tools like git-filter-repo or BFG Repo-Cleaner to scrub secrets from history if exposed.**
3. **Update `.env` files and notify all dependent systems/agents of new credentials.**
4. **Document all rotations in this file with timestamp and responsible agent.**

## Audit Log

- [2025-09-08] Enabled Gmail and Google Drive APIs in Google Cloud (no credentials generated yet) – [BoozeLee]
- [2025-09-08] Added GitHub secret `WOOFY_GOOGLE_OAUTH_CLIENT` for Gmail API integration – [BoozeLee]
- [2025-09-08] Refreshed AWS credentials and added to GitHub Secrets – [BoozeLee]
- [2025-09-08] Refreshed MONETIZATION secret in GitHub Secrets – [BoozeLee]
- [2025-09-08] Refreshed OPENROUTERAPI secret in GitHub Secrets – [BoozeLee]
- [2025-09-08] Refreshed PERPLEXITYAPI secret in GitHub Secrets – [BoozeLee]
- [2025-09-08] Refreshed COPILOT_TOKEN secret in GitHub Secrets – [BoozeLee]

---

_Fill in new entries for each rotation event or API enablement. Escalate if any secrets are found exposed or if rotation cannot be completed._