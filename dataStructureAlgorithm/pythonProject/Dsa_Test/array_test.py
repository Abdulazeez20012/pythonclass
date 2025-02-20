import unittest
from Dsa_Function.array import Array

class TestArray(unittest.TestCase):
    def setUp(self):
        self.list = Array()

    def test_add_element_to_list(self):
        self.list.add(10)
        self.list.add(20)
        self.assertEqual(self.list.array, [10, 20])
        self.assertEqual(self.list.size(), 2)

    def test_to_remove_one_element_and_element_that_is_not_from_list(self):
        self.list.add(10)
        self.list.add(20)
        self.list.remove(10)
        self.assertEqual(self.list.array, [20])
        self.assertEqual(self.list.size(), 1)

        self.list.remove(30)
        self.assertEqual(self.list.array, [20])
        self.assertEqual(self.list.size(), 1)

    def test_get_element_from_list_with_index(self):
        self.list.add(10)
        self.list.add(20)
        self.assertEqual(self.list.get(0), 10)
        self.assertEqual(self.list.get(1), 20)
        self.assertEqual(self.list.get(2), "Index out of range")

    def test_that_list_contains_element(self):
        self.list.add(10)
        self.assertTrue(self.list.contains(10))
        self.assertFalse(self.list.contains(20))

    def test_size_of_list(self):
        self.list.add(10)
        self.list.add(20)
        self.list.add(30)
        self.assertEqual(self.list.size(), 3)

        self.list.remove(20)
        self.assertEqual(self.list.size(), 2)

    def test_to_clear_list(self):
        self.list.add(10)
        self.list.add(20)
        self.list.clear()
        self.assertEqual(self.list.array, [])
        self.assertEqual(self.list.size(), 0)


if __name__ == '__main__':
    unittest.main()
