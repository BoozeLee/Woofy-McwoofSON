
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

#!/usr/bin/env python3
"""
Secure Perplexity API Retrieval Script
Fetches Perplexity API key from GitHub Secrets using MCP server and AWS security
"""

import os
import requests
import json
from integrations.secure_api_client import SecureAPIManager


class GitHubSecretsRetriever:
    def __init__(self):
        self.api_manager = SecureAPIManager()
        self.github_token = self.api_manager.get_github_token()
        self.repo_owner = "Bakery-street-projct"
        self.repo_name = "Woofy-McwoofSON"

    def get_perplexity_api_key(self):
        """Retrieve Perplexity API key from GitHub Secrets"""
        try:
            # First try AWS Secrets Manager
            perplexity_key = self.api_manager.get_perplexity_key()
            print("✅ Retrieved Perplexity API key from AWS Secrets Manager")
            return perplexity_key
        except ValueError:
            print("⚠️ AWS Secrets Manager not available, checking environment...")
            # Fallback to environment variable
            perplexity_key = os.getenv("PERPLEXITY_API_KEY")
            if perplexity_key:
                print("✅ Retrieved Perplexity API key from environment")
                return perplexity_key
            else:
                print("❌ Perplexity API key not found in environment")
                return None

    def verify_github_access(self):
        """Verify GitHub API access"""
        headers = {
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github.v3+json",
        }

        url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print("✅ GitHub API access verified")
            return True
        else:
            print(f"❌ GitHub API access failed: {response.status_code}")
            return False


def main():
    """Main function to retrieve Perplexity API key"""
    print("🔐 Secure Perplexity API Retrieval")
    print("=" * 40)

    try:
        retriever = GitHubSecretsRetriever()

        # Verify GitHub access
        if not retriever.verify_github_access():
            print("Cannot proceed without GitHub access")
            return

        # Get Perplexity API key
        api_key = retriever.get_perplexity_api_key()

        if api_key:
            # Mask the key for display
            masked_key = (
                f"{api_key[:8]}...{api_key[-4:]}" if len(api_key) > 12 else "***"
            )
            print(f"🎯 Perplexity API Key: {masked_key}")
            print("✅ Ready for use with MCP server")
        else:
            print("❌ Could not retrieve Perplexity API key")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
