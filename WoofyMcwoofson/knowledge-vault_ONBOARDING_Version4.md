# Onboarding Checklist

- [ ] Review `README.md` and project context
- [ ] Read `general-instructions.md` for audit/transition protocol
- [ ] Ensure access to all required repos and tools
- [ ] Complete environment setup per `GMAIL_OAUTH_SETUP.md` and related docs
- [ ] Confirm understanding of credential rotation and security policies
- [ ] Announce presence in team communication channel
- [ ] Document all onboarding questions and findings in this file

---

## Secure Handling of OAuth Client JSON

- OAuth client JSON file is handled only via secure removable storage during setup.  
  **Do not store on shared systems or in source control.**
- Download the OAuth client JSON only onto a secure, removable device (e.g., USB stick).
- Do not store on unprotected systems or in cloud storage.
- Never commit the file to source control.
- Unplug and securely store the device when not in use.
- If you miss the download window, revoke and recreate the OAuth client to generate a new JSON.

---

## OAuth Credential Recording

- OAuth JSON files are kept on a secure USB stick and are NOT uploaded or stored in the repo.
- The OAuth Client ID (and any necessary fields) are recorded in the repository’s **secrets tab** for use with CI/CD and serverless workflows.
- Do not upload JSON files or client secrets to GitHub or cloud storage.

---

_Keep this checklist up-to-date for every new team member or agent._