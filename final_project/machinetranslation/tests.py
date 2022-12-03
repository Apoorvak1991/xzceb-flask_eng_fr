"""   Tests to verify text translation """
import unittest
from translator import english_to_french,french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """Test to verify english to french translated text"""
    def test1(self):
        """Function to validate actual and expected output """
        self.assertNotEqual(english_to_french('Bonjour'), 'Hello')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        #self.assertEqual(french_to_english(), )                    #Test case for null input

class TestFrenchToEnglish(unittest.TestCase):
    """Tests to verify french to english translation"""
    def test1(self):
        """Function to validate actual and expected output """
        self.assertNotEqual(french_to_english('Hello'), 'Bonjour')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        #self.assertEqual(french_to_english(), )                        #Test for null input
        
unittest.main()
