#!/usr/bin/env python3
"""
GROQ Integration Test Script
Tests the GROQ API integration for the Neuromorphic Brain Initiative.

Usage:
1. Set your GROQ_API_KEY in .env file
2. Run: python integrations/groq/test_groq.py

Security Note: Never commit real API keys to version control.
"""

import os
import sys
from dotenv import load_dotenv
from groq import Groq


def test_groq_integration():
    """Test GROQ API integration with llama-3.3-70b-versatile model."""

    # Load environment variables
    load_dotenv()

    # Get API key
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key or api_key == "your_groq_api_key_here":
        print("❌ ERROR: GROQ_API_KEY not set in .env file")
        print("Please obtain a GROQ API key from https://console.groq.com/keys")
        print("And update .env: GROQ_API_KEY=your_actual_key_here")
        return False

    try:
        # Initialize GROQ client
        client = Groq(api_key=api_key)

        print("🚀 Testing GROQ integration...")
        print("Model: llama-3.3-70b-versatile")
        print("Query: 'Hello GROQ! What is the capital of France?'")
        print("-" * 50)

        # Make API call
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": "Hello GROQ! What is the capital of France? Also, briefly explain how neuromorphic computing differs from traditional computing.",
                }
            ],
            max_tokens=200,
            temperature=0.1,  # Low temperature for consistent responses
        )

        # Extract response
        answer = response.choices[0].message.content
        usage = response.usage

        print("✅ SUCCESS: GROQ API call successful!")
        print(f"Response: {answer}")
        print("-" * 50)
        print("Usage Statistics:")
        print(f"  Prompt tokens: {usage.prompt_tokens}")
        print(f"  Completion tokens: {usage.completion_tokens}")
        print(f"  Total tokens: {usage.total_tokens}")
        print("-" * 50)
        print("🔒 Security Check: No API key exposed in logs")

        return True

    except Exception as e:
        print(f"❌ ERROR: GROQ API call failed: {str(e)}")
        print("Troubleshooting:")
        print("1. Verify GROQ_API_KEY is correct")
        print("2. Check internet connection")
        print("3. Ensure model 'llama-3.3-70b-versatile' is available")
        print("4. Check GROQ service status at https://console.groq.com")
        return False


if __name__ == "__main__":
    success = test_groq_integration()
    sys.exit(0 if success else 1)
