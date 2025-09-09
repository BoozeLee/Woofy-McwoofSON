
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

import json
import os
from pathlib import Path

def setup_perplexity_vscode():
    """Setup Perplexity API key for VS Code extensions"""
    
    print("🔧 Setting up Perplexity extensions for VS Code...")
    
    # Get API key
    api_key = input("Enter your Perplexity API key: ").strip()
    
    if not api_key:
        print("❌ No API key provided")
        return False
    
    # VS Code settings path
    vscode_settings_path = Path.home() / "AppData/Roaming/Code/User/settings.json"
    
    # Load existing settings or create new
    settings = {}
    if vscode_settings_path.exists():
        try:
            with open(vscode_settings_path, 'r') as f:
                settings = json.load(f)
        except:
            settings = {}
    
    # Add Perplexity configuration
    perplexity_config = {
        "perplexity.apiKey": api_key,
        "perplexity.model": "llama-3.1-sonar-small-128k-online",
        "perplexity.maxTokens": 1000,
        "perplexity.temperature": 0.7,
        "perplexityBot.apiKey": api_key,
        "perplexityBot.enabled": True
    }
    
    # Update settings
    settings.update(perplexity_config)
    
    # Create directory if needed
    vscode_settings_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save settings
    with open(vscode_settings_path, 'w') as f:
        json.dump(settings, f, indent=2)
    
    print("✅ VS Code settings updated")
    
    # Also save to project .env
    env_content = f"""# Perplexity API Configuration
PERPLEXITY_API_KEY={api_key}
PERPLEXITY_MODEL=llama-3.1-sonar-small-128k-online
PERPLEXITY_MAX_TOKENS=1000
PERPLEXITY_TEMPERATURE=0.7
"""
    
    with open('.env.perplexity', 'w') as f:
        f.write(env_content)
    
    print("✅ Project .env.perplexity created")
    
    # Extension installation commands
    extensions = [
        "perplexity-ai.perplexity-ai",
        "perplexity.perplexity-search"
    ]
    
    print("\n📦 Install these VS Code extensions:")
    for ext in extensions:
        print(f"   code --install-extension {ext}")
    
    print("\n🚀 Perplexity extensions configured!")
    print("Restart VS Code to activate the extensions.")
    
    return True

def test_perplexity_api(api_key):
    """Test Perplexity API key"""
    import requests
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {"role": "user", "content": "Hello from WOOFY McWOOFSON!"}
        ],
        "max_tokens": 100
    }
    
    try:
        response = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers=headers,
            json=payload,
            timeout=10
        )
        
        if response.status_code == 200:
            print("✅ Perplexity API key is working!")
            return True
        else:
            print(f"❌ API test failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ API test error: {e}")
        return False

def main():
    print("WOOFY McWOOFSON: Perplexity Extensions Setup")
    print("=" * 50)
    
    # Setup VS Code extensions
    if setup_perplexity_vscode():
        print("\n🎉 Setup complete!")
        print("\nNext steps:")
        print("1. Restart VS Code")
        print("2. Install the recommended extensions")
        print("3. Use Perplexity features in VS Code")
    else:
        print("❌ Setup failed")

if __name__ == "__main__":
    main()