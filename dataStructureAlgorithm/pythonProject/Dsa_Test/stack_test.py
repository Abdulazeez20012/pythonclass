import unittest

from Dsa_Function.stack import Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):

        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.stack, [10, 20, 30])

    def test_to_pop(self):

        self.stack.push(10)
        self.stack.push(20)
        popped_item = self.stack.pop()
        self.assertEqual(popped_item, 20)
        self.assertEqual(self.stack.stack, [10])
        self.stack.pop()
        self.assertEqual(self.stack.pop(), "Stack is empty")

    def test_to_peek_element_in_stack(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.peek(), 20)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 10)
        self.stack.pop()
        with self.assertRaises(Exception):
            self.stack.peek()

    def test_to_check_size_of_stack(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)
        self.stack.clear()
        self.assertEqual(self.stack.size(), 0)

    def test_that_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_clear_all_element_in_stack(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.clear()
        self.assertEqual(self.stack.stack, [])

if __name__ == '__main__':
    unittest.main()
