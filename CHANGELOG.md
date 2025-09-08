# 🐕 GOOD BOY RELEASE NOTES

All notable changes to WOOFY McWOOFSON will be tracked here.

## [1.0.0] - 2025-09-07

### Added
- Initial repository scaffold (lambda handler stub, basic docs, initial test & security scan)
- Branding assets and baseline README

### Security
- Basic secret pattern test (`tests/test_security.py`)

### Infrastructure
- Initial GitHub Actions workflow (lint/test) placeholder

## [Unreleased]
### Added
- Action-based Lambda handler routing (`hello`, `ping`) with structured error responses
- Expanded negative/edge test coverage (`tests/test_lambda_woofy_handler_negative.py`)
- Enhanced security scanning now includes markdown & broader patterns (`tests/test_security.py`)
- Coverage workflow with threshold enforcement (85%) + `.coveragerc`, Codecov upload, and README badge placeholder
- **Perplexity Bot Integration**: Complete API client with secure credential management
- **IBM watsonx Integration**: Template client ready for credential configuration
- **Google Gemini Integration**: Complete API client with text generation capabilities
- AI integration documentation under `/docs/integrations/`

### Documentation
- ADR directory validated (serverless baseline present)
- Perplexity integration guide (`docs/integrations/perplexity.md`)
- IBM watsonx integration guide (`docs/integrations/watsonx.md`)
 - ADR 002: Modular Lambda Action Dispatch (accepted)

### Security
- Environment-based credential management for AI integrations
- Secure API key handling with python-dotenv
- Integration & demo security validation (Perplexity, watsonx) with zero credential exposure
- Complete security compliance verification for all API integrations

### Planned
- Enhanced file audit JSON mode & archival improvements
- Coverage tooling & vulnerability scanning integration
- Credential rotation & history cleanup procedures
- Docker & extended CI/CD enhancements
- IBM watsonx credential activation and testing

---

WOOFY is ready to fetch new features! 🦴