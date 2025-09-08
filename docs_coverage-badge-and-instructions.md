# Coverage Badge & Test Coverage Instructions

## How to Add a Coverage Badge

1. **Set up code coverage reporting:**
   - For Node.js: Use [Jest](https://jestjs.io/) + [Coveralls](https://coveralls.io/) or [Codecov](https://codecov.io/).
   - For Python: Use [pytest-cov](https://pytest-cov.readthedocs.io/) + [Coveralls](https://coveralls.io/) or [Codecov](https://codecov.io/).

2. **Add the coverage action to your workflow:**
   - Example (`.github/workflows/coverage.yml` for Node.js):
     ```yaml
     name: Coverage
     on: [push, pull_request]
     jobs:
       coverage:
         runs-on: ubuntu-latest
         steps:
           - uses: actions/checkout@v3
           - name: Set up Node.js
             uses: actions/setup-node@v4
             with:
               node-version: '18'
           - run: npm install
           - run: npm test -- --coverage
           - name: Upload coverage to Codecov
             uses: codecov/codecov-action@v4
             with:
               token: ${{ secrets.CODECOV_TOKEN }}
     ```
   - Example (`.github/workflows/coverage.yml` for Python):
     ```yaml
     name: Coverage
     on: [push, pull_request]
     jobs:
       coverage:
         runs-on: ubuntu-latest
         steps:
           - uses: actions/checkout@v3
           - name: Set up Python
             uses: actions/setup-python@v5
             with:
               python-version: '3.11'
           - run: pip install -r requirements.txt
           - run: pytest --cov=src --cov-report=xml
           - name: Upload coverage to Codecov
             uses: codecov/codecov-action@v4
             with:
               token: ${{ secrets.CODECOV_TOKEN }}
     ```

3. **Add a badge to your `README.md`:**
   - Codecov:  
     ```markdown
     ![Coverage](https://codecov.io/gh/YOUR_ORG/YOUR_REPO/branch/main/graph/badge.svg)
     ```
   - Coveralls:  
     ```markdown
     ![Coverage Status](https://coveralls.io/repos/github/YOUR_ORG/YOUR_REPO/badge.svg?branch=main)
     ```

4. **Confirm badge updates after each build.**

---

**Copilot Instructions:**  
- Ensure each PR keeps or improves test coverage.
- Reject PRs that decrease coverage without justification.
- Keep badge at the top of the `README.md`.