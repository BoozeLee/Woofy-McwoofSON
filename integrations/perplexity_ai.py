
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
import os
from typing import Dict, List, Any

class PerplexityAI:
    def __init__(self):
        self.api_key = os.getenv('PERPLEXITY_API_KEY')
        self.base_url = 'https://api.perplexity.ai'
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def search_and_analyze(self, query: str, model: str = 'llama-3.1-sonar-small-128k-online') -> Dict[str, Any]:
        payload = {
            'model': model,
            'messages': [{'role': 'user', 'content': query}],
            'max_tokens': 1000,
            'temperature': 0.2
        }
        
        response = requests.post(
            f'{self.base_url}/chat/completions',
            headers=self.headers,
            json=payload
        )
        return response.json()
    
    def batch_analyze(self, queries: List[str]) -> List[Dict[str, Any]]:
        return [self.search_and_analyze(query) for query in queries]
    
    def get_market_insights(self, topic: str) -> Dict[str, Any]:
        query = f"Latest market trends and opportunities for {topic} in 2024"
        return self.search_and_analyze(query)