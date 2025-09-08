# Architecture Decision Records (ADR)

This directory contains Architecture Decision Records (ADRs) that document important architectural decisions made for the WOOFY McWOOFSON platform.

## ADR Format

Each ADR follows the [Michael Nygard ADR format](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions):

- **Title**: Short descriptive title
- **Status**: Proposed, Accepted, Deprecated, Superseded
- **Context**: Situation leading to the decision
- **Decision**: What was decided and why
- **Consequences**: Results and implications

## Current ADRs

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| [001](001-serverless-baseline-architecture.md) | Serverless Baseline Architecture | Accepted | 2025-09-07 |
| [002](002-modular-lambda-action-dispatch.md) | Modular Lambda Action Dispatch | Proposed | 2025-09-08 |

## How to Create a New ADR

1. Create a new file with the next sequential number (e.g., `002-new-decision.md`)
2. Follow the standard ADR template
3. Update this index file
4. Submit as part of a pull request for review

## ADR Workflow

1. **Proposed**: Initial draft for discussion
2. **Accepted**: Decision implemented and active
3. **Deprecated**: Decision no longer recommended
4. **Superseded**: Replaced by a newer ADR

---

*For questions about ADRs or architectural decisions, contact the enterprise architecture team.*