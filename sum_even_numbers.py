import unittest

def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0: 
            total += num
    return total

class TestSumEvenNumbers(unittest.TestCase):

    def test_sum_even_numbers(self):
        
        self.assertEqual(sum_even_numbers([2, 7, 9, 17, 19, 2, 8, 10]), 22)
        
class TestSumEvenNumbers(unittest.TestCase):

    def test_sum_even_numbers(self):

        self.assertEqual(sum_even_numbers([2, 7, 9, 17, 19, 2, 10, 10]), 24)


if __name__ == "__main__":
    unittest.main()




