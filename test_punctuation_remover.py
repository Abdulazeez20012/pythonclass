import unittest
from punctuation_remover import PunctuationRemover

class TestPunctuationRemover(unittest.TestCase):
    
    def setUp(self):
        self.remover = PunctuationRemover()

    def test_remove_single_punctuation(self):
        input_string = "He,ll.o!"
        expected_output = "Hello"
        self.assertEqual(self.remover.remove_special_punctuation(input_string), expected_output)

    def test_remove_multiple_punctuation(self):
        input_string = "Hello, world!!"
        expected_output = "Hello world"
        self.assertEqual(self.remover.remove_special_punctuation(input_string), expected_output)

    def test_string_without_punctuation(self):
        input_string = "Hello world"
        expected_output = "Hello world"
        self.assertEqual(self.remover.remove_special_punctuation(input_string), expected_output)

    def test_string_with_only_punctuation(self):
        input_string = "!@#$%"
        expected_output = ""
        self.assertEqual(self.remover.remove_special_punctuation(input_string), expected_output)

if __name__ == "__main__":
    unittest.main()
