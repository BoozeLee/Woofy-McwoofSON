# 🐶🦴 How to Safely Get and Use a GitHub Token for Copilot in VS Code

This guide ensures your GitHub Personal Access Token (PAT) for Copilot is handled securely and works with VS Code’s authentication process.

> Prefer the built-in OAuth sign-in flow first. Only generate a PAT if the normal browser/device flow fails or you need headless automation.

---
## 1. Generate a Personal Access Token (PAT) on GitHub

1. Go to https://github.com and log in.
2. Profile → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**.
3. **Generate new token (classic)**.
4. Fill out:
   - Name: `VS Code Copilot`
   - Expiration: 30 days (short-lived preferred)
   - Scopes: check `copilot` (add `repo` only if repository access needed)
5. Generate and copy immediately. Store in a password manager (1Password, Bitwarden, etc.).

---
## 2. Sign into VS Code with GitHub (Preferred)

1. Open VS Code.
2. Click **Accounts** icon in Activity Bar.
3. Choose **Sign in with GitHub to use GitHub Copilot**.
4. Complete browser OAuth authorization.
5. Copilot activates automatically (ghost suggestions appear when typing code).

---
## 3. Manually Add the Token (Fallback)

If browser/device sign-in fails:
```
Ctrl+Shift+P → "GitHub Copilot: Sign in" → paste token
```
Or Settings: search "GitHub Copilot Personal Access Token" and paste there.

---
## 4. Verify Copilot is Working

- Open a `.py` or `.js` file and start typing → ghost suggestion appears → accept with `Tab`.
- Command Palette: `GitHub Copilot: Status` should show `Authenticated`.
- If issues: `GitHub Copilot: Sign out` → restart VS Code → sign in again.

---
## 5. Keep Your Token Safe

- Never commit, paste in code, or share publicly.
- Store only in a password manager.
- Revoke immediately if leaked: GitHub → Settings → Developer settings → Personal access tokens.
- Use short expiration and rotate proactively.

---
## 🐾 Troubleshooting

| Issue | Fix |
|-------|-----|
| Invalid token | Sign out/in; verify Copilot subscription active. |
| No suggestions | Check status, ensure file type supported, disable conflicting extensions. |
| Network/proxy block | Use device flow; ensure `api.github.com` reachable. |
| Wrong account | Sign out from Accounts menu; log into correct GitHub user. |
| Persisting auth errors | Clear VS Code auth: Command Palette → `Developer: Open Authentication Log` & review. |

---
## 🦴 Why This is Safe

- PAT transmitted over TLS.
- OAuth flow avoids manual token handling in most cases.
- Scope minimization reduces blast radius.
- Rotation + short expiry limit exposure window.

---
## 🔐 Security Notes

- Do NOT place the PAT into environment files committed to the repo.
- For CI automation, prefer GitHub Actions OIDC or repo secrets, not a Copilot PAT.
- If using multiple machines, generate distinct short-lived tokens per device rather than sharing one.

---
_For more, see GitHub Copilot Docs and VS Code Copilot FAQ._
