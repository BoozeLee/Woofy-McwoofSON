# 🐾 Helper Scripts

Central location for automation, audit, deployment, and maintenance scripts.

## 📂 File Audit & Archival (`scripts/file_audit.py`)
Purpose: Detect versioned Markdown files (e.g. `*_Version3.md`), optionally archive them into a timestamped `archive/` folder, and generate `ENTERPRISE_FILE_SUMMARY.md` with categorized inventory.

### Categories Generated
- Onboarding & Knowledge Vault
- Security & Compliance
- CI/CD & Workflows
- Integrations & API
- Transition & Audit
- Documentation

### Usage
Run directly:
```
python scripts/file_audit.py --dry-run        # Preview archival actions
python scripts/file_audit.py --archive        # Archive versioned files + summary
python scripts/file_audit.py --archive --dry-run  # Show what would move
python scripts/file_audit.py --summary-only   # Only regenerate summary file
```

### Makefile Targets
```
make audit-dry      # dry-run archival + output
make audit          # perform archival
make audit-summary  # summary only
```

### CI Integration
The GitHub Action `woofy-lint-test.yml` runs a dry-run (`make audit-dry`) plus a summary generation and uploads `ENTERPRISE_FILE_SUMMARY.md` as an artifact.

## 🧪 Testing & Lint Helpers
```
make deps     # install Python deps
make py-lint  # flake8 linting
make py-test  # run pytest suite
```

## 🚀 Future Script Ideas
- `rotate-keys.sh` / `rotate_keys.py` for credential rotation orchestration
- `coverage_report.sh` to generate coverage & badge
- `security_scan.py` to aggregate secret + dependency scan results

## Legacy Examples (placeholder)
- deploy.sh
- setup-env.sh
- rotate-keys.sh

> Keep scripts idempotent, minimal dependencies, and document any required environment variables at the top of the script.