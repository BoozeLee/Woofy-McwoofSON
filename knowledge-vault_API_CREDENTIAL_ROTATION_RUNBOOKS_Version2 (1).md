# API Credential Rotation Runbooks 🦴

The checklist below includes the **full content of `CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`** so you never have to search for it.  
Use this as your one-stop shop for secure API key rotation, cleanup, and documentation.

---

## 🔑 Credential Rotation & History Cleanup (Full Protocol)

### Purpose
Procedures for regular credential rotation, secret management, and repository history cleanup to ensure security compliance.

### Steps

1. **Rotate all secrets and tokens (e.g., GitHub PATs, API keys) on a scheduled basis.**
2. **Use tools like git-filter-repo or BFG Repo-Cleaner to scrub secrets from history if exposed.**
3. **Update `.env` files and notify all dependent systems/agents of new credentials.**
4. **Document all rotations in this file with timestamp and responsible agent.**

---

## 🔍 Audit Log

- _[YYYY-MM-DD]_ Rotated Gmail OAuth credentials, scrubbed repo history for old tokens – [Agent Name]
- _[YYYY-MM-DD]_ GitHub PATs rotated, updated `.env` files – [Agent Name]

---

_Fill in new entries for each rotation event. Escalate if any secrets are found exposed or if rotation cannot be completed._

---

## Gmail OAuth API

**API/Service:** Gmail OAuth  
**Rotation Date:** [YYYY-MM-DD]  
**Agent Responsible:** [Your Name]

### 1. Preparation
- [ ] Review the protocol above (no more searching—it's here!)
- [ ] Notify team/stakeholders
- [ ] Locate all uses of Gmail credentials (`.env`, secrets manager, CI/CD, etc.)
- [ ] Schedule maintenance window (if needed)

### 2. Generate & Store New Credentials
- [ ] Go to Google Cloud Console → Credentials
- [ ] Create new OAuth Client ID/Secret
- [ ] Download & store securely
- [ ] Update `.env` and any secrets vaults

### 3. Update Dependencies
- [ ] Update all config files and CI/CD
- [ ] Remove/disable old credentials

### 4. Test & Validate
- [ ] Run Gmail automation/tests
- [ ] Check logs for errors or exposure

### 5. Cleanup & Documentation
- [ ] Remove old creds from everywhere
- [ ] Log rotation event above

---

## Discord Bot API

**API/Service:** Discord Bot  
**Rotation Date:** [YYYY-MM-DD]  
**Agent Responsible:** [Your Name]

### 1. Preparation
- [ ] Review protocol above
- [ ] Notify team
- [ ] Locate all token usage

### 2. Generate & Store New Token
- [ ] Discord Developer Portal → Regenerate Bot Token
- [ ] Update `.env` and secrets manager

### 3. Update Dependencies
- [ ] Update configs, bots, webhooks, CI/CD
- [ ] Remove/disable old token

### 4. Test & Validate
- [ ] Start bot, run core tests
- [ ] Check for errors

### 5. Cleanup & Documentation
- [ ] Remove old tokens
- [ ] Log rotation event above

---

## GitHub API

**API/Service:** GitHub (PAT, App, or OAuth)  
**Rotation Date:** [YYYY-MM-DD]  
**Agent Responsible:** [Your Name]

### 1. Preparation
- [ ] Review protocol above
- [ ] Notify team
- [ ] Find all PAT/App client usage

### 2. Generate & Store New Token
- [ ] Regenerate PAT/OAuth in GitHub
- [ ] Store in GitHub Secrets or vault

### 3. Update Dependencies
- [ ] Update workflows, integrations, `.env`
- [ ] Remove/disable old token

### 4. Test & Validate
- [ ] Run actions/integrations
- [ ] Check for errors

### 5. Cleanup & Documentation
- [ ] Remove old tokens
- [ ] Log rotation event above

---

## Stripe API

**API/Service:** Stripe  
**Rotation Date:** [YYYY-MM-DD]  
**Agent Responsible:** [Your Name]

### 1. Preparation
- [ ] Review protocol above
- [ ] Notify team
- [ ] Locate all keys usage

### 2. Generate & Store New Keys
- [ ] Stripe Dashboard → API → Roll keys
- [ ] Update `.env`, secrets, and backend configs

### 3. Update Dependencies
- [ ] Update all payment and webhook endpoints
- [ ] Remove/disable old keys

### 4. Test & Validate
- [ ] Process test payment
- [ ] Check logs

### 5. Cleanup & Documentation
- [ ] Remove old keys
- [ ] Log rotation event above

---

## Microsoft Graph API

**API/Service:** Microsoft Graph  
**Rotation Date:** [YYYY-MM-DD]  
**Agent Responsible:** [Your Name]

### 1. Preparation
- [ ] Review protocol above
- [ ] Notify team
- [ ] Locate all client/app secret usage

### 2. Generate & Store New Secret
- [ ] Azure Portal → App Registration → Certificates & secrets → New client secret
- [ ] Update `.env`, secrets manager

### 3. Update Dependencies
- [ ] Update services, automations, CI/CD
- [ ] Remove/disable old secret

### 4. Test & Validate
- [ ] Run integration tests
- [ ] Check for errors

### 5. Cleanup & Documentation
- [ ] Remove old secret
- [ ] Log rotation event above

---

## Perplexity API

**API/Service:** Perplexity (Planned)  
**Rotation Date:** [YYYY-MM-DD]  
**Agent Responsible:** [Your Name]

### 1. Preparation
- [ ] Review protocol above
- [ ] Notify stakeholders as needed

### 2. Generate & Store Key
- [ ] Request or generate new API key from Perplexity dashboard
- [ ] Store securely (`.env`, secrets manager)

### 3. Update Dependencies
- [ ] Update backend, integrations, CI/CD

### 4. Test & Validate
- [ ] Run test queries
- [ ] Monitor logs

### 5. Cleanup & Documentation
- [ ] Remove/disable old key
- [ ] Log rotation event above

---

## AWS API Keys

**API/Service:** AWS  
**Rotation Date:** [YYYY-MM-DD]  
**Agent Responsible:** [Your Name]

### 1. Preparation
- [ ] Review protocol above
- [ ] Notify team
- [ ] Identify all places AWS keys are stored/used

### 2. Generate & Store Keys
- [ ] AWS Console → IAM → Users → Security credentials → Create new access key
- [ ] Store in secrets manager

### 3. Update Dependencies
- [ ] Update `.env`, CI/CD, infra as code, etc.

### 4. Test & Validate
- [ ] Deploy/test automations
- [ ] Check for errors

### 5. Cleanup & Documentation
- [ ] Remove old keys
- [ ] Log rotation event above

---

## Google Drive API

**API/Service:** Google Drive  
**Rotation Date:** [YYYY-MM-DD]  
**Agent Responsible:** [Your Name]

### 1. Preparation
- [ ] Review protocol above
- [ ] Notify team
- [ ] Locate all usage

### 2. Generate & Store New Credentials
- [ ] Google Cloud Console → Credentials → Create new client secret
- [ ] Update `.env`, secrets manager

### 3. Update Dependencies
- [ ] Update all configs

### 4. Test & Validate
- [ ] Run automation/tests

### 5. Cleanup & Documentation
- [ ] Remove/disable old creds
- [ ] Log rotation event above

---

# 🦴 WOOFY Rule: Rotate, validate, document, and never leave old keys behind!  
_No more hunting for procedures—they’re all right here._