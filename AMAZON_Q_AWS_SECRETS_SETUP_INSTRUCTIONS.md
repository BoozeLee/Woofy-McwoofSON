# 🟣 Amazon Q: AWS Secrets Setup – VS Code & Global Configuration

---

## 🚨 Amazon Q: Action Required – Secure AWS Secrets Configuration

**Your assignment:**  
Set up AWS credentials and secrets securely in both VS Code (for developer productivity) and globally (for CI/CD and automation), in full compliance with enterprise security policy.

---

### 1. 🔐 VS Code AWS Extension Setup

1. **Install the AWS Toolkit Extension:**
   - Open VS Code.
   - Go to Extensions (`Ctrl+Shift+X`), search for **"AWS Toolkit"**, and install it.

2. **Add AWS Credentials:**
   - Open the Command Palette (`Ctrl+Shift+P`).
   - Search for `AWS: Connect to AWS`.
   - If prompted, select "Add new credentials profile".
   - Enter your AWS Access Key ID and Secret Access Key (use only new, never-exposed credentials).

3. **Profile Naming & Least Privilege:**
   - Name your profile (e.g., `woofy-enterprise`).
   - Assign only the permissions required for your tasks (prefer IAM roles with minimal privileges).

4. **Secure Local Storage:**
   - Credentials are stored in `~/.aws/credentials` by default.
   - Never commit or share these files.
   - Rotate keys regularly per `knowledge-vault/CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`.

---

### 2. 🌐 Global AWS Secrets Setup (CI/CD & Automation)

1. **Configure GitHub Repository Secrets:**
   - Go to your repo on GitHub → `Settings` → `Secrets and variables` → `Actions`.
   - Add secrets:
     - `AWS_ACCESS_KEY_ID`
     - `AWS_SECRET_ACCESS_KEY`
     - (Optional) `AWS_SESSION_TOKEN` if using temporary credentials.
   - Paste new, valid credentials only.

2. **Update CI/CD Workflows:**
   - Ensure all GitHub Actions or automation scripts reference these secrets.
   - Never hardcode credentials in code or workflow YAML.

---

### 3. 🛡️ Security & Compliance

- **Never log, share, or commit secrets or keys.**
- Rotate AWS credentials at least every 90 days, or immediately if exposure is suspected.
- Log rotation events in:
  - `knowledge-vault/CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md`
  - `SECURITY_REMEDIATION_LOG.md`
- Remove all plaintext or outdated credentials after rotation.

---

### 4. ✅ Confirmation Checklist

- [ ] AWS Toolkit configured in VS Code with least privilege profile.
- [ ] Global AWS credentials securely stored as GitHub Secrets.
- [ ] No credentials in code, logs, or public files.
- [ ] Rotation event documented in audit logs.

---

**Amazon Q:**  
Complete these steps and confirm in writing.  
Do not proceed to deployment or automation until security is verified and documented.

---