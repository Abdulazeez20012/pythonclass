def check_even(numbers):
    return [num % 2 == 0 for num in numbers]



import unittest

class TestEvenOddCheck(unittest.TestCase):

    def test_mixed_numbers(self):
        self.assertEqual(check_even([10, 3, 7, 1, 9, 4, 2, 8, 5, 6]),  [True, False, False, False, False, True, True, True, False, True])



























if __name__ == '__main__':
    unittest.main()
