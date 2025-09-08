# 🐶🦴 How to Safely Get and Use a GitHub Token for Copilot in VS Code

This guide ensures your GitHub Personal Access Token (PAT) for Copilot is handled securely and works with VS Code’s authentication process.

---

## 1. Generate a Personal Access Token (PAT) on GitHub

- Go to [GitHub](https://github.com) and log in.
- Click your profile photo > **Settings**.
- In the left sidebar, click **Developer settings** > **Personal access tokens** > **Tokens (classic)**.
- Click **Generate new token** > **Generate new token (classic)**.
- Fill out:
  - **Name**: (e.g., "VS Code Copilot")
  - **Expiration**: Prefer a short period (e.g. 30 days)
  - **Scopes**: At minimum, select `copilot`. Add `repo` if you need repo access.
- Click **Generate token** and **copy it now**. Store it in a password manager.

---

## 2. Sign into VS Code with GitHub

- Open VS Code.
- Click the **Accounts** icon in the Activity Bar (left side).
- Choose **Sign in with GitHub to use GitHub Copilot**.
- Browser opens: log in and authorize as prompted.
- After successful authentication, Copilot should activate automatically in VS Code.

---

## 3. Manually Add the Token (if Needed)

If browser sign-in fails:
- Open Command Palette: `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac).
- Type and select **GitHub Copilot: Sign in**.
- Paste your PAT when prompted.
- OR: Open **Settings** (`Ctrl+,`), search for `GitHub Copilot: Personal Access Token`, and paste your PAT.

---

## 4. Verify Copilot is Working

- Open a code file (e.g., `.py` or `.js`).
- Start typing—Copilot suggestions (ghost text) should appear. Accept with `Tab`.
- Check the Copilot icon in the VS Code Status Bar (bottom). If not active:
  - Command Palette > **GitHub Copilot: Sign out**
  - Restart VS Code and sign in again.

---

## 5. Keep Your Token Safe

- **Never share your token** in code, chats, or email.
- Store tokens in a password manager (e.g., 1Password, Bitwarden).
- If compromised, revoke it in GitHub > **Settings > Developer settings > Personal access tokens**.
- Prefer short expiration periods for security.

---

## 🐾 Troubleshooting

- **"Invalid Copilot token" error**: Sign out, restart VS Code, and sign in again. Confirm your account has an active Copilot subscription.
- **Network/Proxy issues**: If `github.com/login` is blocked, use manual token entry. Ensure `api.github.com` is accessible.
- **Wrong account**: Sign out via Accounts menu and sign in with the correct GitHub account.

---

## 🦴 Why This is Safe

- PAT is encrypted in transit.
- GitHub’s OAuth flow avoids exposing the token in most cases.
- Limiting scope to `copilot` reduces risk.
- Regular token rotation enhances security.

---

_For more, see [GitHub Copilot Docs](https://docs.github.com/en/copilot) or [VS Code Copilot FAQ](https://code.visualstudio.com/docs/copilot/faq)._
