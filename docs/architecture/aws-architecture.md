# ☁️ AWS Architecture Overview

WOOFY McWOOFSON runs on a secure, scalable AWS stack:

- **AWS Lambda:** Serverless compute for AI and integration logic.
- **API Gateway:** Secure, authenticated endpoints for client interaction.
- **S3:** Secure object/document storage.
- **KMS:** Encryption for all data at rest.
- **CloudWatch:** Centralized logging, monitoring, and alerting.
- **Cognito:** User authentication and access control.

---

## 🗺️ Architecture Diagram

![AWS Diagram](aws-architecture-diagram.png)

---

## 🐾 Logging & Monitoring

- All API calls, security events, and admin actions are logged in CloudWatch.
- Alerts are set for anomalous or unauthorized activity.

---

## 🔐 Security Practices

- Least privilege IAM roles for all AWS resources.
- Automatic key rotation for KMS and IAM credentials.
- Continuous compliance checks using AWS Config.

---

For deployment instructions, see `/scripts/deploy.sh` and the [Admin Guide](../admin-guide.md).