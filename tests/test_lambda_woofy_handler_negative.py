"""Negative and edge case tests for lambda_woofy_handler.

Covers invalid event types, invalid action types, unknown actions,
and ensures structured error responses.
"""
import unittest
import json
from integrations.lambda_woofy_handler import lambda_handler


class TestWoofyAPINegative(unittest.TestCase):
    def _parse(self, result):
        self.assertIn('statusCode', result)
        self.assertIn('body', result)
        body = json.loads(result['body'])
        return body

    def test_none_event(self):
        result = lambda_handler(None, None)
        self.assertEqual(result['statusCode'], 400)
        body = self._parse(result)
        self.assertEqual(body.get('status'), 'error')

    def test_string_event(self):
        result = lambda_handler("not-a-dict", None)
        self.assertEqual(result['statusCode'], 400)
        body = self._parse(result)
        self.assertIn('error', body)

    def test_non_string_action(self):
        result = lambda_handler({'action': 123}, None)
        self.assertEqual(result['statusCode'], 400)
        body = self._parse(result)
        self.assertEqual(body.get('status'), 'error')

    def test_unknown_action(self):
        result = lambda_handler({'action': 'nope'}, None)
        self.assertEqual(result['statusCode'], 400)
        body = self._parse(result)
        self.assertEqual(body.get('error'), 'Unknown action')
        self.assertIn('supported', body)
        self.assertTrue(len(body.get('supported', [])) >= 1)

    def test_context_mock(self):
        class Ctx:  # minimal context simulation
            function_name = 'fn'
            memory_limit_in_mb = 128
        result = lambda_handler({'action': 'ping'}, Ctx())
        self.assertEqual(result['statusCode'], 200)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
