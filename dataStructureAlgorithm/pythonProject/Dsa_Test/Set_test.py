import unittest

from Dsa_Function.set import Set

class SetTest(unittest.TestCase):
    def test_that_my_class_exist(self):
        pass

    def test_that_set_is_empty(self):
        set_test = Set()
        self.assertTrue(set_test.is_empty)

    def test_that_set_is_not_empty(self):
        set_test = Set()
        self.assertTrue(set_test.is_empty)
        set_test.add("steve")
        set_test.add("josh")
        self.assertEqual(2,set_test.size)


if __name__ == '__main__':
    unittest.main()
