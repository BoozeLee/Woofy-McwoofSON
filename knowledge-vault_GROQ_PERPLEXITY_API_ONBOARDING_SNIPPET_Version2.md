# 🦴 Secure GROQ & Perplexity API Key Onboarding

## Security Protocol

- **Never share API keys in chat, email, or public docs.**
- **Store keys ONLY in your local `.env` file (excluded by `.gitignore`).**
- Use the automation script `scripts/inject_api_keys.sh` to safely update your `.env`.

## Steps

1. Obtain your GROQ and Perplexity API keys from the project lead (never via insecure channels).
2. Run the injector script:
   ```bash
   bash scripts/inject_api_keys.sh
   ```
3. Follow prompts to securely enter your keys (they won’t be displayed).
4. Confirm `.env` now contains:
   ```
   GROQ_API_KEY=...
   PERPLEXITY_API_KEY=...
   ```
5. **Never commit `.env` to git.** If you ever see it in version control, alert the team!

## Usage in Code

```python
import os
groq_key = os.getenv("GROQ_API_KEY")
perplexity_key = os.getenv("PERPLEXITY_API_KEY")
```