# 🦴 WOOFY Admin Guide

## 🛡️ Admin Responsibilities

- Manage user access via AWS Cognito/SSO.
- Configure and rotate secrets using AWS Secrets Manager.
- Monitor logs and alerts in AWS CloudWatch.
- Enforce branch and workflow protections in GitHub.

## 🔐 Managing Secrets

- NEVER commit secrets or credentials to the repo.
- Store secrets in:
  - `.env` (local, never committed)
  - GitHub Actions Secrets (`Settings > Secrets and variables > Actions`)
  - AWS Secrets Manager or SSM Parameter Store

## 🏗️ Deployment Checklist

- Update `.env` or AWS secrets as needed.
- Run `/scripts/deploy.sh` for deployment.
- Verify deployment status in CloudWatch and GitHub Actions.

## 🚑 Incident Response

- See `/docs/compliance/incident-response.md` for the playbook.

## 🆘 Onboarding/Offboarding

- Add/remove admins in AWS IAM and Cognito.
- Rotate secrets when an admin leaves.

---

For detailed platform setup, see `/docs/architecture/aws-architecture.md`.