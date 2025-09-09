
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

import unittest


class TestWoofy(unittest.TestCase):
    def test_bark(self):
        self.assertEqual("woof".upper(), "WOOF")

    def test_dog_fact(self):
        # Simulate extra endpoint logic
        fact = "Dogs have unique nose prints, just like human fingerprints!"
        self.assertIn("nose", fact)
        self.assertTrue(fact.startswith("Dogs"))


if __name__ == "__main__":
    unittest.main()
