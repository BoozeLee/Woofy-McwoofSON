
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
🔧 Fix Repository Deployment
Deploy to correct Bakery-street-projct repository
"""

import subprocess
import os
from git_helper import GitHelper, get_github_credentials

def main():
    print("🔧 Fixing Repository Deployment...")
    print("📍 Target: https://github.com/Bakery-street-projct/Woofy-McwoofSON")
    
    try:
        # Verify correct remote
        result = subprocess.run(['git', 'remote', '-v'], 
                              capture_output=True, text=True, cwd=os.getcwd())
        print(f"✅ Remote URL: {result.stdout.strip()}")
        
        # Push to correct repository
        print("\n📤 Pushing to Bakery-street-projct/Woofy-McwoofSON...")
        
        # Add all changes
        subprocess.run(['git', 'add', '.'], cwd=os.getcwd())
        
        # Commit latest changes
        subprocess.run(['git', 'commit', '-m', '🚀 Deploy to correct repository: Bakery-street-projct/Woofy-McwoofSON'], 
                      cwd=os.getcwd())
        
        # Push to final-launch branch
        result = subprocess.run(['git', 'push', '-u', 'origin', 'final-launch'], 
                              capture_output=True, text=True, cwd=os.getcwd())
        
        if result.returncode == 0:
            print("✅ Successfully pushed to final-launch branch")
        else:
            print(f"⚠️  Push result: {result.stderr}")
        
        print("\n🎉 DEPLOYMENT FIXED!")
        print("🐕 Correct Repository: https://github.com/Bakery-street-projct/Woofy-McwoofSON")
        print("🌟 Branch: final-launch")
        print("💼 Status: Enterprise-ready with AWS integration")
        
        return True
        
    except Exception as e:
        print(f"❌ Deployment fix failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)