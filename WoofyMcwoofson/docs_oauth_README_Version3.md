# OAuth Client Registration – Web Application

_Maintained by BoozeLee, 2025-09-08_

## For Today's Launch

- **Platform:** Web application
- **Steps:**
  1. Go to [Google Cloud Console](https://console.cloud.google.com/)
  2. APIs & Services > Credentials > Create Credentials > OAuth client ID
  3. **Application type:** Web application
  4. Add your redirect URI (e.g. `https://yourdomain.com/oauth2callback`)
  5. Download `client_secret.json` and store it securely (never in code)
- Document the client ID and redirect URI in the knowledge vault (never in public docs)

_Want to add desktop or mobile later? Just create a new OAuth client for each platform!_