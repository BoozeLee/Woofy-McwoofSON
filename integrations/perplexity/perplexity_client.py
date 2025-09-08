"""
Perplexity Bot Integration Module

This module provides secure integration with Perplexity AI API for the WOOFY McWOOFSON project.
Handles API authentication, query execution, and response processing while maintaining security standards.

Author: Kilo Code
Date: 2025-09-07
"""

import os
import requests
import logging
from typing import Dict, Optional, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PerplexityClient:
    """
    Client for interacting with Perplexity AI API.

    This class handles authentication, request formatting, and response processing
    while ensuring no sensitive data is logged or exposed.
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Perplexity client.

        Args:
            api_key: Perplexity API key. If None, will attempt to load from environment.
        """
        self.api_key = api_key or os.getenv("PERPLEXITY_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Perplexity API key not provided and not found in environment variables"
            )

        self.base_url = "https://api.perplexity.ai"
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }
        )

    def query(
        self, prompt: str, model: str = "pplx-7b-online", **kwargs
    ) -> Dict[str, Any]:
        """
        Execute a query against Perplexity AI.

        Args:
            prompt: The query text to send to Perplexity
            model: The model to use (default: pplx-7b-online)
            **kwargs: Additional parameters for the API request

        Returns:
            Dict containing the API response

        Raises:
            requests.RequestException: If the API request fails
        """
        endpoint = f"{self.base_url}/chat/completions"

        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            **kwargs,
        }

        try:
            logger.info(f"Sending query to Perplexity API (model: {model})")
            response = self.session.post(endpoint, json=payload)
            response.raise_for_status()

            result = response.json()
            logger.info("Query completed successfully")

            # Sanitize response for logging (remove sensitive content if any)
            sanitized_result = self._sanitize_response(result)
            return sanitized_result

        except requests.RequestException as e:
            logger.error(f"Perplexity API request failed: {str(e)}")
            raise

    def _sanitize_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Sanitize API response to remove any potentially sensitive data before logging.

        Args:
            response: Raw API response

        Returns:
            Sanitized response dict
        """
        # For now, return as-is since Perplexity responses typically don't contain sensitive data
        # This method can be enhanced if needed for specific sanitization requirements
        return response

    def get_credit_usage(self) -> Dict[str, Any]:
        """
        Get current credit usage information.

        Note: This is a placeholder - actual implementation depends on Perplexity's billing API.
        """
        # Placeholder for credit usage tracking
        logger.info("Credit usage tracking not yet implemented")
        return {"status": "not_implemented"}

    def close(self):
        """Close the HTTP session."""
        self.session.close()


def main():
    """
    Example usage of the Perplexity client.
    This function demonstrates how to use the client for testing purposes.
    """
    try:
        client = PerplexityClient()

        # Example query
        response = client.query("What is the capital of France?")
        print("Response:", response)

        client.close()

    except Exception as e:
        logger.error(f"Error in main: {str(e)}")


if __name__ == "__main__":
    main()
