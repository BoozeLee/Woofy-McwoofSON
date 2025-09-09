## Summary

Describe the change and its impact.

## Checks
- [ ] Repo remains private-by-default (see Private Visibility Guard)
- [ ] No secrets added (local secret scan passes)
- [ ] Docs updated if behavior changes

## Links
- Private release policy: `docs/enterprise/PRIVATE_RELEASE_POLICY.md`
- Org hardening checklist: `docs/enterprise/ORG_HARDENING_CHECKLIST.md`

# 🐾 WOOFY McWOOFSON - Enterprise Pull Request

## 🎯 What does this PR do?
_Describe the changes and their business impact_

## 🧪 How was this tested?
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed
- [ ] Security scan clean

## 📋 Enterprise Compliance Checklist

### Security & Compliance
- [ ] No secrets or sensitive data committed
- [ ] Security scan passed (detect-secrets, CodeQL)
- [ ] Dependencies reviewed for vulnerabilities
- [ ] Input validation implemented
- [ ] Authentication/authorization verified

### Code Quality
- [ ] Lint and tests pass (`make lint` and `make test`)
- [ ] Code follows enterprise standards
- [ ] Documentation updated
- [ ] CHANGELOG updated (if applicable)
- [ ] ADR created for architectural changes

### Enterprise Requirements
- [ ] Compliance with data residency requirements
- [ ] Audit logging implemented
- [ ] Performance impact assessed
- [ ] Scalability considerations addressed
- [ ] Monitoring/alerting configured

## 🔍 Reviewer Notes
_Anything the reviewer should pay special attention to? Security implications? Breaking changes?_

## 🚀 Deployment Notes
_Special deployment considerations or rollback plan?_

## 📊 Business Impact
_How does this change support our revenue goals and partner attraction?_

---

## 💡 Prompt Kit (copy or open)
- Feature: docs/prompts/feature.md
- Bugfix: docs/prompts/bugfix.md
- Tests: docs/prompts/tests.md
- Security review: docs/prompts/security-review.md
- API change: docs/prompts/api-change.md
- Commits: docs/prompts/commit-messages.md

> Tip: open these files in VS Code or GitHub and copy the blocks into Copilot Chat on either surface.