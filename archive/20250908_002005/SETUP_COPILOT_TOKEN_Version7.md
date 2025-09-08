# 🐶🦴 Setting Up the COPILOT_TOKEN Secret for GitHub Actions

## Action Steps for BoozeLee

1. **Go to your repository on GitHub.**
2. **Navigate to:**  
   `Settings` → `Secrets and variables` → `Actions` → `New repository secret`
3. **Add the new secret:**
   - **Name:** `COPILOT_TOKEN`
   - **Value:** _(Paste your GitHub token here)_
   - Click **Save**.

## Usage

Once set, this secret will be available to reference in GitHub Actions workflows as `${{ secrets.COPILOT_TOKEN }}`.

---

**Please reply here once the secret is set up—I'll proceed with the next steps!**