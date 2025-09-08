# 🐶 WoofyMcWOOFSON OAuth Client Registration – Step-by-Step

_Last updated: 2025-09-08_

## For Each Platform (Web, Desktop, Android, iOS):

1. **Create a New Google Project or Use an Existing One**
    - Go to [Google Cloud Console](https://console.cloud.google.com/)
    - Select your project or create a new one for your platform.

2. **Navigate to APIs & Services > Credentials**
    - Click **Create Credentials** > **OAuth client ID**

3. **Configure Consent Screen**
    - Set up OAuth consent screen (brand, support email, scopes).

4. **Register Application Type**
    - Web: Add authorized redirect URIs (e.g. `https://yourdomain.com/oauth2callback`)
    - Desktop: No custom URI needed, defaults to `http://localhost`
    - Android/iOS: Enter app identifiers (package name, SHA-1, or bundle ID)

5. **Download Credentials**
    - Download `client_secret.json` or platform config
    - Store securely (never in code)

6. **Document in Knowledge Vault**
    - Update `knowledge-vault/GMAIL_OAUTH_SETUP.md` or equivalent with (never in public docs):
        - Platform
        - Client ID (redacted)
        - Secret (redacted)
        - Redirect URIs

7. **Integrate Into App**
    - Use environment variables or secret managers for all runtime configs

8. **Rotate & Audit Regularly**
    - Rotate secrets at least quarterly and after any exposure
    - Log all rotations in `CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`

---

**Tip:**  
If you only need Web for now, start there—add others as you go!

---

_Questions? Ping BoozeLee or check the `knowledge-vault/` for troubleshooting._