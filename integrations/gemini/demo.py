#!/usr/bin/env python3
"""
Google Gemini Integration Demo

This script demonstrates the usage of the Google Gemini client for testing purposes.
Ensure your .env file contains GEMINI_API_KEY before running.

Usage:
    python integrations/gemini/demo.py
"""

import sys
import os

# Add the integrations directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gemini_client import GeminiClient


def main():
    """
    Demo function showing Gemini client usage.
    """
    print("🤖 WOOFY McWOOFSON - Google Gemini Integration Demo")
    print("=" * 55)

    try:
        # Initialize client
        print("🔑 Initializing Gemini client...")
        client = GeminiClient()

        # Example queries
        queries = [
            "Explain the concept of machine learning in simple terms",
            "Write a short Python function to reverse a string",
            "What are the benefits of renewable energy?",
        ]

        for i, query in enumerate(queries, 1):
            print(f"\n📝 Query {i}: {query}")
            print("-" * 50)

            try:
                response = client.generate_text(query)
                print("✅ Response received successfully!")

                # Print a summary (avoid printing full response for brevity)
                text = response.get("text", "")
                preview = text[:300] + "..." if len(text) > 300 else text
                print(f"📄 Preview: {preview}")

            except Exception as e:
                print(f"❌ Query failed: {str(e)}")

        # List available models
        print("\n📋 Fetching available models...")
        try:
            models = client.list_models()
            print(f"✅ Found {len(models['models'])} Gemini models")
            for model in models["models"][:3]:  # Show first 3
                print(f"   - {model['name']}")
        except Exception as e:
            print(f"❌ Failed to list models: {str(e)}")

        print("\n🎉 Demo completed successfully!")

    except ValueError as e:
        print(f"❌ Configuration Error: {str(e)}")
        print("💡 Make sure GEMINI_API_KEY is set in your .env file")
        print("🔗 Get your API key from: https://makersuite.google.com/app/apikey")
    except Exception as e:
        print(f"❌ Demo failed: {str(e)}")


def test_credentials():
    """
    Test function to validate Gemini credentials without making API calls.
    """
    print("\n🔍 Testing Gemini credentials...")

    api_key = os.getenv("GEMINI_API_KEY")

    if api_key:
        print("✅ GEMINI_API_KEY is set")
        # Basic validation - check if it looks like a valid API key format
        if api_key.startswith("AIza") and len(api_key) > 20:
            print("✅ API key format appears valid")
        else:
            print("⚠️  API key format may be incorrect (should start with 'AIza')")
    else:
        print("❌ GEMINI_API_KEY is not set")

    if api_key:
        print("🎯 Credentials appear to be configured correctly")
    else:
        print("⚠️  Credentials need to be configured before using Gemini integration")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test-credentials":
        test_credentials()
    else:
        main()
