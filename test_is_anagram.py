import unittest
import is_anagram
class TestIsAnagram(unittest.TestCase):
    def test_is_anagram(self):
        self.assertTrue(is_anagram.is_anagram("listen", "silent"))
        self.assertFalse(is_anagram.is_anagram("road","moad"))





