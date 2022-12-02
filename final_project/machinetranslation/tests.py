import unittest

from translator import english_to_french,french_to_english

class Testenglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hi'),'Salut')
        self.assertEqual(english_to_french(),)     
        self.assertEqual(english_to_french('Hello'), 'Bonjour') 
        

class Testfrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(),) 
        self.assertEqual(french_to_english('Salut'),'Hi')
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 
        
        
unittest.main()
