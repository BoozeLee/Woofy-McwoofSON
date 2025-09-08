# 🐾 WoofyMcWOOFSON OAuth Client Registration Guide

_Maintained by BoozeLee, 2025-09-08_

This guide explains how to register and manage OAuth clients for all WoofyMcWOOFSON platforms (start with Web application).

## For Today’s Setup

- **Platform:** Web application
- **Steps:**
  1. Go to [Google Cloud Console](https://console.cloud.google.com/)
  2. APIs & Services > Credentials > Create Credentials > OAuth client ID
  3. Application type: **Web application**
  4. Add your redirect URI (e.g. `https://yourdomain.com/oauth2callback`)
  5. Download `client_secret.json` and store securely (never in code)
  6. Document the client ID and redirect URI in the knowledge vault

## Expanding Later?

- **Desktop, Android, iOS:** Register separate clients for each.  
- Never reuse client IDs across platforms.

See [`CLIENT_REGISTRATION_SETUP.md`](./CLIENT_REGISTRATION_SETUP.md) for step-by-step.