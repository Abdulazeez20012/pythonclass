import unittest
from Dsa_Function.increament import Increament

class TestIncrementArray(unittest.TestCase):

    def test_increment_array_1(self):
        input_array = [3, 4, 2]
        expected_output = [3, 4, 3]
        self.assertEqual(Increament(input_array), expected_output)

    def test_increment_array_2(self):
        input_array = [9, 9, 9]
        expected_output = [1, 0, 0, 0]
        self.assertEqual(Increament(input_array), expected_output)


if __name__ == "__main__":
    unittest.main()
