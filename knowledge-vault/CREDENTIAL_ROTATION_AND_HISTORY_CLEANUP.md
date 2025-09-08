# 🐕 WOOFY McWOOFSON - Credential Rotation & History Cleanup

**Version:** 1.0  
**Last Updated:** 2025-01-27  
**Critical:** Follow these procedures exactly to maintain security  

## 🔄 Credential Rotation Procedures

### AWS Credentials
1. **Generate new AWS access keys**
   ```bash
   aws iam create-access-key --user-name woofy-service-user
   ```
2. **Update environment variables**
   - Update AWS Secrets Manager entries
   - Update CI/CD pipeline secrets
   - Update local development environments
3. **Test new credentials**
   - Verify all services can authenticate
   - Run integration tests
4. **Deactivate old credentials**
   ```bash
   aws iam delete-access-key --access-key-id OLD_KEY_ID --user-name woofy-service-user
   ```

### API Keys & Tokens
1. **Generate new keys** in respective service dashboards
2. **Update secrets storage**
   - AWS Secrets Manager
   - GitHub repository secrets
   - Environment configurations
3. **Deploy updated configurations**
4. **Revoke old keys** after successful deployment

### Database Credentials
1. **Create new database user** with same permissions
2. **Update connection strings** in all applications
3. **Test database connectivity**
4. **Drop old database user**

## 🧽 Repository History Cleanup

### 🚨 If Secrets Are Found in History

#### Immediate Actions
1. **ROTATE ALL EXPOSED CREDENTIALS IMMEDIATELY**
2. **Document the exposure** in SECURITY_REMEDIATION_LOG.md
3. **Notify security team** within 1 hour

#### History Cleanup Tools

**Option 1: BFG Repo-Cleaner (Recommended)**
```bash
# Download BFG
wget https://repo1.maven.org/maven2/com/madgag/bfg/1.14.0/bfg-1.14.0.jar

# Remove secrets from history
java -jar bfg-1.14.0.jar --replace-text secrets.txt repo.git
cd repo.git
git reflog expire --expire=now --all && git gc --prune=now --aggressive
```

**Option 2: git-filter-branch**
```bash
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch path/to/secret/file' \
  --prune-empty --tag-name-filter cat -- --all
```

**Option 3: GitHub Secret Scanning**
- Enable GitHub secret scanning
- Review and remediate all detected secrets
- Use GitHub's secret scanning API for automation

### 📋 Post-Cleanup Verification
1. **Scan entire history** for remaining secrets
   ```bash
   git log --all --full-history -- "*.env" "*secret*" "*key*"
   ```
2. **Verify all credentials rotated**
3. **Update security documentation**
4. **Force push cleaned repository** (if necessary)
   ```bash
   git push origin --force --all
   git push origin --force --tags
   ```

## 📅 Rotation Schedule

### Mandatory Rotation Intervals
- **AWS Access Keys:** Every 90 days
- **API Keys:** Every 90 days
- **AI Service Tokens (Perplexity, watsonx, Gemini):** Every 90 days
- **Database Passwords:** Every 180 days
- **Service Account Tokens:** Every 30 days

### Emergency Rotation Triggers
- Suspected credential compromise
- Employee departure
- Security incident
- Compliance requirement

## 📝 Documentation Requirements

For every rotation:
1. **Log the action** in SECURITY_REMEDIATION_LOG.md
2. **Update credential inventory**
3. **Notify relevant teams**
4. **Verify all services operational**

## 🎆 Automation

### Automated Rotation (Recommended)
```yaml
# GitHub Actions example
name: Credential Rotation
on:
  schedule:
    - cron: '0 2 1 */3 *'  # Every 3 months
jobs:
  rotate:
    runs-on: ubuntu-latest
    steps:
      - name: Rotate AWS Keys
        run: |
          # Automated rotation script
          ./scripts/rotate-aws-credentials.sh
```

## 📋 AUDIT LOG

- _2025-09-07_ Set up secure credential management for new AI integrations (Perplexity, IBM watsonx, Google Gemini); created comprehensive .env template with placeholders; implemented environment-based credential loading; updated rotation schedule for AI services; verified .gitignore protection – Kilo Code
- _2025-01-27_ Rotated Amazon Q, Gmail, Discord, GitHub, Stripe credentials after log file exposure; scrubbed repo history; updated all `.env` files and notified all agents – Kilo Code

---

_Fill in new entries for each rotation event. Escalate if any secrets are found exposed or if rotation cannot be completed._

---
**🚨 CRITICAL:** Never commit real credentials to version control!  
**🐕 WOOFY's Rule:** When in doubt, rotate it out! 🔄
