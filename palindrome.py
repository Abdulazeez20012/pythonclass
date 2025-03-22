def check_palindromes(strings):
    return [s == s[::-1] for s in strings]


import unittest

class TestPalindromeFunction(unittest.TestCase):
    def test_is_palindrome(self):
       
        input_list = ["madam","apple", "racecar", ]
        expected_output = [True, False, True]
        
       
        self.assertEqual(check_palindromes(input_list), expected_output)


