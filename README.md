# Woofy-McwoofSON

The "bakery-street-project/Woofy-McwoofSON" Python project is meticulously organized with a wide range of documentation, installation scripts, AWS management files, deployment checklists, orchestrator reports, compliance documents, enterprise-level instructions, demo scripts, and comprehensive README files. The vision emphasizes protecting the webhook endpoint by verifying its signature using GitHub's WEBHOOK_SECRET for secure communication. The plan includes detailed steps such as analysis, sta

## Vision

The "bakery-street-project/Woofy-McwoofSON" Python project is meticulously organized with a wide range of documentation, installation scripts, AWS management files, deployment checklists, orchestrator reports, compliance documents, enterprise-level instructions, demo scripts, and comprehensive README files. The vision emphasizes protecting the webhook endpoint by verifying its signature using GitHub's WEBHOOK_SECRET for secure communication. The plan includes detailed steps such as analysis, stack assessment, identifying missing components, exploring monetization strategies, considering potential Lua integrations, ensuring robust security measures, addressing TODO items, and assessing required effort. Overall, the project is designed with strong security practices and comprehensive documen

## Features

- Developed in **Python**
- Well-structured and maintainable codebase
- Integration ready for development workflows
- Comprehensive documentation
- 1. **Documentation Files**: ADR-future-template.md, ADR-middleware-stub.md, etc.
- 2. **Installation Scripts**: AUTO_MODE_BLOCKED_ACTIONS.md, AUTO_MODE_PROTOCOL.md, AUTO_MODE_STATUS.md
- 3. **AWS Management**: AWS_CENTRALIZED_CREDENTIAL_MANAGEMENT.md, AWS_SECURE_SETUP_GUIDE.md, AWS_SETUP_COMPREHENSIVE_PLAN.md
- 4. **Deployment and Execution**: DEPLOYMENT_EXECUTION_CHECKLIST.md, DEPLOYMENT_STATUS.md
- 5. **Orchestrator Reports**: ORCHESTRATOR_COMMUNICATION_LOG.md, ORCHESTRATOR_UPDATE_REPORT.md

## Quick Start

### Prerequisites
- Python 3.9+
- pip
- Virtual environment (venv or conda)

### Installation
```bash
git clone https://github.com/bakery-street-project/Woofy-McwoofSON.git
cd Woofy-McwoofSON
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # then set WEBHOOK_SECRET
```

### Usage
```bash
# Run the webhook server (GitHub signature verification + autonomous scheduler)
WEBHOOK_SECRET=$(openssl rand -hex 32) python main.py

# Endpoints
curl http://127.0.0.1:8080/health   # agent health probe
curl http://127.0.0.1:8080/woof     # agent greeting
curl -X POST http://127.0.0.1:8080/webhook -H "X-Hub-Signature-256: ..." -d '{"type":"push",...}'

# Run tests
pytest

# Lint + security scan
ruff check integrations main.py tests scripts
bandit -r integrations main.py -ll
```

### How the scheduler decides
`integrations/scheduler.py` watches the event stream and decides **when to act — and which tasks not to do** (ADR 003). It skips draft PRs, bot noise, duplicates, ignored branches (`main`/`master`), out-of-scope paths, low-priority events, and enforces a per-repository cooldown. When it acts, it hands a `WorkOrder` to the agent (`integrations/lambda_woofy_handler.py`) and you review the PR.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Security

See [SECURITY.md](SECURITY.md) for security policy information.
