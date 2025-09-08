#!/usr/bin/env python3
"""
MCP GitHub Client for Secure API Access
Uses the GitHub MCP server to securely access repository secrets
"""

import requests
import json
import os


class MCPGitHubClient:
    def __init__(self, mcp_server_url="http://localhost:8080"):
        self.mcp_server_url = mcp_server_url
        self.session = requests.Session()

    def get_repo_context(self, repo_name="Woofy-McwoofSON"):
        """Get repository context through MCP server"""
        try:
            response = self.session.get(f"{self.mcp_server_url}/context/{repo_name}")
            if response.status_code == 200:
                return response.json()
            else:
                print(f"MCP Server error: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Connection error: {e}")
            return None

    def health_check(self):
        """Check MCP server health"""
        try:
            response = self.session.get(f"{self.mcp_server_url}/health")
            if response.status_code == 200:
                return response.json()
            return None
        except requests.RequestException:
            return None


def main():
    """Main function to test MCP GitHub client"""
    print("🔗 MCP GitHub Client Test")
    print("=" * 30)

    client = MCPGitHubClient()

    # Health check
    health = client.health_check()
    if health:
        print(f"✅ MCP Server: {health['status']}")
    else:
        print("❌ MCP Server not available")
        return

    # Get repository context
    context = client.get_repo_context()
    if context:
        print("✅ Repository context retrieved")
        print(f"Context: {context}")
    else:
        print("❌ Could not retrieve repository context")


if __name__ == "__main__":
    main()
