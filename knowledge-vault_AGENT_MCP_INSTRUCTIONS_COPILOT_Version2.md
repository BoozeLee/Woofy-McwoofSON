# 🐶 Copilot Agent: Secure Automation Workflow

**Your Mission:**  
All repo changes, code pushes, and automations must go through the MCP server using secrets from AWS or GitHub Actions.  
**Never use or request raw API keys.**

---

## What You Must Do:

1. **Access GitHub & APIs ONLY via MCP server or GitHub Actions.**
   - Use `${{ secrets.GITHUB_TOKEN }}` for all workflows—never expose it.
   - Perform all file additions or repo changes through automation or the GitHub web UI, not manual tokens.

2. **Remove Local Credentials:**
   - Delete any `.env`, `api_keys.json`, or config files containing secrets after migration.  
   - Do not copy or share secrets.

3. **Compliance & Logging:**
   - Log your completed actions and compliance in:  
     `knowledge-vault/CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`  
   - Never log or screenshot secrets.

4. **If MCP Server Fails:**  
   - Escalate to KiloCoder or BoozeLee immediately.  
   - Do not proceed with local secrets.

---

**Remember:**  
All automation must go through secure, approved channels.  
“No paws on plaintext credentials!”