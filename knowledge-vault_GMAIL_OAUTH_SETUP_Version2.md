# Gmail OAuth Setup & Troubleshooting

## Overview

- Step-by-step guide to integrating Gmail OAuth for the Bakery-street-projct agents and automation.

## Setup Steps

1. Create a Google Cloud project and enable Gmail API.
2. Configure OAuth consent screen and scopes.
3. Download client secrets and store securely.
4. Update application config and `.env` with new credentials.
5. Test integration and document any issues.

---

## OAuth Redirect URIs (2025-09-08)
Environment-specific authorized redirect URIs:

- Production: https://woofymcwoofson.com/oauth2callback
- Staging (planned): https://staging.woofymcwoofson.com/oauth2callback
- Development: 
  - http://localhost:5000/oauth2callback
  - http://localhost:8000/oauth2callback

Register ONLY those in active use; add new URIs when an environment goes live.

## Authorized JavaScript Origins
Leave blank unless a browser SPA (React/Vue/etc.) performs the OAuth initiation.
Add only when such a flow is implemented:
- (Future) https://woofymcwoofson.com

## Security Handling
- NEVER commit GOOGLE_CLIENT_ID or GOOGLE_CLIENT_SECRET.
- Store them as managed secrets (GitHub Secrets / encrypted vault).
- Log all rotations in CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md.
- Propagation delay: Config changes may take 5 minutes to several hours—record anomalies in SECURITY_REMEDIATION_LOG.md.

## Troubleshooting

- "Invalid client secret": Double-check downloaded credentials.
- Token expiry: Rotate and re-authorize via Google Cloud Console.

## Future Implementation Notes
Planned:
- Token exchange endpoint
- Refresh token rotation policy
- Revocation endpoint (admin)
Add ADR if architecture deviates (e.g., multi-tenant auth broker).

_Log all setup issues and solutions below._