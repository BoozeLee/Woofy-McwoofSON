# GROQ & Perplexity API Key Onboarding

## Secure API Key Handling

- **Do NOT share API keys in chat, email, or public files.**
- **Store locally** in a `.env` file (excluded by `.gitignore`):

    ```
    GROQ_API_KEY=your_groq_api_key_here
    PERPLEXITY_API_KEY=your_perplexity_api_key_here
    ```

- **For GitHub Actions/CI:**  
  Store keys as GitHub encrypted secrets:  
    - `GROQ_API_KEY`
    - `PERPLEXITY_API_KEY`

## Usage in Code

```python
import os

groq_key = os.getenv("GROQ_API_KEY")
perplexity_key = os.getenv("PERPLEXITY_API_KEY")
```

## Best Practices

- Rotate API keys regularly (see `CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`)
- Never log or print full API keys
- Remove API keys from `.env` before sharing machines or code