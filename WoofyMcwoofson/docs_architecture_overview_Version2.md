# 🏗️ Bakery Street Project Architecture

Maintained by BoozeLee, 2025-09-08

## System Overview

```mermaid
flowchart TD
    User[User/Client] -->|REST API| Gateway
    Gateway -->|Auth & Routing| CoreServices
    CoreServices -->|Integrations| [Gmail, AWS, Discord, Stripe, Google Drive]
    CoreServices -->|Knowledge Vault| DocsDB
    CoreServices -->|Audit Logging| AuditLog
```

## Sequence: Automation Run

```mermaid
sequenceDiagram
    participant U as User
    participant API as Gateway/API
    participant CS as Core Service
    participant EXT as External API

    U->>API: POST /automation/run
    API->>CS: Validate + route request
    CS->>EXT: Trigger service integration (e.g., Google Drive)
    EXT-->>CS: Result/confirmation
    CS-->>API: Run started (runId/status)
    API-->>U: 202 Accepted (runId)
```

## Security Data Flow

```mermaid
graph LR
    Sec1[Credential Rotation] --> Sec2[.env & GitHub Secrets]
    Sec2 --> Sec3[Runtime Injection]
    Sec3 --> Sec4[Audit Log]
```

---

## Reference

- [API Spec](../openapi.yaml)
- [Knowledge Vault](../../knowledge-vault/README.md)