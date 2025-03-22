import unittest

class TestCountVowels(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("python is sweet"), 4)  
        self.assertEqual(count_vowels("hello"), 2)  
        self.assertEqual(count_vowels("aeiou"), 5)  
        self.assertEqual(count_vowels("bcdfghjklmnpqrstvwxyz"), 0)  
        self.assertEqual(count_vowels("I love programming"), 6)  











if __name__ == "__main__":
    unittest.main()
