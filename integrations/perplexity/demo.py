#!/usr/bin/env python3
"""
Perplexity Bot Integration Demo

This script demonstrates the usage of the Perplexity client for testing purposes.
Ensure your .env file contains PERPLEXITY_API_KEY before running.

Usage:
    python integrations/perplexity/demo.py
"""

import sys
import os

# Add the integrations directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from perplexity_client import PerplexityClient

def main():
    """
    Demo function showing Perplexity client usage.
    """
    print("🐕 WOOFY McWOOFSON - Perplexity Integration Demo")
    print("=" * 50)

    try:
        # Initialize client
        print("🔑 Initializing Perplexity client...")
        client = PerplexityClient()

        # Example queries
        queries = [
            "What is the current population of Tokyo?",
            "Explain quantum computing in simple terms",
            "What are the latest developments in AI safety?"
        ]

        for i, query in enumerate(queries, 1):
            print(f"\n📝 Query {i}: {query}")
            print("-" * 40)

            try:
                response = client.query(query)
                print("✅ Response received successfully!")

                # Print a summary (avoid printing full response for brevity)
                if 'choices' in response and response['choices']:
                    content = response['choices'][0].get('message', {}).get('content', '')
                    # Print first 200 characters
                    preview = content[:200] + "..." if len(content) > 200 else content
                    print(f"📄 Preview: {preview}")
                else:
                    print("📄 Response structure may vary - check full response in logs")

            except Exception as e:
                print(f"❌ Query failed: {str(e)}")

        # Clean up
        client.close()
        print("\n🎉 Demo completed successfully!")

    except ValueError as e:
        print(f"❌ Configuration Error: {str(e)}")
        print("💡 Make sure PERPLEXITY_API_KEY is set in your .env file")
    except Exception as e:
        print(f"❌ Demo failed: {str(e)}")

if __name__ == "__main__":
    main()