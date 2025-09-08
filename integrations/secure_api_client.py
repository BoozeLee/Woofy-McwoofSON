#!/usr/bin/env python3
"""
Secure API Client using AWS Secrets Manager
Centralized credential management for all API integrations
"""

import boto3
import json
import logging
from botocore.exceptions import ClientError, NoCredentialsError
from typing import Dict, Optional
import os


class SecureAPIManager:
    """Centralized API credential management using AWS Secrets Manager"""

    def __init__(self, region_name: str = "us-east-1"):
        """Initialize SecureAPIManager with AWS region"""
        self.region_name = region_name
        self.logger = logging.getLogger(__name__)

        try:
            self.secrets_client = boto3.client(
                "secretsmanager", region_name=region_name
            )
            self.logger.info(
                f"AWS Secrets Manager client initialized for region: {region_name}"
            )
        except NoCredentialsError:
            self.logger.warning(
                "AWS credentials not found, falling back to environment variables"
            )
            self.secrets_client = None

    def get_secret(self, secret_name: str) -> str:
        """Retrieve secret from AWS Secrets Manager with fallback to environment"""
        if self.secrets_client:
            try:
                response = self.secrets_client.get_secret_value(SecretId=secret_name)
                self.logger.info(f"Retrieved secret from AWS: {secret_name}")
                return response["SecretString"]
            except ClientError as e:
                self.logger.error(
                    f"Failed to retrieve secret {secret_name} from AWS: {e}"
                )
                # Fall back to environment variable
                return self._get_env_fallback(secret_name)
        else:
            return self._get_env_fallback(secret_name)

    def _get_env_fallback(self, secret_name: str) -> str:
        """Fallback to environment variables when AWS is not available"""
        # Convert secret name to environment variable format
        env_var = secret_name.replace("woofy-mcwoofson/", "").replace("-", "_").upper()

        value = os.getenv(env_var)
        if value:
            self.logger.info(f"Retrieved secret from environment: {env_var}")
            return value
        else:
            raise ValueError(f"Secret not found in AWS or environment: {secret_name}")

    def get_json_secret(self, secret_name: str) -> Dict:
        """Retrieve and parse JSON secret"""
        secret_string = self.get_secret(secret_name)
        try:
            return json.loads(secret_string)
        except json.JSONDecodeError:
            # If not JSON, return as single key
            return {"value": secret_string}

    def get_perplexity_key(self) -> str:
        """Get Perplexity API key"""
        return self.get_secret("woofy-mcwoofson/perplexity-api-key")

    def get_watsonx_credentials(self) -> Dict[str, str]:
        """Get watsonx credentials"""
        try:
            return self.get_json_secret("woofy-mcwoofson/watsonx-credentials")
        except ValueError:
            # Fallback to separate environment variables
            return {
                "api_key": os.getenv("WATSONX_API_KEY", ""),
                "project_id": os.getenv("WATSONX_PROJECT_ID", ""),
            }

    def get_gemini_key(self) -> str:
        """Get Gemini API key"""
        return self.get_secret("woofy-mcwoofson/gemini-api-key")

    def get_groq_key(self) -> str:
        """Get GROQ API key"""
        return self.get_secret("woofy-mcwoofson/groq-api-key")

    def get_github_token(self) -> str:
        """Get GitHub token"""
        return self.get_secret("woofy-mcwoofson/github-token")

    def get_discord_token(self) -> str:
        """Get Discord bot token"""
        return self.get_secret("woofy-mcwoofson/discord-bot-token")

    def get_stripe_keys(self) -> Dict[str, str]:
        """Get Stripe API keys"""
        try:
            return self.get_json_secret("woofy-mcwoofson/stripe-keys")
        except ValueError:
            # Fallback to separate environment variables
            return {
                "publishable_key": os.getenv("STRIPE_PUBLISHABLE_KEY", ""),
                "secret_key": os.getenv("STRIPE_SECRET_KEY", ""),
            }


class SecurePerplexityClient:
    """Secure Perplexity client using AWS Secrets Manager"""

    def __init__(self):
        self.api_manager = SecureAPIManager()
        try:
            self.api_key = self.api_manager.get_perplexity_key()
            self.logger = logging.getLogger(__name__)
            self.logger.info("Perplexity client initialized with secure credentials")
        except ValueError as e:
            self.logger.error(f"Failed to initialize Perplexity client: {e}")
            raise

    def query(self, prompt: str, model: str = "pplx-7b-online") -> Dict:
        """Execute secure query to Perplexity API"""
        # Implementation would use self.api_key
        self.logger.info(f"Executing Perplexity query with model: {model}")
        # Actual API call implementation here
        return {"status": "success", "model": model, "prompt": prompt}


