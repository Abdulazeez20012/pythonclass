def capitalize_first_letter(strings):
    return [string.capitalize() for string in strings]


import unittest

class TestCapitalizeFunction(unittest.TestCase):

    def test_mixed_case(self):
        self.assertEqual(capitalize_first_letter(["red", "orange", "yello","green","blue"]),(["Red", "Orange", "Yello","Green","Blue"])

    
































if __name__ == '__main__':
    unittest.main()
