# 🐾 WOOFY Makefile

install:
	npm install

lint:
	npm run lint

test:
	npm test

start:
	npm start

docker-build:
	docker build -t woofy-mcwoofson .

docker-run:
	docker-compose up

# --- Python / Automation Targets ---
PY=python

.PHONY: deps py-lint py-test audit audit-dry audit-summary coverage coverage-html coverage-xml coverage-ci vuln-scan

deps:
	$(PY) -m pip install -r requirements.txt

py-lint:
	ruff check integrations main.py tests scripts

py-test:
	pytest -q

coverage:
	pytest --cov=integrations --cov-report=term-missing

coverage-html:
	pytest --cov=integrations --cov-report=html && echo "HTML report at htmlcov/index.html"

coverage-xml:
	pytest --cov=integrations --cov-report=xml

coverage-ci:
	pytest --cov=integrations --cov-report=xml --cov-report=term-missing --cov-fail-under=85

vuln-scan:
	pip-audit || true

audit:
	$(PY) scripts/file_audit.py --archive

audit-dry:
	$(PY) scripts/file_audit.py --archive --dry-run

audit-summary:
	$(PY) scripts/file_audit.py --summary-only