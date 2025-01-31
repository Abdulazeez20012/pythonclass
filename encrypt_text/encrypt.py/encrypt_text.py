import unittest
from encrypt_text import encrypt


class TestEncryptText(unittest.TestCase):
    def test_sample_case(self):
        input_text = "Hello, World!"
        expected_output = "Uryyb, jbeyq!"
        self.assertEqual(encrypt(input_text), expected_output)

    def test_sample_case2(self):
        input_text = "Hello, World!"
        expected_output = "Uryyb, jbeyq!"
        self.assertEqual(encrypt(input_text, 2), expected_output)
        input_text = "Hello, World!"


if __name__ == '__main__':
    unittest.main()
