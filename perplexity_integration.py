
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

import requests
import json
import os
from typing import Dict, List, Optional

class PerplexityBot:
    """Perplexity API Bot for WOOFY McWOOFSON"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('PERPLEXITY_API_KEY')
        self.base_url = "https://api.perplexity.ai"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def chat(self, message: str, model: str = "llama-3.1-sonar-small-128k-online") -> Dict:
        """Send chat message to Perplexity API"""
        url = f"{self.base_url}/chat/completions"
        
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are WOOFY McWOOFSON, an enterprise AI assistant with psychedelic creativity and atomic precision."
                },
                {
                    "role": "user", 
                    "content": message
                }
            ],
            "max_tokens": 1000,
            "temperature": 0.7,
            "stream": False
        }
        
        try:
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Perplexity API error: {str(e)}"}
    
    def search(self, query: str) -> Dict:
        """Search using Perplexity's online capabilities"""
        return self.chat(f"Search and provide detailed information about: {query}")
    
    def code_review(self, code: str, language: str = "python") -> Dict:
        """Review code using Perplexity"""
        prompt = f"""
        Review this {language} code for WOOFY McWOOFSON enterprise project:
        
        ```{language}
        {code}
        ```
        
        Provide:
        1. Security analysis
        2. Performance optimization
        3. Best practices compliance
        4. Enterprise readiness assessment
        """
        return self.chat(prompt)

class PerplexityExtensionManager:
    """Manage Perplexity extensions for VS Code"""
    
    def __init__(self):
        self.bot = PerplexityBot()
        self.extensions = {
            "perplexity-ai": "Official Perplexity AI extension",
            "perplexity-search": "Perplexity Search integration"
        }
    
    def setup_vscode_integration(self) -> Dict:
        """Setup VS Code integration with Perplexity"""
        config = {
            "perplexity.apiKey": "${PERPLEXITY_API_KEY}",
            "perplexity.model": "llama-3.1-sonar-small-128k-online",
            "perplexity.maxTokens": 1000,
            "perplexity.temperature": 0.7,
            "perplexity.enableCodeReview": True,
            "perplexity.enableSearch": True
        }
        
        return {
            "vscode_settings": config,
            "extensions_to_install": list(self.extensions.keys()),
            "setup_complete": True
        }
    
    def test_integration(self) -> Dict:
        """Test Perplexity integration"""
        test_message = "Hello from WOOFY McWOOFSON! Test the Perplexity integration."
        result = self.bot.chat(test_message)
        
        return {
            "test_message": test_message,
            "response": result,
            "status": "success" if "error" not in result else "failed"
        }

def setup_perplexity_env():
    """Setup Perplexity environment variables"""
    env_content = """
# Perplexity API Configuration for WOOFY McWOOFSON
PERPLEXITY_API_KEY=your_perplexity_api_key_here

# Perplexity Models
PERPLEXITY_MODEL_ONLINE=llama-3.1-sonar-small-128k-online
PERPLEXITY_MODEL_CHAT=llama-3.1-sonar-large-128k-chat

# Integration Settings
PERPLEXITY_MAX_TOKENS=1000
PERPLEXITY_TEMPERATURE=0.7
"""
    
    with open('.env.perplexity', 'w') as f:
        f.write(env_content)
    
    return "Perplexity environment file created: .env.perplexity"

def main():
    """Main setup and test function"""
    print("WOOFY McWOOFSON: Perplexity Integration Setup")
    print("=" * 50)
    
    # Setup environment
    env_result = setup_perplexity_env()
    print(f"✅ {env_result}")
    
    # Setup extension manager
    manager = PerplexityExtensionManager()
    
    # Get VS Code configuration
    vscode_config = manager.setup_vscode_integration()
    print("✅ VS Code integration configured")
    print(f"Extensions to install: {vscode_config['extensions_to_install']}")
    
    # Test integration (if API key is available)
    if os.getenv('PERPLEXITY_API_KEY'):
        test_result = manager.test_integration()
        print(f"✅ Integration test: {test_result['status']}")
    else:
        print("⚠️  Set PERPLEXITY_API_KEY to test integration")
    
    print("\n🚀 Perplexity integration ready for WOOFY McWOOFSON!")

if __name__ == "__main__":
    main()