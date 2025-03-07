import unittest
from word_with_ce import WordWithCE

class TestWordWithCE(unittest.TestCase):

    def test_for_word_that_can_be_divided(self):
        word = WordWithCE("hello")
        result = word.insert_ce_in_middle()
        self.assertNotEqual(result, "hecello")

    def test_for_word_that_cannot_be_divided(self):
        word = WordWithCE("joy")
        result = word.insert_ce_in_middle()
        self.assertEqual(result, "joyce")

    def test_single_character_word(self):
        word = WordWithCE("a")
        result = word.insert_ce_in_middle()
        self.assertEqual(result, "ace")

    def test_for_an_empty_string(self):
        word = WordWithCE("")
        result = word.insert_ce_in_middle()
        self.assertEqual(result, "ce")  

if __name__ == "__main__":
    unittest.main()
