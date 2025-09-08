# 🦴 Woofy Profile & Organization Cleanup Automation Guide

Want to look sharp, stay safe, and keep snoopers out?  
Follow this checklist and automation strategy to **revoke unused app permissions, secure your GitHub (and org), and boost your professional profile.**

---

## 🐾 1. Automated OAuth App/Token Revocation

### For Individual Accounts

- **Scripted Audit** *(using GitHub API & CLI):*
    - List all authorized OAuth apps and personal access tokens (PATs)
    - Identify unused, risky, or legacy integrations
    - Revoke or delete with one command

```bash name=scripts/github_oauth_cleanup.sh
#!/bin/bash
# Woofy: Automated GitHub OAuth & PAT cleanup

# List all authorized OAuth apps
echo "🐾 Listing authorized OAuth apps:"
gh api user/installations | jq '.installations[] | {app: .app_slug, id: .id}'

# List all PATs (requires fine-grained PAT or UI for classic tokens)
echo "🐾 Visit https://github.com/settings/tokens to review/delete classic PATs."

# Revoke OAuth app by ID
# Example: gh api --method DELETE /user/installations/<installation_id>

echo "🐾 Review completed! Manually revoke legacy tokens via GitHub UI as needed."
```
- **Manual step:**  
  Delete any remaining old OAuth apps or tokens via [GitHub Settings > Applications](https://github.com/settings/applications).

---

### For Organizations

- **List all third-party app access:**
    - [Organization Settings > Third-party access](https://github.com/organizations/YOUR-ORG/settings/oauth_application_policy)
- **Scripted Review:**  
    - Use GitHub Org API to list and (with correct permissions) revoke app grants.
- **Audit all org members’ authorized apps periodically.**

---

## 🐾 2. General Profile & Org Hygiene

- **Profile:**
    - Remove outdated emails, links, or bios
    - Add professional avatar, clear tagline, and up-to-date contact info
    - Hide or archive old/unmaintained public repos

- **Org:**
    - Clean up old teams, invite lists, unused repos, and stale branches
    - Ensure branch protection and 2FA is enforced for all members
    - Add CODEOWNERS, SECURITY.md, and enterprise contact email
    - Rotate all org-level secrets and update audit logs

---

## 🦴 3. Automate It All

- **Schedule this cleanup quarterly** (use GitHub Actions or a calendar reminder)
- **Automate reporting**:  
    - Use scripts to email you a summary of tokens/apps/teams needing attention
    - Log all actions in `SECURITY_REMEDIATION_LOG.md`

---

## 🛡️ 4. Bonus: Woofy’s Security & Privacy Tips

- Never use shared tokens—generate per-app, per-user
- Remove integrations you don’t recognize or use
- Regularly review org audit logs for suspicious access
- Keep your profile public, but your credentials private!

---

## 🏁 Example Automation Flow

1. **Run `github_oauth_cleanup.sh`** locally or in a secure CI job.
2. **Receive summary report**: All apps/tokens, flagged for review.
3. **Manually revoke anything suspicious or legacy.**
4. **Push an updated `SECURITY_REMEDIATION_LOG.md`** documenting actions.
5. **Review org/team settings quarterly.**

---

**Stay sharp, stay safe, and keep your repo looking as professional as Woofy’s badge!**

---