def count_even_numbers(numbers):
    return len([num for num in numbers if num % 2 == 0])


import unittest

class TestEvenNumberCount(unittest.TestCase):

    def test_even_numbers_in_list(self):
        self.assertEqual(count_even_numbers([1, 5, 7, 3, 2, 9, 8,10]), 3)


if __name__ == '__main__':
    unittest.main()




