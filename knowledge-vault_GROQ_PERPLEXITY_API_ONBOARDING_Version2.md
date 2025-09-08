# 🦴 GROQ & Perplexity API Key Secure Onboarding

## Overview

This document ensures all team members and automation agents handle API keys for GROQ and Perplexity in a secure, compliant manner—aligned with enterprise security and Amazon Q/CoPilot Space requirements.

---

## 🔐 Secure Handling Steps

1. **Never share API keys via chat, email, or public docs.**
2. **Store all keys in your local `.env` file only** (excluded by `.gitignore`).
3. Use the provided automation script to inject/update keys:
    ```bash
    bash scripts/inject_api_keys.sh
    ```
   - This script will safely add/replace your API keys in `.env` without exposing them in logs or history.
4. For CI/CD (GitHub Actions), store keys as **encrypted repository secrets**:
    - `GROQ_API_KEY`
    - `PERPLEXITY_API_KEY`
5. **Never print, log, or expose keys in code or output.**

---

## 🏗️ Example `.env` (DO NOT COMMIT)

```
GROQ_API_KEY=your_groq_api_key_here
PERPLEXITY_API_KEY=your_perplexity_api_key_here
```

---

## 👨‍💻 Example Usage in Python

```python
import os
groq_key = os.getenv("GROQ_API_KEY")
perplexity_key = os.getenv("PERPLEXITY_API_KEY")
```

---

## 🚨 Incident Response

- If a key is ever exposed, **rotate immediately** and update `.env` and GitHub Secrets.
- Report any exposure in the `SECURITY_REMEDIATION_LOG.md`.

---

## 🦴 Woofy Rule

> Secrets belong in `.env` or encrypted vaults—never in chat, docs, or code!

---

_Keep this document in `knowledge-vault/` as the source of truth for all future onboarding and compliance checks._