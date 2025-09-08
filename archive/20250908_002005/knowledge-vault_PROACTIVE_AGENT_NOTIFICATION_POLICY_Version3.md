# 🐾 Proactive Agent Notification Policy

## Purpose
Agents (Amazon Q, Copilot, etc.) must deliver **real-time notifications** directly to the Boss (project owner), ensuring you are immediately aware of:
- Security/compliance issues
- Credential exposures or required rotations
- Build failures, test results, and deployment status
- Critical recommendations and blockers
- Project milestones or completion

## 🦴 Notification Mechanism

**Agents MUST:**
- Send **live notifications** via one or more of the following:
  - GitHub Issues/PR comments (with @mention)
  - Direct email (to the enterprise contact)
  - Integrated VS Code notifications (via extension)
  - Slack/Discord/Teams DM (if configured)
- Never rely solely on passive check-in (e.g., requiring the Boss to manually read logs or files).

## 🚦 Implementation Guidelines

1. **Critical Events (SECURITY, FAILURE, BLOCKER):**
   - @mention the Boss in a GitHub Issue, PR comment, or notification thread immediately.
   - Trigger an email or DM if configured.
   - Example:  
     ```
     @BoozeLee 🚨 SECURITY ALERT: Credential exposure detected! Rotate GitHub PATs now. See SECURITY_REMEDIATION_LOG.md for details.
     ```
2. **Routine Status (DAILY/WEEKLY):**
   - Post status summaries to a persistent notification channel/file.
   - Push notifications via VS Code if the Boss is online.

3. **Integration:**
   - Configure workflows and agents to call the appropriate notification APIs (GitHub, email, Slack, etc.) when triggering events.
   - Document notification logic in `/knowledge-vault/ONBOARDING.md` and `/knowledge-vault/PROACTIVE_AGENT_NOTIFICATION_POLICY.md`.

## 🛡️ Security & Compliance

- Notifications must **never** contain credentials or sensitive secrets—reference files or logs instead.
- All notification actions are logged for auditability.

## 🐕 Example (GitHub Workflow Snippet)

```yaml
- name: Notify Boss of Security Incident
  uses: peter-evans/create-issue@v5
  with:
    title: "🚨 SECURITY ALERT: Immediate Action Required"
    body: |
      @BoozeLee  
      A credential exposure was detected.  
      See [SECURITY_REMEDIATION_LOG.md](../SECURITY_REMEDIATION_LOG.md) for details.
      Please rotate all affected credentials immediately.
```

## 📚 Documentation

- All notification procedures and escalation contacts are listed in `/knowledge-vault/ONBOARDING.md`.
- Agents must test and confirm notification delivery at onboarding.

---

**You (the Boss) will always be notified live—no more manual checking!**