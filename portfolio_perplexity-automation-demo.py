
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

# Perplexity-Powered Bug Fix Demo
import os
import requests

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")


def fix_bug_with_perplexity(code_snippet, bug_desc):
    """
    Uses Perplexity API to suggest bug fixes for given code.
    """
    url = "https://api.perplexity.ai/v1/fix"
    headers = {"Authorization": f"Bearer {PERPLEXITY_API_KEY}"}
    data = {"code": code_snippet, "description": bug_desc}
    resp = requests.post(url, headers=headers, json=data, timeout=30)
    resp.raise_for_status()
    return resp.json()["fixed_code"]


if __name__ == "__main__":
    code = "def add(a, b):\n  return a - b  # bug!"
    desc = "Addition is incorrect; should be a + b."
    print(fix_bug_with_perplexity(code, desc))
