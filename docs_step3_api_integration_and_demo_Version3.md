# 🦴 Step 3: Integration & Demo – Perplexity, watsonx, Gemini, etc. 🐾

**After security closure, follow this order for integrations and demos.  
No demo runs without security clearance!**

---

## 🎯 Integration Order

### 1. Perplexity Integration
- [ ] **Environment:**  
      Set and verify `PERPLEXITY_API_KEY` in `.env` or GitHub Secrets  
- [ ] **Demo:**  
      Run:  
      ```
      python integrations/perplexity/demo.py
      ```
- [ ] **Security:**  
      Confirm no credentials appear in logs or demo output

---

### 2. IBM watsonx Integration
- [ ] **Environment:**  
      Set `WATSONX_API_KEY` and `WATSONX_PROJECT_ID` in `.env` or GitHub Secrets  
- [ ] **Demo:**  
      Run:  
      ```
      python integrations/watsonx/demo.py
      ```
- [ ] **Security:**  
      Validate secure credential handling; no secrets in logs/output

---

### 3. Gemini Integration (Optional)
- [ ] **Environment:**  
      Configure `GEMINI_API_KEY` in `.env` or GitHub Secrets  
- [ ] **Module:**  
      Create `/integrations/gemini/` if not present  
- [ ] **Documentation:**  
      Update `/docs/integrations/gemini.md`, `README.md`, `CHANGELOG.md`, `SECURITY.md`
- [ ] **Demo:**  
      Add and run Gemini integration demo  
- [ ] **Security:**  
      Confirm all Gemini credentials are handled and logged securely

---

## 🛡️ Security Requirements (Active Throughout Integration)
- ✅ No secrets in code (use environment variables only)
- ✅ No secrets in logs (comply with logging policy)
- ✅ No secrets in docs (sanitize documentation)
- ✅ Escalate and block immediately if any credentials are exposed

---

## 📋 Integration Execution Plan

- **Phase 1:** Perplexity integration and demo
- **Phase 2:** watsonx integration and demo
- **Phase 3:** Gemini integration (if enabled)
- **Documentation:** Complete all result logs and security validation steps

---

🚨 **Critical Reminder:**  
Block and escalate if any compliance/security issues arise during integration.  
**Security first, demos second!** 🐾

---