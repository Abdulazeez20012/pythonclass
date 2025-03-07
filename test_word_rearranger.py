import unittest
from word_rearranger import WordRearranger


class TestWordRearranger(unittest.TestCase):
    def test_empty_string(self):
        wordRearranger = WordRearranger("")
        result = wordRearranger.rearrange_case()
        self.assertEqual(result, "")

    def test_single_uppercase(self):
        wordRearranger = WordRearranger("A")
        result = wordRearranger.rearrange_case()
        self.assertEqual(result, "A")

    def test_single_lowercase(self):
        wordRearranger = WordRearranger("a")
        result = wordRearranger.rearrange_case()
        self.assertEqual(result, "a")

    def test_mixed_case(self):
        wordRearranger = WordRearranger("aAbBcC")
        result = wordRearranger.rearrange_case()
        self.assertEqual(result, "ABCabc")

    def test_all_uppercase(self):
        wordRearranger = WordRearranger("SemIcoloN")
        result = wordRearranger.rearrange_case()
        self.assertEqual(result, "SINemcolo")

    def test_all_lowercase(self):
        wordRearranger = WordRearranger("hello")
        result = wordRearranger.rearrange_case()
        self.assertEqual(result, "hello")
        

if __name__ == "__main__":
    unittest.main()
