# Security Policy

- All secrets/tokens must be stored securely and rotated regularly (`see CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`)
- No passwords or tokens in code or version history
- Follow GitHub’s 2FA and least privilege best practices
- Escalate any suspected breach or exposure immediately to the project admin

## 🔒 Logging Policy (2025-09-07 Update)
- **Sensitive data (credentials, API keys, tokens, passwords) must never be logged, written to logs, or output to persistent storage.**
- **Any log file found to contain sensitive data must be immediately deleted and reported as a critical incident.**
- **All logs containing sensitive data must be purged within 2 days of creation.**
- **After any incident, all affected credentials must be rotated and a full incident report added to the security remediation log.**
- **Regularly audit extension/plugin logs (e.g., Amazon Q, Copilot, etc.) for compliance.**