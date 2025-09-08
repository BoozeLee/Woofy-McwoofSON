# 🔑 Secure API Key Retrieval & Usage – WOOFY McWOOFSON

## 1. Where Are API Keys Stored?

- All sensitive API keys (Perplexity, AWS, etc.) are stored as **GitHub Actions Encrypted Secrets**.
- No keys should ever be committed to code, logs, or config files in this repo.

---

## 2. How to Retrieve API Keys

### For GitHub Actions/CI:

- Secrets are automatically injected as environment variables in GitHub Actions workflows.
- **Usage Example in a GitHub Action:**
    ```yaml
    env:
      PERPLEXITY_API_KEY: ${{ secrets.PERPLEXITY_API_KEY }}
      AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    ```

### For Local Development/Server (MCP Server):

1. **Request Access:**
   - Contact the project admin or a CODEOWNER for permission to access required secrets.

2. **Fetch Keys Securely:**
   - In the GitHub repo:  
     - Go to **Settings** → **Secrets and variables** → **Actions**.
     - Only those with Admin/Owner permissions can view/add secrets.
     - If you are authorized, **copy the required key** (e.g., `PERPLEXITY_API_KEY`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`).

3. **Local Usage:**
   - **Never** paste keys into code or logs.
   - Place them in a local `.env` file (which is already in `.gitignore`).
   - Example `.env`:
        ```
        PERPLEXITY_API_KEY=your-key-here
        AWS_ACCESS_KEY_ID=your-key-here
        AWS_SECRET_ACCESS_KEY=your-key-here
        ```

4. **Environment Variables:**
   - Ensure your server or local app loads these keys via environment variables.

---

## 3. AWS Security Notes

- **Do NOT share AWS console credentials.** Use IAM users with least privilege.
- Rotate keys regularly (see `knowledge-vault/CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`).
- Store AWS keys only in GitHub Secrets, never in code.
- All IAM user actions should be logged and monitored (CloudTrail).
- If a key is suspected compromised, rotate and delete immediately.

---

## 4. Compliance

- **Never commit secrets** to the repo or share via chat/email.
- **All access requests and rotations must be logged** (see audit logs).
- Reference: [`knowledge-vault/SECURITY_POLICY.md`](knowledge-vault/SECURITY_POLICY.md)

---

## 5. Troubleshooting

- If you lack access or a secret is missing, request it from a CODEOWNER or project admin.
- For AWS credential setup, see [AWS IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

---

🐶 Questions? Bark at the security team or check the [Security Policy](knowledge-vault/SECURITY_POLICY.md)!