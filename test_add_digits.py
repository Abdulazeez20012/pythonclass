import unittest
import add_digits
class TestAddDigits(unittest.TestCase):
	def test_add_digits_exist(self):
		add_digits.add_digits([1,2,3,4,])

	def test_add_digits_correct(self):
		actual = add_digits.add_digits([1,2])
		expected = 3  
		self.assertEqual(actual, expected)
sss