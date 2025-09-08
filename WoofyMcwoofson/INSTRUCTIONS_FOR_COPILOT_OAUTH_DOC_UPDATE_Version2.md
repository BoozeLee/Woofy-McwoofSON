# 🐾 Copilot: OAuth Documentation & Security Instructions

**Context:**  
The authentication/OAuth doc feedback is correct and clear. Please proceed with the following updates and actions for enterprise compliance and zero-loss onboarding.

---

## 1. Document All Redirect URIs

- In `knowledge-vault/GMAIL_OAUTH_SETUP.md`, explicitly list:
  - Production: `https://woofymcwoofson.com/oauth2callback`
  - Staging: `https://staging.woofymcwoofson.com/oauth2callback` (if staging will exist)
  - Development: `http://localhost:5000/oauth2callback` and `http://localhost:8000/oauth2callback`
- Note: Only register the URIs in Google Cloud Console that are currently needed. Add more as environments are deployed.

## 2. JavaScript Origins

- Instruct: **Leave blank unless a browser SPA will do the OAuth flow.**  
  Example: Only add `https://woofymcwoofson.com` if React/Vue login is implemented.

## 3. Security Handling

- **Never commit client secrets.**
- **GOOGLE_CLIENT_ID** and **GOOGLE_CLIENT_SECRET** must be stored as managed secrets (GitHub Secrets or encrypted vault).
- Log all credential rotation events in `knowledge-vault/CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`.
- Add a note about propagation delay (5min–hours) in `SECURITY_REMEDIATION_LOG.md`.

## 4. Checklist: Update `knowledge-vault/ONBOARDING.md`

- [x] Confirm all redirect URIs are documented and registered per environment.
- [x] Add reminder to update and rotate secrets after environment/domain changes.
- [x] Remind: Do not commit secrets.

## 5. Next Steps (Planned/Future)

- Prepare specs for token exchange endpoint and refresh token strategy (for future OAuth implementation).
- Update security docs as soon as OAuth endpoints are live.

---

**Action:**  
- Update all referenced files with these details.
- Confirm in PR and/or chat when complete.
- Tag Amazon Q for review after pushing changes.

_WoofyMcWOOFSON thanks you for your enterprise security and documentation discipline!_ 🦴🐾