# API Credential Rotation Runbooks 🦴

_This file includes:_  
- The complete Credential Rotation & History Cleanup protocol (copied from `knowledge-vault_CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`)
- Fill-in-the-blank rotation checklists for every major API in your stack

---

## 🔑 Credential Rotation & History Cleanup Protocol

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

_Fill in a new entry below for each rotation event, with timestamp and agent._

---

## 🦴 API Credential Rotation Runbooks

### Gmail OAuth API

**API/Service:** Gmail OAuth  
**Rotation Date:** [YYYY-MM-DD]  
**Agent Responsible:** [Your Name]

**Checklist:**
- [ ] Review the protocol above (no more searching—it's here!)
- [ ] Notify team/stakeholders
- [ ] Locate all uses of Gmail credentials (`.env`, secrets manager, CI/CD, etc.)
- [ ] Schedule maintenance window (if needed)
- [ ] Go to Google Cloud Console → Credentials
- [ ] Create new OAuth Client ID/Secret
- [ ] Download & store securely
- [ ] Update `.env` and any secrets vaults
- [ ] Update all config files and CI/CD
- [ ] Remove/disable old credentials
- [ ] Run Gmail automation/tests
- [ ] Check logs for errors or exposure
- [ ] Remove old creds from everywhere
- [ ] Log rotation event above

---

### Discord Bot API

**API/Service:** Discord Bot  
**Rotation Date:** [YYYY-MM-DD]  
**Agent Responsible:** [Your Name]

**Checklist:**
- [ ] Review protocol above
- [ ] Notify team
- [ ] Locate all token usage
- [ ] Discord Developer Portal → Regenerate Bot Token
- [ ] Update `.env` and secrets manager
- [ ] Update configs, bots, webhooks, CI/CD
- [ ] Remove/disable old token
- [ ] Start bot, run core tests
- [ ] Check for errors
- [ ] Remove old tokens
- [ ] Log rotation event above

---

### GitHub API

**API/Service:** GitHub (PAT, App, or OAuth)  
**Rotation Date:** [YYYY-MM-DD]  
**Agent Responsible:** [Your Name]

**Checklist:**
- [ ] Review protocol above
- [ ] Notify team
- [ ] Find all PAT/App client usage
- [ ] Regenerate PAT/OAuth in GitHub
- [ ] Store in GitHub Secrets or vault
- [ ] Update workflows, integrations, `.env`
- [ ] Remove/disable old token
- [ ] Run actions/integrations
- [ ] Check for errors
- [ ] Remove old tokens
- [ ] Log rotation event above

---

### Stripe API

**API/Service:** Stripe  
**Rotation Date:** [YYYY-MM-DD]  
**Agent Responsible:** [Your Name]

**Checklist:**
- [ ] Review protocol above
- [ ] Notify team
- [ ] Locate all keys usage
- [ ] Stripe Dashboard → API → Roll keys
- [ ] Update `.env`, secrets, and backend configs
- [ ] Update all payment and webhook endpoints
- [ ] Remove/disable old keys
- [ ] Process test payment
- [ ] Check logs
- [ ] Remove old keys
- [ ] Log rotation event above

---

### Microsoft Graph API

**API/Service:** Microsoft Graph  
**Rotation Date:** [YYYY-MM-DD]  
**Agent Responsible:** [Your Name]

**Checklist:**
- [ ] Review protocol above
- [ ] Notify team
- [ ] Locate all client/app secret usage
- [ ] Azure Portal → App Registration → Certificates & secrets → New client secret
- [ ] Update `.env`, secrets manager
- [ ] Update services, automations, CI/CD
- [ ] Remove/disable old secret
- [ ] Run integration tests
- [ ] Check for errors
- [ ] Remove old secret
- [ ] Log rotation event above

---

### Perplexity API

**API/Service:** Perplexity (Planned)  
**Rotation Date:** [YYYY-MM-DD]  
**Agent Responsible:** [Your Name]

**Checklist:**
- [ ] Review protocol above
- [ ] Notify stakeholders as needed
- [ ] Request or generate new API key from Perplexity dashboard
- [ ] Store securely (`.env`, secrets manager)
- [ ] Update backend, integrations, CI/CD
- [ ] Run test queries
- [ ] Monitor logs
- [ ] Remove/disable old key
- [ ] Log rotation event above

---

### AWS API Keys

**API/Service:** AWS  
**Rotation Date:** [YYYY-MM-DD]  
**Agent Responsible:** [Your Name]

**Checklist:**
- [ ] Review protocol above
- [ ] Notify team
- [ ] Identify all places AWS keys are stored/used
- [ ] AWS Console → IAM → Users → Security credentials → Create new access key
- [ ] Store in secrets manager
- [ ] Update `.env`, CI/CD, infra as code, etc.
- [ ] Deploy/test automations
- [ ] Check for errors
- [ ] Remove old keys
- [ ] Log rotation event above

---

### Google Drive API

**API/Service:** Google Drive  
**Rotation Date:** [YYYY-MM-DD]  
**Agent Responsible:** [Your Name]

**Checklist:**
- [ ] Review protocol above
- [ ] Notify team
- [ ] Locate all usage
- [ ] Google Cloud Console → Credentials → Create new client secret
- [ ] Update `.env`, secrets manager
- [ ] Update all configs
- [ ] Run automation/tests
- [ ] Remove/disable old creds
- [ ] Log rotation event above

---

# 🦴 WOOFY Rule: Rotate, validate, document, and never leave old keys behind!  
_No more hunting for procedures—they’re all right here._