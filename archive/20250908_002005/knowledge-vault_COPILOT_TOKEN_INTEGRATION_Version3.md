# Copilot Token Integration

- Token securely stored as GitHub Secret: `COPILOT_TOKEN`
- Referenced in workflows as: `${{ secrets.COPILOT_TOKEN }}`
- Never committed to code or documentation
- For local use: distributed via encrypted channel, loaded into `.env` (gitignored) or direct OS env var

_Security review required before production use._