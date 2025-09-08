# OAuth Credentials & Google API Policy 🦴

## Secure Storage & Handling

- **OAuth client ID** is securely stored in the GitHub secrets tab for use by CI/CD and workflows.
- **OAuth client JSON file** is always stored on a secure USB drive or encrypted removable media.
  - _Never commit the JSON file to the repository or upload to cloud storage._
- If credential rotation or re-creation is required, update both the USB storage and the GitHub secrets tab.

## Google API Enablement Checklist

- **Gmail API and Google Drive API** are enabled in the relevant Google Cloud Platform project.
- **API Key** is _only_ created if specifically required for a Google API that does NOT support OAuth or requires public unauthenticated access.
  - _API Key is **NOT** needed for Gmail or Drive automation (these require OAuth only)._
- If an API Key is created, it must be stored in the GitHub secrets tab and never in code or documentation.

## Additional Manual API/Key Approaches

- For Google APIs _outside_ of Gmail/Drive (e.g., **YouTube Data API**, **Maps API**, **Places API**):
  - Many require a manual API Key, not OAuth.
  - **Always check the Google API documentation** to determine if OAuth or API Key is required.
  - Store any such keys securely in GitHub secrets and document their use in the Knowledge Vault.

---

_Last updated: 2025-09-08 by BoozeLee_