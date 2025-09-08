#!/usr/bin/env python3
"""
IBM watsonx Integration Demo

This script demonstrates the usage of the watsonx client for testing purposes.
Note: This is a template demo. Actual execution requires valid IBM watsonx credentials.

Usage:
    python integrations/watsonx/demo.py
"""

import sys
import os

# Add the integrations directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from watsonx_client import WatsonxClient


def main():
    """
    Demo function showing watsonx client usage.
    This will fail until proper credentials are configured.
    """
    print("🤖 WOOFY McWOOFSON - IBM watsonx Integration Demo")
    print("=" * 55)

    print("⚠️  STATUS: This integration is pending IBM watsonx credentials")
    print("📋 Required environment variables:")
    print("   - WATSONX_API_KEY")
    print("   - WATSONX_PROJECT_ID")
    print()

    try:
        # Attempt to initialize client
        print("🔑 Attempting to initialize watsonx client...")
        client = WatsonxClient()

        # Example text generation
        prompt = "Write a short poem about artificial intelligence"
        print(f"📝 Query: {prompt}")
        print("-" * 40)

        response = client.generate_text(prompt)
        print("✅ Response received successfully!")

        # Print a summary
        if "results" in response and response["results"]:
            content = response["results"][0].get("generated_text", "")
            preview = content[:200] + "..." if len(content) > 200 else content
            print(f"📄 Generated text: {preview}")
        else:
            print("📄 Response structure may vary - check full response in logs")

        # Clean up
        client.close()
        print("\n🎉 Demo completed successfully!")

    except ValueError as e:
        print(f"❌ Configuration Error: {str(e)}")
        print(
            "💡 Please ensure WATSONX_API_KEY and WATSONX_PROJECT_ID are set in your .env file"
        )
        print("📞 Contact IBM to obtain watsonx credentials")
    except Exception as e:
        print(f"❌ Demo failed: {str(e)}")
        print("🔧 This may be due to API endpoint changes or credential issues")


def test_credentials():
    """
    Test function to validate watsonx credentials without making API calls.
    """
    print("\n🔍 Testing watsonx credentials...")

    api_key = os.getenv("WATSONX_API_KEY")
    project_id = os.getenv("WATSONX_PROJECT_ID")

    if api_key:
        print("✅ WATSONX_API_KEY is set")
    else:
        print("❌ WATSONX_API_KEY is not set")

    if project_id:
        print("✅ WATSONX_PROJECT_ID is set")
    else:
        print("❌ WATSONX_PROJECT_ID is not set")

    if api_key and project_id:
        print("🎯 Credentials appear to be configured correctly")
    else:
        print("⚠️  Credentials need to be configured before using watsonx integration")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test-credentials":
        test_credentials()
    else:
        main()
