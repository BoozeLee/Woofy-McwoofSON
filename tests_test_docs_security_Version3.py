
# WOOFY SECURITY GUARDRAILS - AUTO-APPLIED
import os
import sys
import logging

# Disable AWS credential logging
for logger_name in ['boto3', 'botocore', 'urllib3', 's3transfer']:
    logging.getLogger(logger_name).setLevel(logging.CRITICAL)

# Suppress credential discovery
os.environ['AWS_DEFAULT_OUTPUT'] = 'json'
os.environ['AWS_CLI_FILE_ENCODING'] = 'UTF-8'

# Import security guardrails
try:
    from security_guardrails import SecurityGuardrails
    SecurityGuardrails.secure_log("Security guardrails active")
except ImportError:
    pass

import re
import pathlib


def potential_token_lines(text):
    # Example: GitHub PATs: ghp_xxx, github_pat_xxx, classic token patterns, etc.
    token_patterns = [
        r"ghp_[A-Za-z0-9]{30,}",  # GitHub classic PAT
        r"github_pat_[A-Za-z0-9_]{20,}",  # Newer GitHub PAT
        r"(?<![A-Za-z0-9])[A-Za-z0-9]{40}(?![A-Za-z0-9])",  # Generic 40-char secrets
        r"sk_live_[A-Za-z0-9]{20,}",  # Stripe live keys
    ]
    combined = re.compile("|".join(token_patterns))
    return [line for line in text.splitlines() if combined.search(line)]


def test_github_copilot_token_guide_no_secrets():
    guide = pathlib.Path("GITHUB_COPILOT_TOKEN_GUIDE.md").read_text()
    lines = potential_token_lines(guide)
    assert not lines, (
        f"Potential credential/token patterns found in GITHUB_COPILOT_TOKEN_GUIDE.md:\n"
        + "\n".join(lines)
    )
