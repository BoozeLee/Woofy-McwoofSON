# 🐾 WoofyMcWOOFSON OAuth Client Registration Guide

_Maintained by BoozeLee, 2025-09-08_

This guide explains how to register and manage OAuth clients for all WoofyMcWOOFSON platforms—Web, Desktop, Android, iOS.

---

## Supported Platforms & Google Console Types

| Platform | Google App Type      | Use Case                     |
|----------|---------------------|------------------------------|
| Web      | Web application     | Browser, API, backend/server |
| Desktop  | Desktop app         | Electron/native apps         |
| Android  | Android             | Native Android               |
| iOS      | iOS                 | Native iOS                   |

**Best Practice:**  
👉 Register a separate OAuth project/client for each platform.  
👉 Never reuse a client ID across web, desktop, or mobile.

---

## General Registration Steps (Google Example)

1. **Go to [Google Cloud Console](https://console.cloud.google.com/)**
2. APIs & Services > Credentials > Create Credentials > **OAuth client ID**
3. Select the correct Application type for your platform.
4. Enter authorized redirect URIs or platform identifiers as required.
5. Download client secrets/config and store in your enterprise secrets vault (never in source control).
6. Document client IDs and URIs in the _knowledge vault_ (not in this README).

---

## Quick Reference: Platform Checklist

### Web Application
- App type: **Web application**
- Redirect URI: `https://yourdomain.com/oauth2callback`
- Used for: Browser login, backend auth flows

### Desktop App
- App type: **Desktop app**
- Redirect URI: `http://localhost` (or as instructed)
- Used for: Electron/native desktop packages

### Android
- App type: **Android**
- Requires: Package name, SHA-1 fingerprint
- Used for: Native Android Play Store app

### iOS
- App type: **iOS**
- Requires: Bundle ID
- Used for: Native iOS App Store app

---

## Security & Storage

- Store all secrets in **GitHub Secrets**, environment files, or a secure secrets vault.
- Rotate credentials periodically and document in `knowledge-vault/CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`.
- NEVER commit client secrets to code or chat.

---

See [`CLIENT_REGISTRATION_SETUP.md`](./CLIENT_REGISTRATION_SETUP.md) for detailed instructions.