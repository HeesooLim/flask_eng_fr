import unittest
from translator import english_to_french, french_to_english

class TestMethods(unittest.TestCase):
    def test_en2fr(self):
        """
        Test English to French
        """
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_fr2en(self):
        """
        Test French to English
        """
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()