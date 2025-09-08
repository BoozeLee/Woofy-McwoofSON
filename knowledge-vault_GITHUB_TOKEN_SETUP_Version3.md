# 🐶 GitHub Token Security Setup (Zero-Exposure AI Integration)

This guide enforces secure, auditable handling of GitHub tokens (PAT / fine‑grained) for WOOFY McWOOFSON.

## ✅ Checklist (Must Complete)
- [x] `.env` created (never committed) with placeholder `GITHUB_TOKEN=` (no value stored in repo)
- [x] `.env` in `.gitignore`
- [x] Token created: fine‑grained, 90‑day expiry, minimum scopes (only what CI requires)
- [x] Added to GitHub Actions secrets (e.g. `COPILOT_TOKEN` or service-specific name)
- [x] Rotation event logged in:
  - `knowledge-vault/CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`
  - `SECURITY_REMEDIATION_LOG.md`

## 🔐 Principles
- Never hardcode tokens
- Prefer ephemeral `GITHUB_TOKEN` from Actions where possible
- PAT only for scopes the ephemeral token lacks
- Rotate before expiry (reminder workflow runs monthly)

## 🚀 Local Setup (No Secrets in Repo)
1. Create `.env`:
   ```
   GITHUB_TOKEN=
   ```
2. Store actual value only in your password manager.
3. Use a dotenv loader locally (never commit value).

## 🛠 Using in GitHub Actions
Reference secret:
```yaml
env:
  GITHUB_TOKEN: ${{ secrets.COPILOT_TOKEN }}
```

## 🔁 Rotation Process
1. Generate new fine‑grained PAT (90 days)
2. Update GitHub secret
3. Invalidate old PAT
4. Append rotation log entry (truncate old token to 6 chars)
5. Confirm workflows succeed

Example log line (no secrets):
```
2025-09-08T12:14:00Z – GitHub PAT rotated (old: abc123…, new set & verified) – OK
```

## 🧪 Verification
- Run token access workflow: `.github/workflows/token-access-check.yml`
- Run: `pytest -k token` (if token tests added)
- Confirm no matches in secret scan: `pytest -k security`

## ⚠️ Prohibited
- Screenshots of full token
- Pasting token in chat, issues, PRs
- Storing token in shell history (`setx` optional but avoid direct echo)

## 🧭 Related
- `CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`
- `SECURITY_REMEDIATION_LOG.md`
- `.github/workflows/github-token-rotation-reminder.yml`

Security Status: 🟢 Active (maintain logs + enforce rotation)

🐾 “No paws on plaintext credentials.” 