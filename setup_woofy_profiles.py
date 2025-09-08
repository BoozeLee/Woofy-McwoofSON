#!/usr/bin/env python3
"""
🐕‍🦺 WOOFY McWOOFSON Enterprise Profile Setup Script

This script helps configure GitHub profiles for the Woofy-McWoofSON enterprise setup.
Run this to get detailed instructions for manual profile configuration.
"""

import json
import webbrowser
import os
from pathlib import Path

def load_config():
    """Load the Woofy profile configuration"""
    config_path = Path(__file__).parent / "woofy_profile_config.json"
    with open(config_path, 'r') as f:
        return json.load(f)

def print_personal_profile_setup(config):
    """Print personal profile setup instructions"""
    print("\n" + "="*60)
    print("PHASE 1A: PERSONAL PROFILE SETUP")
    print("="*60)

    personal = config['personal_profile']

    print("\n📝 MANUAL STEPS REQUIRED:")
    print("1. Go to: https://github.com/settings/profile")
    print("2. Update the following fields:")

    print(f"\n   Name: {personal['name']}")
    print(f"   Bio: {personal['bio']}")
    print(f"   Company: {personal['company']}")
    print(f"   Location: {personal['location']}")
    print(f"   Website: {personal['website']}")
    print(f"   Twitter: @{personal['twitter']}")

    print("\nAVATAR UPDATE:")
    print(f"   Description: {personal['avatar_description']}")
    print("   TIP: Generate a psychedelic atomic dog avatar using AI image tools")

    print("\nPINNED REPOSITORIES:")
    print("   Go to: https://github.com/settings/pinned")
    print("   Pin these repositories:")
    for repo in personal['pinned_repos']:
        print(f"   - {repo}")

    print("\nSECURITY SETTINGS:")
    print("   Go to: https://github.com/settings/security")
    print("   - Enable 2FA if not already enabled")
    print("   - Review SSH keys and personal access tokens")

def print_organization_profile_setup(config):
    """Print organization profile setup instructions"""
    print("\n" + "="*60)
    print("PHASE 1B: ORGANIZATION PROFILE SETUP")
    print("="*60)

    org = config['organization_profile']

    print("\nORGANIZATION CREATION:")
    print("1. Go to: https://github.com/organizations/new")
    print("2. Create organization with these details:")

    print(f"\n   Organization Name: {org['name']}")
    print(f"   Description: {org['description']}")
    print(f"   Website: {org['website']}")
    print(f"   Email: {org['email']}")
    print(f"   Location: {org['location']}")

    print("\nORGANIZATION LOGO:")
    print(f"   Description: {org['logo_description']}")
    print("   TIP: Generate a psychedelic bakery-dog fusion logo")

    print("\nBILLING & PLAN:")
    print("   Go to: https://github.com/organizations/YOUR-ORG/settings/billing")
    print("   Upgrade to Team/Enterprise plan for:")
    print("   - Advanced security features")
    print("   - Unlimited private repositories")
    print("   - Priority support")

    print("\nTEAM MANAGEMENT:")
    print("   Go to: https://github.com/organizations/YOUR-ORG/settings/members")
    print("   - Invite team members")
    print("   - Set up role-based access control (RBAC)")
    print("   - Configure SAML SSO (Enterprise only)")

def print_enterprise_features_setup(config):
    """Print enterprise features setup instructions"""
    print("\n" + "="*60)
    print("PHASE 1C: ENTERPRISE FEATURES ACTIVATION")
    print("="*60)

    enterprise = config['enterprise_features']

    print("\nSECURITY FEATURES:")
    print("   For each repository, enable:")
    for feature in enterprise['security_features']:
        print(f"   - {feature}")

    print("\nCOLLABORATION FEATURES:")
    print("   Enable in repository settings:")
    for feature in enterprise['collaboration_features']:
        print(f"   - {feature}")

    print("\nREPOSITORY SETTINGS:")
    print("   Go to: https://github.com/YOUR-ORG/REPO/settings")
    print("   - Configure branch protection rules")
    print("   - Set up automated security scanning")
    print("   - Enable dependency alerts")

def print_business_config_summary(config):
    """Print business configuration summary"""
    print("\n" + "="*60)
    print("PHASE 1D: BUSINESS CONFIGURATION SUMMARY")
    print("="*60)

    business = config['business_config']

    print("\nREVENUE STREAMS:")
    for stream in business['revenue_streams']:
        print(f"   - {stream}")

    print("\nTARGET MARKETS:")
    for market in business['target_markets']:
        print(f"   - {market}")

    print("\nPARTNERSHIP CRITERIA:")
    for criteria in business['partnership_criteria']:
        print(f"   - {criteria}")

def open_github_pages():
    """Open relevant GitHub pages for setup"""
    urls = [
        "https://github.com/settings/profile",
        "https://github.com/organizations/new",
        "https://github.com/BoozeLee/woofy-mcwoofson-enterprise/settings"
    ]

    print("\n🌐 OPENING GITHUB PAGES...")
    for url in urls:
        print(f"   Opening: {url}")
        webbrowser.open(url)

def main():
    """Main setup function"""
    print("WOOFY McWOOFSON ENTERPRISE PROFILE SETUP")
    print("="*60)
    print("Welcome to the Woofy-McWoofSON Enterprise Profile Configuration!")
    print("This script will guide you through setting up your GitHub profiles")
    print("for maximum business impact and revenue generation potential.")

    try:
        config = load_config()

        print_personal_profile_setup(config)
        print_organization_profile_setup(config)
        print_enterprise_features_setup(config)
        print_business_config_summary(config)

        print("\n🚀 READY TO LAUNCH?")
        print("Follow the instructions above to configure your profiles.")
        print("Once complete, your GitHub presence will be optimized for:")
        print("   • Business partnerships")
        print("   • Revenue generation")
        print("   • Enterprise credibility")
        print("   • Community engagement")

        response = input("\nOpen GitHub setup pages in browser? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            open_github_pages()

        print("\n✅ PROFILE SETUP COMPLETE!")
        print("Your Woofy-McWoofSON enterprise is ready to unleash revenue! 🐕💰")

    except FileNotFoundError:
        print("❌ Error: woofy_profile_config.json not found!")
        print("Please ensure the configuration file is in the same directory.")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()