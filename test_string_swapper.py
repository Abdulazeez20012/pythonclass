import unittest
from string_swapper import StringSwapper

class TestStringSwapper(unittest.TestCase):

    def test_valid_swap(self):
        stringswapper = StringSwapper("hello", "world")
        result = stringswapper.swap_first_two_chars()
        self.assertNotEqual(result, "woello horld")
       
    def test_to_swap_same_strings(self):
        stringswapper = StringSwapper("abcd", "abcd")
        result = stringswapper.swap_first_two_chars()
        self.assertEqual(result, "abcd abcd")

    def test_to_swap_different_strings(self):
        stringswapper = StringSwapper("abc","xyz")
        result = stringswapper.swap_first_two_chars()
        self.assertEqual(result,"xyc abz")

if __name__ == "__main__":
    unittest.main()
