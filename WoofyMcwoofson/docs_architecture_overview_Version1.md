# 🏗️ Bakery Street Project Architecture

Maintained by BoozeLee, 2025-09-08

## High-Level System Diagram

```mermaid
flowchart TD
    User[User/Client] -->|REST API| Gateway
    Gateway -->|Auth & Routing| CoreServices
    CoreServices -->|Integrations| [Gmail, AWS, Discord, Stripe, Google Drive]
    CoreServices -->|Knowledge Vault| DocsDB
    CoreServices -->|Audit Logging| AuditLog
```

## Key Components

- **Gateway:** Handles authentication, rate-limiting, API versioning.
- **CoreServices:** Business logic, workflow orchestration, credential handling.
- **Integrations:** Secure connectors for external APIs (Gmail, AWS, etc).
- **Knowledge Vault:** Centralized technical/business documentation.
- **AuditLog:** Persistent security and compliance event storage.

## Security Principles

- No secrets in code or history.
- All external calls authenticated and audited.
- Least-privilege access enforced.

---

## 🐾 See also
- [openapi.yaml](../openapi.yaml)
- [knowledge-vault/SECURITY_POLICY.md](../../knowledge-vault/SECURITY_POLICY.md)