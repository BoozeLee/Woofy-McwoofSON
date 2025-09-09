
# WOOFY SECURITY GUARDRAILS - AUTO-APPLIED
import os
import sys
import logging

# Disable AWS credential logging
for logger_name in ['boto3', 'botocore', 'urllib3', 's3transfer']:
    logging.getLogger(logger_name).setLevel(logging.CRITICAL)

# Suppress credential discovery
os.environ['AWS_DEFAULT_OUTPUT'] = 'json'
os.environ['AWS_CLI_FILE_ENCODING'] = 'UTF-8'

# Import security guardrails
try:
    from security_guardrails import SecurityGuardrails
    SecurityGuardrails.secure_log("Security guardrails active")
except ImportError:
    pass

"""API tests for lambda_woofy_handler.

Focus on positive path for supported actions and basic structure.
Detailed negative/edge cases live in dedicated negative test module.
"""

import unittest
import json
from integrations.lambda_woofy_handler import lambda_handler


class TestWoofyAPIHappyPaths(unittest.TestCase):
    def _parse(self, result):
        self.assertIn("statusCode", result)
        self.assertIn("body", result)
        self.assertIn("headers", result)
        self.assertEqual(result["headers"].get("Content-Type"), "application/json")
        return json.loads(result["body"])

    def test_hello_action(self):
        result = lambda_handler({"action": "hello"}, None)
        self.assertEqual(result["statusCode"], 200)
        body = self._parse(result)
        self.assertEqual(body.get("status"), "ok")
        self.assertIn("Woofy McWoofson", body.get("message", ""))

    def test_ping_action(self):
        result = lambda_handler({"action": "ping"}, None)
        self.assertEqual(result["statusCode"], 200)
        body = self._parse(result)
        self.assertTrue(body.get("pong"))

    def test_default_action_when_missing(self):
        result = lambda_handler({}, None)  # defaults to hello
        self.assertEqual(result["statusCode"], 200)
        body = self._parse(result)
        self.assertEqual(body.get("status"), "ok")

    def test_idempotent_hello(self):
        event = {"action": "hello"}
        r1 = lambda_handler(event, None)
        r2 = lambda_handler(event, None)
        self.assertEqual(r1["statusCode"], r2["statusCode"])
        self.assertEqual(r1["headers"], r2["headers"])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
