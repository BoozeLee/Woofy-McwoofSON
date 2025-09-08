# 🐶 GitHub Copilot MCP Server Setup – Enterprise & Audit-Ready

## Overview

This guide walks you through the secure, compliant setup of the GitHub Copilot MCP (Managed Context Provider) Server for use in your repo, in line with all enterprise security and audit requirements.

---

## 1. 📦 Prerequisites

- **Private repo** with branch protection and CODEOWNERS enabled.
- **Admin** access to GitHub org/repo and Actions.
- All secrets managed via GitHub Secrets or encrypted vaults.
- Audit logging enabled (`knowledge-vault/CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`).

---

## 2. 🦴 MCP Server Deployment (Zero-Exposure Steps)

### a. **Create a new directory for MCP server**
```bash
mkdir -p integrations/github-mcp-server
cd integrations/github-mcp-server
```

### b. **Clone MCP server repo**
```bash
git clone https://github.com/github/copilot-mcp-server .
```

### c. **Install dependencies**
```bash
npm install
# Or, if using yarn:
# yarn install
```

### d. **Configure secure environment variables**
Add the following to your `.env` (never commit the values!):

```
GITHUB_APP_ID=
GITHUB_APP_PRIVATE_KEY=
GITHUB_APP_CLIENT_ID=
GITHUB_APP_CLIENT_SECRET=
GITHUB_WEBHOOK_SECRET=
MCP_SERVER_SECRET=
```

- Store these in GitHub Secrets for Actions workflows.
- Log rotation in `knowledge-vault/CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`.

### e. **Set up MCP configuration**
- Copy and edit `config.example.yaml` to `config.yaml`.
- Set all URLs and org/repo names to match your environment.
- Do NOT embed secrets in config files.

### f. **Run MCP server locally for testing**
```bash
npm run start
# Or, for Docker:
# docker build -t github-mcp-server .
# docker run --env-file .env -p 8080:8080 github-mcp-server
```

### g. **Add MCP server (and config) to `.gitignore` if it contains secrets**
```
integrations/github-mcp-server/.env
integrations/github-mcp-server/config.yaml
```

---

## 3. 🛡️ Security & Compliance

- **NO credentials** in code, logs, or chat.
- All key rotations and updates must be logged for audit.
- Enable secret scanning and branch protection for all MCP-related branches.
- Document all steps, issues, and handoffs in the knowledge vault.

---

## 4. 🧪 Testing

- Run all integration and security tests (`pytest -k security`).
- Confirm MCP server can connect to GitHub, and Copilot context is available.
- Validate no credentials are leaked in logs or artifacts.

---

## 5. 📝 Audit Log Entry Example

Add this to your credential rotation file:
```
2025-09-08T03:20:00Z – MCP server app credentials generated, stored in .env & GitHub Secrets, old tokens revoked – BoozeLee
```

---

## 6. 🏁 Handoff

- Document MCP server setup and config in this file and `DETAILED_TRANSITION_REPORT.md`.
- Store no secrets in chat, screenshots, or docs.
- Confirm operational status to Amazon Q and next agent.

---

**No paws on plaintext credentials!** 🐶🦴

_Reference: [GitHub Docs – MCP Server](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/use-the-github-mcp-server)_