class SecureWatsonxClient:
    """Secure watsonx client using AWS Secrets Manager"""

    def __init__(self):
        self.api_manager = SecureAPIManager()
        try:
            credentials = self.api_manager.get_watsonx_credentials()
            self.api_key = credentials.get("api_key", "")
            self.project_id = credentials.get("project_id", "")
            self.logger = logging.getLogger(__name__)

            if not self.api_key or not self.project_id:
                raise ValueError("watsonx credentials incomplete")

            self.logger.info("watsonx client initialized with secure credentials")
        except ValueError as e:
            self.logger.error(f"Failed to initialize watsonx client: {e}")
            raise

    def generate_text(
        self, prompt: str, model: str = "meta-llama/llama-3-70b-instruct"
    ) -> Dict:
        """Execute secure text generation with watsonx"""
        self.logger.info(f"Executing watsonx text generation with model: {model}")
        # Actual API call implementation here
        return {"status": "success", "model": model, "prompt": prompt}


class SecureGeminiClient:
    """Secure Gemini client using AWS Secrets Manager"""

    def __init__(self):
        self.api_manager = SecureAPIManager()
        try:
            self.api_key = self.api_manager.get_gemini_key()
            self.logger = logging.getLogger(__name__)
            self.logger.info("Gemini client initialized with secure credentials")
        except ValueError as e:
            self.logger.error(f"Failed to initialize Gemini client: {e}")
            raise

    def generate_content(self, prompt: str, model: str = "gemini-pro") -> Dict:
        """Execute secure content generation with Gemini"""
        self.logger.info(f"Executing Gemini content generation with model: {model}")
        # Actual API call implementation here
        return {"status": "success", "model": model, "prompt": prompt}


class SecureGROQClient:
    """Secure GROQ client using AWS Secrets Manager"""

    def __init__(self):
        self.api_manager = SecureAPIManager()
        try:
            self.api_key = self.api_manager.get_groq_key()
            self.logger = logging.getLogger(__name__)
            self.logger.info("GROQ client initialized with secure credentials")
        except ValueError as e:
            self.logger.error(f"Failed to initialize GROQ client: {e}")
            raise

    def chat_completion(
        self, messages: list, model: str = "mixtral-8x7b-32768"
    ) -> Dict:
        """Execute secure chat completion with GROQ"""
        self.logger.info(f"Executing GROQ chat completion with model: {model}")
        # Actual API call implementation here
        return {"status": "success", "model": model, "messages": messages}


# Unified secure client
class WoofySecureAI:
    """Unified secure AI client for all integrations"""

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.api_manager = SecureAPIManager()

        # Initialize all clients
        self.clients = {}
        self._initialize_clients()

    def _initialize_clients(self):
        """Initialize all available AI clients"""
        try:
            self.clients["perplexity"] = SecurePerplexityClient()
        except ValueError:
            self.logger.warning("Perplexity client not available")

        try:
            self.clients["watsonx"] = SecureWatsonxClient()
        except ValueError:
            self.logger.warning("watsonx client not available")

        try:
            self.clients["gemini"] = SecureGeminiClient()
        except ValueError:
            self.logger.warning("Gemini client not available")

        try:
            self.clients["groq"] = SecureGROQClient()
        except ValueError:
            self.logger.warning("GROQ client not available")

    def query(self, service: str, prompt: str, **kwargs) -> Dict:
        """Execute query on specified service"""
        if service not in self.clients:
            raise ValueError(f"Service not available: {service}")

        client = self.clients[service]

        if service == "perplexity":
            return client.query(prompt, **kwargs)
        elif service == "watsonx":
            return client.generate_text(prompt, **kwargs)
        elif service == "gemini":
            return client.generate_content(prompt, **kwargs)
        elif service == "groq":
            messages = kwargs.get("messages", [{"role": "user", "content": prompt}])
            return client.chat_completion(messages, **kwargs)
        else:
            raise ValueError(f"Unknown service: {service}")

    def get_available_services(self) -> list:
        """Get list of available services"""
        return list(self.clients.keys())


# Example usage and testing
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    print("🔐 Testing Secure API Manager")
    print("=" * 40)

    try:
        # Test unified client
        ai = WoofySecureAI()
        available = ai.get_available_services()
        print(f"✅ Available services: {available}")

        # Test individual managers
        manager = SecureAPIManager()

        # Test each credential (will fall back to env vars if AWS not available)
        try:
            perplexity_key = manager.get_perplexity_key()
            print("✅ Perplexity key: Retrieved")
        except ValueError:
            print("❌ Perplexity key: Not available")

        try:
            watsonx_creds = manager.get_watsonx_credentials()
            print("✅ watsonx credentials: Retrieved")
        except ValueError:
            print("❌ watsonx credentials: Not available")

        print("\n🔐 Secure API Manager test completed")

    except Exception as e:
        print(f"❌ Test failed: {e}")
