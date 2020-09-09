#Test simple to complex. Work your way up.
import unittest
# https://docs.python.org/3/library/unittest.html docs on unittest
# PY.py file Import any file that you will use for testing.
import PY
#unittest.TestCase is a bunch of methods that you can run.
#general structure of a test
# 1. You create your class to be called at the end
# 2. Inherit from unittest.TestCase
class TestCap(unittest.TestCase):
# 3. Have a function to be called.
# usually numbered. so next = test_two_word, test_three_word etc
    def test_one_word(self):
        text = 'python'
        # 4. calling functions off of the script. cap_text from PY.py file
        result = PY.cap_text(text)
        #result that you want.
        self.assertEqual(result, 'Python')
#another example test.
    def test_multiple_words(self): 
        text = 'the brown fox jumped quickly over the lazy dog.'
        result = PY.cap_text(text)
        self.assertEqual(result, 'The Brown Fox Jumped Quickly Over The Lazy Dog.')

if __name__=='__main__':
    unittest.main()