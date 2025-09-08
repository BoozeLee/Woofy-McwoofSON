"""
Google Gemini Integration Module

This module provides secure integration with Google Gemini AI for the WOOFY McWOOFSON project.
Handles API authentication, text generation, and response processing while maintaining security standards.

Author: Kilo Code
Date: 2025-09-07
"""

import os
import google.generativeai as genai
import logging
from typing import Dict, Optional, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GeminiClient:
    """
    Client for interacting with Google Gemini AI.

    This class handles authentication, request formatting, and response processing
    while ensuring no sensitive data is logged or exposed.
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Gemini client.

        Args:
            api_key: Google Gemini API key. If None, will attempt to load from environment.
        """
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("Gemini API key not provided and not found in environment variables")

        # Configure the Gemini API
        genai.configure(api_key=self.api_key)

        # Initialize the model
        self.model = genai.GenerativeModel('gemini-pro')
        logger.info("Gemini client initialized successfully")

    def generate_text(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """
        Generate text using Google Gemini AI.

        Args:
            prompt: The input text prompt
            **kwargs: Additional parameters for the API request

        Returns:
            Dict containing the API response

        Raises:
            Exception: If the API request fails
        """
        try:
            logger.info("Sending text generation request to Gemini API")

            # Generate content
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=kwargs.get('temperature', 0.7),
                    top_p=kwargs.get('top_p', 0.8),
                    top_k=kwargs.get('top_k', 10),
                    max_output_tokens=kwargs.get('max_output_tokens', 2048),
                    **{k: v for k, v in kwargs.items()
                       if k in ['temperature', 'top_p', 'top_k', 'max_output_tokens']}
                )
            )

            # Extract the response text
            result_text = response.text if hasattr(response, 'text') else str(response)

            result = {
                'text': result_text,
                'model': 'gemini-pro',
                'usage': getattr(response, 'usage_metadata', None)
            }

            logger.info("Text generation completed successfully")

            # Sanitize response for logging
            sanitized_result = self._sanitize_response(result)
            return sanitized_result

        except Exception as e:
            logger.error(f"Gemini API request failed: {str(e)}")
            raise

    def _sanitize_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Sanitize API response to remove any potentially sensitive data before logging.

        Args:
            response: Raw API response

        Returns:
            Sanitized response dict
        """
        # For Gemini, responses typically don't contain sensitive data
        # This method can be enhanced if needed for specific sanitization requirements
        return response

    def list_models(self) -> Dict[str, Any]:
        """
        List available Gemini models.

        Returns:
            Dict containing available models
        """
        try:
            logger.info("Fetching available Gemini models")
            models = genai.list_models()
            model_list = [{'name': model.name, 'description': model.description}
                         for model in models if 'gemini' in model.name.lower()]

            return {'models': model_list}

        except Exception as e:
            logger.error(f"Failed to list models: {str(e)}")
            raise

def main():
    """
    Example usage of the Gemini client.
    This function demonstrates how to use the client for testing purposes.

    Note: This will fail until proper credentials are configured.
    """
    try:
        client = GeminiClient()

        # Example text generation
        prompt = "Explain the concept of machine learning in simple terms"
        print(f"🤖 Query: {prompt}")
        print("-" * 50)

        response = client.generate_text(prompt)
        print("✅ Response received successfully!")
        print(f"📝 Generated text: {response['text'][:300]}...")

        # List available models
        models = client.list_models()
        print(f"\n📋 Available models: {len(models['models'])}")

    except ValueError as e:
        print(f"❌ Configuration Error: {str(e)}")
        print("💡 Make sure GEMINI_API_KEY is set in your .env file")
        print("🔗 Get your API key from: https://makersuite.google.com/app/apikey")
    except Exception as e:
        print(f"❌ Demo failed: {str(e)}")

if __name__ == "__main__":
    main()