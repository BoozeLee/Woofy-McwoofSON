# 🦴 How to Get Free Groq (Grok) API Access via OpenRouter

OpenRouter provides **free, limited-access** API keys for many top LLMs—including Groq-hosted and xAI’s Grok models.  
You’ll use your OpenRouter key with compatible tools (Cursor, LibreChat, Cline, etc.) to access Groq for free (within quota).

---

## 1. Register for OpenRouter

- Go to [https://openrouter.ai/](https://openrouter.ai/)
- Click **Sign Up** (top right)
- Register with email, GitHub, or Google

---

## 2. Verify Your Account

- Check your inbox for a verification email (it may take a minute)
- Click the verification link to activate your account

---

## 3. Generate Your API Key

- After logging in, click your user icon (top right) → **API Keys**
- Click **Create new key**
- Give it a name (e.g., “Woofy Groq Integration”)
- Copy your API key (**keep it secret!**)

---

## 4. Get Your Free Quota

- New users typically get free usage (e.g., 10 prompts per 2 hours for Grok/Groq models)
- Your dashboard will show current quota and refill time
- **Limits and availability change**—always check your OpenRouter dashboard

---

## 5. Using Your API Key

- Use this key with any OpenAI-compatible client (the endpoint is `https://openrouter.ai/api/v1`)
- For Groq/Grok models, select:
    - `x-ai/grok-3`
    - `x-ai/grok-4`
    - Or “Groq” if available in the model list

**Sample cURL:**
```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer sk-..." \
  -H "Content-Type: application/json" \
  -d '{
    "model": "x-ai/grok-3",
    "messages": [{"role":"user","content":"Hello Grok!"}]
  }'
```

---

## 6. Security & Compliance Reminders

- **Never share your API key** in chat, email, or code
- Store keys in `.env` (excluded by `.gitignore`) or a secure secrets manager
- Rotate if you suspect exposure

---

## 🐶 Handy Troubleshooting

- If you hit a quota limit, wait for your window to reset (shown on dashboard)
- For more free LLM APIs, see [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources)

---

**Now you’re ready to fetch some Groq/Grok completions—Woofy style! 🦴✨**