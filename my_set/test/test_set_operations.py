import unittest

from my_set.set import set_operation

class TestSetOperation(unittest.TestCase):

    def setUp(self):
        self.test_set_operation = set_operation()

    def test_to_add_element(self):
        actual = add_element(set([1, 2, 3]), 4)
        expected = {1, 2, 3, 4}
        self.assertEqual(actual, expected)

    def test_to_remove_element(self):
        actual = remove_element(set([1, 2, 3, 4]), 3)
        expected = {1, 2, 4}
        self.assertEqual(actual, expected)
        with self.assertRaises(KeyError):
            remove_element(set([1, 2]), 3)

    def test_to_check_if_element_exists(self):
        actual = element_exists(set([1, 2, 3]), 2)
        expected = True
        self.assertEqual(actual, expected)
        actual = element_exists(set([1, 2, 3]), 5)
        expected = False
        self.assertEqual(actual, expected)

    def test_union_sets(self):
        actual = union_sets(set([1, 2, 3]), set([3, 4, 5]))
        expected = {1, 2, 3, 4, 5}
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
