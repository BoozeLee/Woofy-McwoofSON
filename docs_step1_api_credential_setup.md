# 🚀 Step 1: Secure API Credential Setup for All Integrations

**This guide walks you through obtaining and storing API credentials for each integration.  
Follow in order. Do not proceed to integration until all keys are obtained and stored securely.**

---

## 1. Google (Gmail) API

### A. How to Obtain Gmail API Credentials
1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create or select a project.
3. Navigate: **APIs & Services** → **Library** → search "Gmail API" → **ENABLE**.
4. Go to **Credentials** → **Create Credentials** → **OAuth client ID**.
5. Configure consent screen, app type, and download `client_secret.json`.
6. **Store client ID and client secret securely.**

### B. Secure the Credentials
- Add to your `.env` (or GitHub Secrets for prod):
  ```
  GMAIL_CLIENT_ID=your-client-id
  GMAIL_CLIENT_SECRET=your-client-secret
  GMAIL_REDIRECT_URI=your-redirect-uri
  ```
- **Never commit `client_secret.json` or `.env` to Git!**

---

## 2. Discord API

### A. How to Obtain Discord Bot Token  
1. Go to [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **New Application** → name it → **Bot** tab → **Add Bot**.
3. Click **Reset Token** and copy the bot token.
4. Under **OAuth2**, set scopes/permissions.

### B. Secure the Credentials
- Add to `.env` (or GitHub Secrets):
  ```
  DISCORD_BOT_TOKEN=your-bot-token
  DISCORD_CLIENT_ID=your-client-id
  DISCORD_CLIENT_SECRET=your-client-secret
  ```

---

## 3. GitHub API

### A. How to Obtain a PAT
1. Go to [GitHub Settings → Developer Settings → Personal Access Tokens](https://github.com/settings/tokens).
2. Generate new token with needed scopes, copy it.

### B. Secure the Credentials
- Add to `.env` or GitHub Secrets:
  ```
  GITHUB_TOKEN=your-github-token
  ```

---

## 4. Stripe API

### A. How to Obtain Stripe API Keys
1. Log in to [Stripe Dashboard](https://dashboard.stripe.com/apikeys).
2. Copy **publishable** and **secret** keys.

### B. Secure the Credentials
- Add to `.env` or GitHub Secrets:
  ```
  STRIPE_PUBLISHABLE_KEY=pk_live_xxx
  STRIPE_SECRET_KEY=sk_live_xxx
  ```

---

## 5. Perplexity AI

### A. How to Obtain Perplexity API Key
1. Log in at [Perplexity AI](https://www.perplexity.ai/).
2. Navigate to API, generate a new key.

### B. Secure the Credentials
- Add to `.env` or GitHub Secrets:
  ```
  PERPLEXITY_API_KEY=your-perplexity-key
  ```

---

## 6. IBM watsonx

### A. How to Obtain watsonx API Credentials
1. Log in at [IBM Cloud](https://cloud.ibm.com/).
2. Create a watsonx project/service.
3. Go to **Service Credentials**, generate credentials.

### B. Secure the Credentials
- Add to `.env` or GitHub Secrets:
  ```
  WATSONX_API_KEY=your-watsonx-key
  WATSONX_PROJECT_ID=your-watsonx-project-id
  ```

---

## 7. Google Gemini

### A. How to Obtain Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey) or Google Cloud.
2. Generate an API key.

### B. Secure the Credentials
- Add to `.env` or GitHub Secrets:
  ```
  GEMINI_API_KEY=your-gemini-key
  ```

---

## ✅ When complete:
- [ ] Verify all keys are present, tested, and **NOT committed to Git**.
- [ ] Proceed to Step 2: Security & Compliance Closure.