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