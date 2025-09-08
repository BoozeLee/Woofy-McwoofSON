import boto3
import subprocess
import json
import os

class GitHelper:
    def __init__(self):
        self.secrets_client = boto3.client('secretsmanager', region_name='us-east-1')
        self.github_token = None
        self.repo_url = "https://github.com/Bakery-street-projct/Woofy-McwoofSON.git"
    
    def get_github_token(self):
        response = self.secrets_client.get_secret_value(SecretId='github-oauth-secret')
        secret = json.loads(response['SecretString'])
        self.github_token = secret['client_secret']
        return self.github_token
    
    def setup_git_auth(self):
        """Configure git with GitHub token for authentication"""
        token = self.get_github_token()
        
        # Set git credentials
        subprocess.run(['git', 'config', '--global', 'user.name', 'BoozeLee'], cwd=os.getcwd())
        subprocess.run(['git', 'config', '--global', 'user.email', 'booze@woofymcwoofson.com'], cwd=os.getcwd())
        
        # Configure token-based authentication
        auth_url = f"https://{token}@github.com/BoozeLee/woofy-mcwoofson-enterprise.git"
        
        return auth_url
    
    def init_local_repo(self):
        """Initialize local git repository and connect to GitHub"""
        try:
            # Initialize git if not already done
            subprocess.run(['git', 'init'], cwd=os.getcwd(), check=True)
            
            # Get authenticated URL
            auth_url = self.setup_git_auth()
            
            # Add remote origin
            subprocess.run(['git', 'remote', 'add', 'origin', auth_url], cwd=os.getcwd())
            
            print("SUCCESS: Local repo initialized and connected to GitHub!")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"Git command failed: {e}")
            return False
    
    def push_to_github(self, commit_message="🐾 WOOFY: Updated local repository"):
        """Add, commit, and push changes to GitHub"""
        try:
            # Add all files
            subprocess.run(['git', 'add', '.'], cwd=os.getcwd(), check=True)
            
            # Commit changes
            subprocess.run(['git', 'commit', '-m', commit_message], cwd=os.getcwd(), check=True)
            
            # Push to GitHub
            subprocess.run(['git', 'push', '-u', 'origin', 'main'], cwd=os.getcwd(), check=True)
            
            print("SUCCESS: Changes pushed to GitHub!")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"Push failed: {e}")
            return False

# Helper function for AI coder
def get_github_credentials():
    """Returns GitHub token for AI coder use"""
    helper = GitHelper()
    return {
        'token': helper.get_github_token(),
        'repo_url': helper.repo_url,
        'username': 'BoozeLee'
    }

if __name__ == "__main__":
    helper = GitHelper()
    helper.init_local_repo()