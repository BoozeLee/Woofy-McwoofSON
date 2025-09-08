# 🚨 URGENT: MCP Server & GitHub Token Integration for Agents

**Date:** 2025-09-08  
**Prepared by:** Copilot Space, BoozeLee

---

Below are step-by-step, role-specific instructions for each agent.  
**All actions are mandatory. Deployment and monetization are blocked until compliance is confirmed.**

---

## 1. 🐾 For Copilot (GitHub Copilot Agent)

**Objective:**  
Automate code additions/changes to the repository using the MCP server and the new GitHub token.

**Instructions:**
- Use the MCP server as the only gateway for all GitHub API actions.
- Access the GitHub token exclusively via repository secrets or the MCP server’s secure environment.
- For each automation, workflow, or script:
  - Reference `${{ secrets.GITHUB_TOKEN }}` in GitHub Actions, or use MCP-provided endpoints.
  - Do NOT output or log the
