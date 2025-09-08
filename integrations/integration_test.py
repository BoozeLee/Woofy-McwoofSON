#!/usr/bin/env python3
"""
Complete Integration Test - Enterprise Security Framework
Demonstrates the full secure AI workflow for KiloCoder

Mission Status: ✅ INTEGRATION TEST READY
Security Level: 🔒 ENTERPRISE GRADE
Zero-Exposure Implementation: ✅ ACTIVE
"""

import os
import sys
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def test_environment_setup():
    """Test environment variable configuration"""
    print("🔧 Testing Environment Setup...")
    print("-" * 40)

    required_vars = [
        "PERPLEXITY_API_KEY",
        "OPENROUTER_API_KEY_PRIMARY",
        "OPENROUTER_API_KEY_SECONDARY",
        "OPENROUTER_API_KEY_TERTIARY",
        "GROQ_API_KEY",
    ]

    missing_vars = []
    for var in required_vars:
        value = os.getenv(var)
        if not value or value.endswith("_here"):
            missing_vars.append(var)
            print(f"❌ {var}: MISSING or PLACEHOLDER")
        else:
            print(f"✅ {var}: CONFIGURED")

    if missing_vars:
        print(f"\n⚠️  MISSING VARIABLES: {', '.join(missing_vars)}")
        print("Please update .env with real API keys before running full tests")
        return False

    print("\n✅ Environment setup: PASSED")
    return True


def test_secure_imports():
    """Test secure module imports"""
    print("\n🔐 Testing Secure Imports...")
    print("-" * 40)

    try:
        from secure_ai_apis import KiloCoderSecureAI, SecurityError

        print("✅ Secure AI APIs: IMPORTED")

        from key_rotation import AutomatedKeyRotation

        print("✅ Key Rotation: IMPORTED")

        from security_monitor import SecurityMonitor, get_security_status

        print("✅ Security Monitor: IMPORTED")

        print("\n✅ Secure imports: PASSED")
        return True

    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False


def test_secure_client_initialization():
    """Test secure client initialization without API calls"""
    print("\n🚀 Testing Secure Client Initialization...")
    print("-" * 40)

    try:
        from secure_ai_apis import SecurePerplexityClient, SecureOpenRouterClient

        # Test Perplexity client initialization
        perplexity = SecurePerplexityClient()
        print("✅ Perplexity client: INITIALIZED")

        # Test OpenRouter client initialization
        openrouter = SecureOpenRouterClient()
        print("✅ OpenRouter client: INITIALIZED")

        # Test combined client
        from secure_ai_apis import KiloCoderSecureAI

        ai = KiloCoderSecureAI()
        print("✅ Combined AI client: INITIALIZED")

        print("\n✅ Client initialization: PASSED")
        return True

    except Exception as e:
        print(f"❌ Client initialization failed: {e}")
        return False


def test_security_monitoring():
    """Test security monitoring functionality"""
    print("\n📊 Testing Security Monitoring...")
    print("-" * 40)

    try:
        from security_monitor import SecurityMonitor

        monitor = SecurityMonitor()

        # Test logging
        monitor.log_api_request("test_api", True, {"test": "data"})
        monitor.log_rate_limit("test_api", 0)
        monitor.log_security_violation("test_violation", {"details": "test"})

        # Test report generation
        report = monitor.generate_security_report()
        print("✅ Security report: GENERATED")
        print(f"   Status: {report['status']}")
        print(f"   Anomalies: {len(report['anomalies'])}")

        # Test dashboard
        dashboard = monitor.get_dashboard_data()
        print("✅ Security dashboard: ACTIVE")
        print(f"   Total requests: {dashboard['summary']['total_requests']}")

        print("\n✅ Security monitoring: PASSED")
        return True

    except Exception as e:
        print(f"❌ Security monitoring failed: {e}")
        return False


def test_key_rotation_system():
    """Test key rotation system"""
    print("\n🔄 Testing Key Rotation System...")
    print("-" * 40)

    try:
        from key_rotation import AutomatedKeyRotation

        rotator = AutomatedKeyRotation()

        # Test status check
        status = rotator.get_rotation_status()
        print("✅ Rotation status: RETRIEVED")
        print(f"   Perplexity status: {status['perplexity']['status']}")
        print(f"   OpenRouter status: {status['openrouter']['status']}")

        # Test rotation checks
        rotator.check_all_keys()
        print("✅ Key rotation check: COMPLETED")

        print("\n✅ Key rotation system: PASSED")
        return True

    except Exception as e:
        print(f"❌ Key rotation failed: {e}")
        return False


def test_emergency_response():
    """Test emergency response system (simulation only)"""
    print("\n🚨 Testing Emergency Response System...")
    print("-" * 40)

    # Note: We won't actually run the emergency script as it disables APIs
    emergency_script = "integrations/emergency_response.sh"

    if os.path.exists(emergency_script):
        print("✅ Emergency response script: EXISTS")
        print(f"   Location: {emergency_script}")

        # Check if executable (on Unix systems)
        if os.name != "nt":  # Not Windows
            import stat

            if os.stat(emergency_script).st_mode & stat.S_IEXEC:
                print("✅ Emergency script: EXECUTABLE")
            else:
                print("⚠️  Emergency script: NOT EXECUTABLE")
        else:
            print("ℹ️  Windows system: Script execution depends on shell")

        print("\n✅ Emergency response system: READY")
        return True
    else:
        print(f"❌ Emergency script not found: {emergency_script}")
        return False


def run_full_integration_test():
    """Run complete integration test suite"""
    print("🧪 KILOCODER ENTERPRISE SECURITY INTEGRATION TEST")
    print("=" * 60)
    print(f"⏰ Test Start: {datetime.now().isoformat()}")
    print()

    test_results = {
        "environment_setup": test_environment_setup(),
        "secure_imports": test_secure_imports(),
        "client_initialization": test_secure_client_initialization(),
        "security_monitoring": test_security_monitoring(),
        "key_rotation": test_key_rotation_system(),
        "emergency_response": test_emergency_response(),
    }

    print("\n" + "=" * 60)
    print("📋 TEST RESULTS SUMMARY")
    print("=" * 60)

    passed = 0
    total = len(test_results)

    for test_name, result in test_results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status}: {test_name.replace('_', ' ').title()}")
        if result:
            passed += 1

    print(f"\n📊 Overall Result: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 ALL TESTS PASSED - Enterprise Security Framework Ready!")
        print("🚀 Ready for production deployment with API keys")
    else:
        print("⚠️  Some tests failed - Review and fix before production use")
        print("🔧 Check missing dependencies or configuration issues")

    # Generate test report
    test_report = {
        "timestamp": datetime.now().isoformat(),
        "results": test_results,
        "summary": {
            "passed": passed,
            "total": total,
            "success_rate": f"{(passed/total)*100:.1f}%" if total > 0 else "0%",
        },
    }

    report_file = (
        f"integration_test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )
    with open(report_file, "w") as f:
        json.dump(test_report, f, indent=2)

    print(f"\n📄 Detailed report saved: {report_file}")

    return passed == total


if __name__ == "__main__":
    success = run_full_integration_test()
    sys.exit(0 if success else 1)
