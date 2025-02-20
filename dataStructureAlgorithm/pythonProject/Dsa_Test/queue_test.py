import unittest
from Dsa_Function.queue import Queue


class QueueTest(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_that_queue_is_empty_on_creation(self):
        self.assertTrue(self.queue.is_empty())

    def test_that_queue_is_not_empty(self):
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())

    def test_that_can_dequeue_is_not_empty(self):
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_that_can_dequeue_element(self ):
        self.queue.enqueue(50)
        self.assertEqual(self.queue.dequeue(), 50)
        self.assertTrue(self.queue.is_empty())

    def test_that_dequeue_from_empty_queue_raises_exception(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_that_queue_follows_fifo_order(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.dequeue(), 20)
        self.assertEqual(self.queue.dequeue(), 30)

    def test_that_can_peek_queue_element(self):
        self.queue.enqueue(50)
        self.assertEqual(self.queue.dequeue(), 50)
        self.assertTrue(self.queue.is_empty())

    def test_that_when_we_peek_an_empty_queue_raise_IndexError(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()


    def test_that_can_check_size_of_queue(self):
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.assertEqual(self.queue.size(), 3)



if __name__ == '__main__':
    unittest.main()