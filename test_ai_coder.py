
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

# Import the helper
from git_helper import get_github_credentials, GitHelper
import pytest

# Get GitHub access (skip if no AWS creds configured for Secrets Manager)
if not (os.environ.get('AWS_ACCESS_KEY_ID') or os.environ.get('AWS_PROFILE')):
    pytest.skip("Skipping: AWS credentials not configured for Secrets Manager", allow_module_level=True)
creds = get_github_credentials()
print(f"Token: {creds['token'][:20]}...")  # Only show first 20 chars for security
print(f"Repo: {creds['repo_url']}")
print(f"Username: {creds['username']}")

# Use Git operations
helper = GitHelper()
helper.init_local_repo()
helper.push_to_github("🚀 AI Coder: Repository upgrade complete")