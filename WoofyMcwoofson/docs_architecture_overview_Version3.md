# System Overview
Maintained by BoozeLee, 2025-09-08

```mermaid
flowchart TD
  User --> API
  API --> Core[Core Services]
  Core --> Integrations
  Core --> Audit[(Audit Log)]
```