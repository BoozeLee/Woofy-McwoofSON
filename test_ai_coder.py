# Import the helper
from git_helper import get_github_credentials, GitHelper

# Get GitHub access
creds = get_github_credentials()
print(f"Token: {creds['token'][:20]}...")  # Only show first 20 chars for security
print(f"Repo: {creds['repo_url']}")
print(f"Username: {creds['username']}")

# Use Git operations
helper = GitHelper()
helper.init_local_repo()
helper.push_to_github("🚀 AI Coder: Repository upgrade complete")