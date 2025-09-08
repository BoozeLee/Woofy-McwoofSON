# Gmail OAuth Setup & Troubleshooting

## Overview

- Step-by-step guide to integrating Gmail OAuth for the Bakery-street-projct agents and automation.

## Setup Steps

1. Create a Google Cloud project and enable Gmail API.
2. Configure OAuth consent screen and scopes.
3. **For initial development, set your redirect URI to:**
   ```
   http://localhost:8000/oauth2callback
   ```
   - This matches FastAPI default (adjust if using Flask or a different port).
   - Only set production/staging URIs once your app is ready to deploy.
4. Download client secrets and store securely.
5. Update application config and `.env` with new credentials.
6. Test integration and document any issues.

## Redirect URI Management

- **You can add or update redirect URIs in Google Cloud Console at any time.**
- Only the currently needed URIs (e.g., development) must be registered now; add production ones before you go live.

## Troubleshooting

- "Invalid client secret": Double-check downloaded credentials.
- OAuth error “redirect_uri_mismatch”: Ensure the URI in Google Cloud matches exactly what your app sends.
- Token expiry: Rotate and re-authorize via Google Cloud Console.

---

## Checklist

- [x] Set up Google Cloud project
- [x] Enable Gmail API
- [x] Create OAuth credentials
- [x] Set initial redirect URI: `http://localhost:8000/oauth2callback`
- [ ] Add production redirect URI before launch
- [x] Download and secure client secrets
- [x] Update `.env` and config
- [ ] Test integration

---

## Snippet: How to Reference Redirect URI

```env
# .env example for Gmail OAuth
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=http://localhost:8000/oauth2callback
```

---

_Log all setup issues and solutions below._