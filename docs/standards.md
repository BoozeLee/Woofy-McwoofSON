# 🦴 CI/CD, Deployment, and Documentation Standards

## CI/CD

- All code must pass lint (`make lint`) and tests (`make test`) before merging.
- Use GitHub Actions workflows for:
  - Lint/Test (`woofy-lint-test.yml`)
  - Deployment (`woofy-deploy.yml`)
  - Compliance check (`woofy-compliance.yml`)
- Protect the `main` branch; require PR review and status checks.

## Deployment

- Use Docker and docker-compose for reproducible environments.
- Secrets are never committed; use `.env` and GitHub/AWS secrets.
- Deployments are performed via CI/CD on tag release (`v*.*.*`).

## Documentation

- All docs must be up-to-date, clear, and use dog-themed branding.
- API reference lives in `/docs/api/`.
- User/admin guides in `/docs/`.
- Architecture diagrams in `/docs/architecture/`.
- Changelog and roadmap are mandatory.

## Security

- Run security tests on every PR.
- Store results in `SECURITY_TEST_RESULTS.md`.
- Regularly review permissions, dependencies, and secrets.

---

Pawsitive development, always! 🐶