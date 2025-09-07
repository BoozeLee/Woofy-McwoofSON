import unittest
from integrations.lambda_woofy_handler import lambda_handler

class TestWoofyAPI(unittest.TestCase):
    def test_hello(self):
        event = {}
        context = None
        result = lambda_handler(event, context)
        self.assertEqual(result['statusCode'], 200)
        self.assertIn("Woofy McWoofson", result['body'])

if __name__ == '__main__':
    unittest.main()
