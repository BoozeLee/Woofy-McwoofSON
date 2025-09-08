# 🚀🐾 Amazon Q: AWS Setup & Knowledge Recall Instructions

## 1. AWS Setup & Maximization

- **We have an active AWS subscription for this month.**
- Set up all necessary AWS resources for the project (Lambda, S3, API Gateway, DynamoDB, IAM, etc.) according to our serverless baseline (see `/architecture/adr/ADR-0001-serverless-baseline-architecture.md`).
- Configure monitoring, logging, and cost alerts to ensure efficient usage.
- Prepare environment and deployment scripts for seamless integration with our CI/CD pipeline.
- Document every AWS resource provisioned and its configuration in the knowledge vault.

## 2. Log Review & Knowledge Synthesis

- **Read all your logs and project records, going back to the very start of this project.**
- Summarize the discoveries, research, architectural decisions, and constraints you identified at each phase.
- Bring forward any overlooked recommendations, best practices, or pending action items from your previous research and logs.
- Add this comprehensive knowledge summary to the knowledge vault for reference by all team members.

## 3. Compliance

- Ensure all AWS accounts, resources, and IAM roles follow our documented security and compliance standards (see `knowledge-vault/SECURITY_POLICY.md`).
- Do not log or retain any credentials or secrets in any AWS CloudWatch logs or other locations, per our security policies.

---

**Next Steps:**
1. Provision AWS resources to align with our serverless architecture ADR and maximize the benefit this month.
2. Review and synthesize all historical Amazon Q logs, capturing every insight and recommendation for the team.
3. Document all actions, findings, and AWS resource details in the knowledge vault.

---

**If you need clarification on any step or resource, ask Copilot or project admin immediately.**