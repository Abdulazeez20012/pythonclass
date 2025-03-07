import unittest
from Dsa_Function.pascals_triangle.triangle import PascalsTriangle

class TestPascalsTriangle(unittest.TestCase):
    def setUp(self):
        self.pascals_triangle = PascalsTriangle()

    def test_generate_zero_rows(self):
        self.assertEqual(self.pascals_triangle.generate(0), [])

    def test_generate_one_row(self):
        self.assertEqual(self.pascals_triangle.generate(1), [[1]])

    def test_generate_two_rows(self):
        self.assertEqual(self.pascals_triangle.generate(2), [[1], [1, 1]])

    def test_generate_three_rows(self):
        self.assertEqual(self.pascals_triangle.generate(3), [[1], [1, 1], [1, 2, 1]])

    def test_generate_four_rows(self):
        self.assertEqual(self.pascals_triangle.generate(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

    def test_generate_five_rows(self):
        self.assertEqual(self.pascals_triangle.generate(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])

    def test_generate_six_rows(self):
        self.assertEqual(self.pascals_triangle.generate(6), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])

    def test_generate_seven_rows(self):
        self.assertEqual(self.pascals_triangle.generate(7), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]])

    def test_generate_eight_rows(self):
        self.assertEqual(self.pascals_triangle.generate(8), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]])

    def test_generate_nine_rows(self):
        self.assertEqual(self.pascals_triangle.generate(9), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1]])

    def test_generate_ten_rows(self):
        self.assertEqual(self.pascals_triangle.generate(10), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]])

if __name__ == "__main__":
    unittest.main()
