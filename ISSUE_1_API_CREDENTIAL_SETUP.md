# 🚀 Step 1: Secure API Credential Setup for All Integrations

**Assignee:** @Kilo-Code

This checklist walks you through obtaining and setting up API credentials for each supported service.  
Follow in order—do not skip steps or proceed to integrations until all API keys are obtained and stored securely.

---

## 1. Google (Gmail) API

### A. How to Obtain Gmail API Credentials
1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create or select a project.
3. Navigate to "APIs & Services" → "Library" → search for "Gmail API" → ENABLE.
4. Go to "Credentials" → "Create Credentials" → "OAuth client ID".
5. Configure the consent screen, set application type, and download `client_secret.json`.
6. **Store client ID and client secret securely.**

### B. Secure the Credentials
- Add these to your `.env` (or GitHub Secrets for production):
  ```
  GMAIL_CLIENT_ID=your-client-id
  GMAIL_CLIENT_SECRET=your-client-secret
  GMAIL_REDIRECT_URI=your-redirect-uri
  ```
- **Never commit `client_secret.json` or .env to Git.**
- See `knowledge-vault/GMAIL_OAUTH_SETUP.md` for troubleshooting.

---

## 2. Discord API

### A. How to Obtain Discord Bot Token  
1. Go to [Discord Developer Portal](https://discord.com/developers/applications).
2. Click "New Application" → name it → "Bot" tab → "Add Bot".
3. Click "Reset Token" and **copy the bot token**.
4. Under "OAuth2", set scopes and permissions as needed.

### B. Secure the Credentials
- Add to your `.env` (or GitHub Secrets):
  ```
  DISCORD_BOT_TOKEN=your-bot-token
  DISCORD_CLIENT_ID=your-client-id
  DISCORD_CLIENT_SECRET=your-client-secret
  ```
- **Never share or commit these!**

---

## 3. GitHub API

### A. How to Obtain a Personal Access Token (PAT)
1. Go to [GitHub Settings → Developer Settings → Personal Access Tokens](https://github.com/settings/tokens).
2. Generate new token, select required scopes (repo, workflow, etc), and copy it.

### B. Secure the Credentials
- Add to `.env` or GitHub Secrets:
  ```
  GITHUB_TOKEN=your-github-token
  ```
- **Never share PAT or commit to the repo.**

---

## 4. Stripe API

### A. How to Obtain Stripe API Keys
1. Log in to [Stripe Dashboard](https://dashboard.stripe.com/apikeys).
2. Copy the **publishable** and **secret** keys.

### B. Secure the Credentials
- Add to `.env` or GitHub Secrets:
  ```
  STRIPE_PUBLISHABLE_KEY=pk_live_xxx
  STRIPE_SECRET_KEY=sk_live_xxx
  ```

---

## 5. Perplexity AI

### A. How to Obtain Perplexity API Key
1. Log in to your [Perplexity AI account](https://www.perplexity.ai/).
2. Navigate to API section and generate a new key.

### B. Secure the Credentials
- Add to `.env` or GitHub Secrets:
  ```
  PERPLEXITY_API_KEY=your-perplexity-key
  ```

---

## 6. IBM watsonx

### A. How to Obtain watsonx API Credentials
1. Log in to [IBM Cloud](https://cloud.ibm.com/).
2. Create a watsonx project/service.
3. Go to "Service Credentials" and generate credentials.

### B. Secure the Credentials
- Add to `.env` or GitHub Secrets:
  ```
  WATSONX_API_KEY=your-watsonx-key
  WATSONX_PROJECT_ID=your-watsonx-project-id
  ```

---

## 7. Google Gemini (if required)

### How to Obtain Gemini API Key
1. Access [Google AI Studio](https://makersuite.google.com/app/apikey) or Google Cloud for Gemini.
2. Generate an API key.

### Secure the Credentials
- Add to `.env` or GitHub Secrets:
  ```
  GEMINI_API_KEY=your-gemini-key
  ```

---

## ✅ When complete:
- [ ] **Check all keys are present, tested, and NOT committed.**
- [ ] **Proceed to next issue: Security & Compliance Closure.**

---