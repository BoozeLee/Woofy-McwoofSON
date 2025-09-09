# 📚 Woofy McWoofson Documentation

**Maintained by:** BoozeLee, 2025-09-08  
**Purpose:** Enterprise documentation hub for Woofy McWoofson AI Assistant

## 📋 Documentation Index

### 🏗️ Architecture
- **[architecture/overview.md](architecture/overview.md)** - System architecture and design
- **[architecture/aws-architecture.md](architecture/aws-architecture.md)** - AWS infrastructure design
- **[architecture/operational-workflow.md](architecture/operational-workflow.md)** - Kilo Code operational workflow

### 🔌 API Documentation
- **[openapi.yaml](openapi.yaml)** - Complete API specification
- **API Base URL:** `https://api.bakerystreet.example.com/v1`
- **Authentication:** API Key required (`X-API-Key` header)

### 🤖 AI Assistant Guidelines
- **[chapter1-introduction.md](chapter1-introduction.md)** - Chapter 1 introduction and core capabilities
- **[chapter2-architect-code-workflow.md](chapter2-architect-code-workflow.md)** - Chapter 2 architect and code mode workflow
- **[chapter3-mode-management.md](chapter3-mode-management.md)** - Chapter 3 mode management and custom modes
- **[practical-workflow-examples.md](practical-workflow-examples.md)** - Chapter 3 workflow examples (legacy)
- **[chapter4-advanced-modes.md](chapter4-advanced-modes.md)** - Chapter 4 advanced mode usage and orchestration
- **[chapter5-tool-usage.md](chapter5-tool-usage.md)** - Chapter 5 effective tool use and code indexing
- **[kilo-code-guidelines.md](kilo-code-guidelines.md)** - Kilo Code operational guidelines
- **[architecture/operational-workflow.md](architecture/operational-workflow.md)** - Operational workflow diagram

### 🎨 Branding & Assets
- **[../branding/README.md](../branding/README.md)** - Brand guidelines and assets
- **Logo Usage:** Enterprise compliance required
- **Color Palette:** Defined in branding directory

### 🚀 Deployment Guides
- **[../AWS_CENTRALIZED_CREDENTIAL_MANAGEMENT.md](../AWS_CENTRALIZED_CREDENTIAL_MANAGEMENT.md)** - AWS credential setup
- **[../infrastructure/woofy-infrastructure.yaml](../infrastructure/woofy-infrastructure.yaml)** - CloudFormation templates

### 🔐 Security Documentation
- **[../SECURITY.md](../SECURITY.md)** - Security policy and reporting
- **[../knowledge-vault/SECURITY_POLICY.md](../knowledge-vault/SECURITY_POLICY.md)** - Detailed security procedures

## 🛠️ Quick Start

1. **API Access:** Obtain API key from BoozeLee
2. **Authentication:** Include `X-API-Key` header in all requests
3. **Health Check:** `GET /woof` - Returns "Woof! 🐾 The API is live."
4. **Documentation:** Review OpenAPI spec for complete endpoint list

## 🚀 Mode Switching & Operational Workflows

### Quick Start Guide
- **Architect Mode**: Use `/architect` for planning, design, and system architecture
- **Code Mode**: Use `/code` for implementation, coding, and file modifications
- **Debug Mode**: Use `/debug` for troubleshooting and issue resolution
- **Ask Mode**: Use `/ask` for technical guidance and explanations

### Best Practices
1. **Start with Architect Mode** for new features and complex tasks
2. **Switch to Code Mode** when ready to implement approved designs
3. **Use Debug Mode** when encountering issues during development
4. **Confirm mode switches** explicitly in conversation to avoid confusion

### Key Resources
- **[Kilo Code Guidelines](kilo-code-guidelines.md)**: Complete operational instructions
- **[Practical Workflow Examples](practical-workflow-examples.md)**: Real-world implementation examples
- **[Operational Workflow Diagram](architecture/operational-workflow.md)**: Visual process overview
- **[Custom Modes Configuration](../../custom_modes.yaml)**: Project-specific mode definitions

### Custom Mode Creation
Create specialized modes using:
- **Interactive**: "Create a mode called 'Security Reviewer' for code analysis"
- **UI Panel**: Use VS Code Kilo Code panel → Prompts tab
- **Configuration**: Edit `custom_modes.yaml` or `.kilocodemodes`

## Prompt kit

Reusable prompts for Copilot Chat across VS Code and GitHub.com live in `docs/prompts/`:
- `feature.md`
- `bugfix.md`
- `tests.md`
- `security-review.md`
- `api-change.md`
- `commit-messages.md`

These are copy-friendly, secrets-free, and aligned with our enterprise checklists.

## � Support

- **Technical Issues:** See [../SUPPORT.md](../SUPPORT.md)
- **Security Reports:** security@bakery-street-projct.com
- **General Contact:** BoozeLee

---

**🐾 Woof! Documentation is the best friend of every developer.** 📖