# Security Policy

- All secrets/tokens must be stored securely and rotated regularly (`see CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`)
- No passwords or tokens in code or version history
- Use `.env` for local development, protected by `.gitignore`
- Escalate any suspected breach or exposure immediately to the project admin
- Never share credentials in chat, email, or unprotected files