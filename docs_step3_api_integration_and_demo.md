# 🦴 Step 3: Integration & Demo – Perplexity, watsonx, Gemini, etc.

**Once security is closed, use this order for API integrations and tests.**

---

## 1. Perplexity Integration
- [ ] Ensure `PERPLEXITY_API_KEY` is in `.env`/GitHub Secrets
- [ ] Run:  
  ```
  python integrations/perplexity/demo.py
  ```
- [ ] Document/test results

---

## 2. IBM watsonx Integration
- [ ] Ensure `WATSONX_API_KEY` and `WATSONX_PROJECT_ID` are set
- [ ] Run:  
  ```
  python integrations/watsonx/demo.py
  ```
- [ ] Document/test results

---

## 3. Gemini Integration (if enabled)
- [ ] Ensure `GEMINI_API_KEY` is set
- [ ] Add `/integrations/gemini/` module (if not present)
- [ ] Document setup in `/docs/integrations/gemini.md`
- [ ] Add to `README.md`, `CHANGELOG.md`, `SECURITY.md`
- [ ] Run demo/tests

---

## 4. General Security Reminders
- [ ] No secrets in code, logs, or docs
- [ ] All test results and integration steps are documented in the knowledge vault

---

**Block and escalate if any compliance/security issues arise during integration.**