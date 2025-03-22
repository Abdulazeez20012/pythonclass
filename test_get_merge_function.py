import unittest
import get_merging

class TestGetMergeFunction(TestCase):
	def test_that_get_merging_function_exist(self):
		addition_of_list.get_merging([1,2,3], [7, 9, 8])



	def test_that_get_merge_function_return_value(self):
		actual  = addition_of_list.get_merging([1,2,4,90], [-8,3, 5, 6])
		expected = [-8,1, 2, 3, 4, 5, 6,90]
		self.assertEqual(actual,expected)