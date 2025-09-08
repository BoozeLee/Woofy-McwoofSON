# Gmail OAuth Setup & Troubleshooting

## Overview

Step-by-step Gmail/Drive OAuth setup for secure, enterprise automation.

---

## 1. Google Cloud Setup

- Create a GCP project.
- Enable **Gmail API** and **Google Drive API**.

## 2. OAuth Credentials

- Configure OAuth consent screen (internal or external).
- Add redirect URIs:
  - Production: `https://woofymcwoofson.com/oauth2callback`
  - Dev: `http://localhost:5000/oauth2callback`, `http://localhost:8000/oauth2callback`
- Download the OAuth client JSON.  
  - **Store on secure USB or encrypted vault** (never in repo/cloud).

## 3. GitHub & AWS Secrets

- Add OAuth Client ID/Secret to **GitHub Secrets**.
- (Optional) Store credentials in **AWS Secrets Manager** for enterprise workflows.

## 4. Testing

- Run local/dev OAuth flow and confirm token generation.
- Test automation scripts for Gmail/Drive access.

## 5. Rotation & Logging

- Document any credential rotation in `CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`.
- Log issues in `SECURITY_REMEDIATION_LOG.md`.

---

## Troubleshooting

- "Invalid client secret": Redownload credentials.
- "Redirect URI mismatch": Confirm all environments are listed in GCP.
- "Token expired": Rotate OAuth secret & re-authorize.

---

_Log all setup issues and solutions below._