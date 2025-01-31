import unittest
from queue_test import Queue


class queue_test(unittest.TestCase):

    def test_enqueue(self):
        q = Queue()
        q.enqueue(5)
        self.assertEqual(q.size(), 1)

    def test_dequeue(self):
        q = Queue()
        q.enqueue(5)
        q.enqueue(10)
        item = q.dequeue()
        self.assertEqual(item, 5)
        self.assertEqual(q.size(), 1)

    def test_peek(self):
        q = Queue()
        q.enqueue(5)
        q.enqueue(10)
        item = q.peek()
        self.assertEqual(item, 5)

    def test_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(5)
        self.assertFalse(q.is_empty())

    def test_size(self):
        q = Queue()
        self.assertEqual(q.size(), 0)
        q.enqueue(5)
        q.enqueue(10)
        self.assertEqual(q.size(), 2)
        q.dequeue()
        self.assertEqual(q.size(), 1)


if __name__ == "__main__":
    unittest.main()
