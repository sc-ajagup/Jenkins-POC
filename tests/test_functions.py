# tests/test_functions.py

import unittest
from main import is_even, is_palindrome, reverse

class TestFunctions(unittest.TestCase):

    def test_is_even(self):
        # Test even numbers
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))
        
        # Test odd numbers
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-7))
        self.assertFalse(is_even(1))

    def test_is_palindrome(self):
        # Test palindromes
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome(""))

        # Test non-palindromes
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("OpenAI"))
    
    def test_reverse(self):
        # Test regular strings
        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse("world"), "dlrow")
        self.assertEqual(reverse("OpenAI"), "IAnepO")
        
        # Test empty string
        self.assertEqual(reverse(""), "")
        
        # Test single character
        self.assertEqual(reverse("a"), "a")
        
        # Test strings with spaces
        self.assertEqual(reverse("a b c"), "c b a")
        self.assertEqual(reverse(" hello "), " olleh ")

if __name__ == "__main__":
    unittest.main()
