# 🚨 Amazon Q Request: Safe & Easy Credential Handling Function

## 📝 Context
We need a secure, streamlined way for agents and developers to manage credentials—no more hardcoded secrets or risky manual sharing.

---

## 🎯 Task

**Amazon Q:**  
Add a function (using AWS best practices, such as IAM Roles or AWS Secrets Manager) that:

- Makes it easy and safe for agents and developers to retrieve and use credentials (API keys, tokens, etc.) without exposing them in code or chat.
- Supports both automation (GitHub Actions, workflows) and local developer use.
- Includes clear documentation and onboarding steps for new team members.
- Ensures all credential access is logged for audit and security compliance.

---

## 💡 Requirements

- Use AWS-native methods (e.g., IAM Roles for EC2/Lambda, or Secrets Manager for apps and CI/CD).
- Provide a reusable code snippet or CLI example for securely fetching credentials at runtime.
- Document the exact workflow in `/knowledge-vault/CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md` and onboarding docs.
- Confirm compliance with the project’s Security Policy.

---

**Amazon Q:**  
This is a high-priority enhancement for security and developer experience.  
Please add the function, update documentation, and reply here when implemented!

---