# 🐶🦴 WOOFY McWOOFSON ENTERPRISE TODO LIST: SECRET SETUP & PRIORITY TASKS

---

## 🚨 1. IMMEDIATE PRIORITY: SECRET/TOKEN SETUP & REMOVAL

- [ ] **Rotate and create ALL new credentials/tokens** (Gmail OAuth, Discord Bot, GitHub PAT, Stripe Keys, etc.)  
      _Reference:_ `knowledge-vault/CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`, `SECURITY_REMEDIATION_LOG.md`
- [ ] **Add all new secrets to GitHub Actions/Repo Secrets** (never in code or chat!)
- [ ] **Scrub** any exposed secrets from local files and repository history using BFG or git-filter-repo
- [ ] **Remove/delete all local files containing old/exposed secrets**
- [ ] **Document each credential rotation and file removal** in the audit log (`CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`)
- [ ] **ONLY proceed with other setup after confirming all secrets are secured and documented**

---

## 2. STRUCTURED REPO & CODE TASKS (after secret remediation)

- [ ] **ADR Files:**  
  - Create/update Architecture Decision Records in `/docs/architecture/adr/`
  - Ensure ADR-0001 documents the serverless baseline
- [ ] **Handler & Tests Update:**  
  - Refactor handler to support negative test cases (invalid/malformed events)
  - Add/expand `tests/test_lambda_woofy_handler_negative.py`
- [ ] **Security Doc/Test:**  
  - Add/verify security policy in `SECURITY.md`
  - Add automated test to check for secret leaks in docs and code
- [ ] **README & CHANGELOG Links:**  
  - Update `README.md` and `CHANGELOG.md` to reference all new features, security steps, and ADRs
- [ ] **CI/CD Update:**  
  - Ensure GitHub Actions/CI config runs all new tests, coverage jobs, and secret scans

---

## 3. FINAL REVIEW

- [ ] Confirm all documentation, audit logs, and code changes are complete
- [ ] Push all updates to the repo and perform a final security review

---

> **Note:**  
> _DO NOT proceed with any further development or documentation until token/secret rotation, local file removal, and audit logging are confirmed complete. This is a deployment blocker and required for enterprise compliance._

---