# 🐶 GitHub Token Security Setup (Zero-Exposure AI Integration)

This guide enforces secure, auditable handling of GitHub tokens (PAT / fine‑grained) for WOOFY McWOOFSON.

## ✅ Mandatory Checklist
- [x] `.env` created (never committed) with placeholder `GITHUB_TOKEN=` (no value stored in repo)
- [x] `.env` listed in `.gitignore`
- [x] Fine‑grained PAT created (90‑day expiry, minimum scopes)
- [x] Added to GitHub Actions secrets (e.g. `COPILOT_TOKEN`)
- [x] Rotation event logged in:
  - `knowledge-vault/CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`
  - `SECURITY_REMEDIATION_LOG.md`
- [x] Secret scan (tests/test_security.py) passes (no leaks)

Security Status: 🟢 Active (maintain logs + enforce rotation)

---

## 🔐 Principles
- Prefer ephemeral `GITHUB_TOKEN` provided by Actions.
- Use a PAT only when required for scopes the default token lacks.
- Never commit or echo tokens into shell history/output.
- All rotations are documented (never store token values, only metadata).

---

## 🚀 Local Setup (No Secret Persistence)
Create (or ensure) a local `.env` file:
```
GITHUB_TOKEN=
```
Store the real value only in a password manager. Load with your local tooling (dotenv, direnv, etc.). Do not commit the value.

---

## 🛠 GitHub Actions Usage
Reference the secret (example):
```yaml
env:
  GITHUB_TOKEN: ${{ secrets.COPILOT_TOKEN }}
```
Do not rename secrets without updating all workflows + documenting the change in the rotation log.

---

## 🔁 Rotation Process
1. Generate new fine‑grained PAT (minimum scopes, 90 days).
2. Update the repository secret.
3. Revoke the old token immediately.
4. Append rotation entry (truncate old token to first 6 chars).
5. Re-run CI workflows (`token-access-check`, security scan).
6. Confirm no failures, then mark rotation complete in logs.

Example log line (no secret exposure):
```
2025-09-08T12:14:00Z – GitHub PAT rotated (old: abc123…, new applied & verified) – OK
```

---

## 🧪 Verification Steps
- `pytest -k security` → no findings.
- token-access-check.yml succeeds.
- Secret not present in:
  - `git grep -i github_token`
  - `git log -p` (recent commits)
  - build artifacts / cache.

---

## ⚠️ Prohibited
| Action | Reason |
|--------|--------|
| Committing tokens | Permanent exposure risk |
| Sharing full token in chats / PRs | Violates zero‑exposure policy |
| Embedding token in scripts | Prevents rotation & auditability |
| Copying token into screenshots | Uncontrolled replication |

---

## 📂 Related Assets
- Rotation log: CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md
- Security remediation: SECURITY_REMEDIATION_LOG.md
- Monthly reminder workflow: `.github/workflows/github-token-rotation-reminder.yml`
- Helper scripts: `scripts/github_token_setup.sh`, `scripts/github_token_setup.ps1`

---

## 🐾 Enforcement
- Secret scan patterns maintained in test_security.py
- Any relaxation requires PR label: `security` + rationale
- Non-compliant PRs are blocked until remediation

---

“No paws on plaintext credentials.” 🐶
