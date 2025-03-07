import unittest
from seven_segment_display import SevenSegmentDisplay

class TestSevenSegmentDisplay(unittest.TestCase):
    def test_segment_0(self):
        expected = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', ' ', ' ', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        actual = SevenSegmentDisplay.get_seven_segment_display(0)
        self.assertEqual(expected, actual)

    def test_segment_1(self):
        expected = [
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', '#']
        ]
        actual = SevenSegmentDisplay.get_seven_segment_display(1)
        self.assertEqual(expected, actual)

    def test_segment_2(self):
        expected = [
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', ' '],
            ['#', '#', '#', '#']
        ]
        actual = SevenSegmentDisplay.get_seven_segment_display(2)
        self.assertEqual(expected, actual)

    def test_segment_3(self):
        expected = [
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        actual = SevenSegmentDisplay.get_seven_segment_display(3)
        self.assertEqual(expected, actual)

    def test_segment_4(self):
        expected = [
            [' ', ' ', ' ', ' '],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', ' ']
        ]
        actual = SevenSegmentDisplay.get_seven_segment_display(4)
        self.assertEqual(expected, actual)

    def test_segment_5(self):
        expected = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', ' '],
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        actual = SevenSegmentDisplay.get_seven_segment_display(5)
        self.assertEqual(expected, actual)

    def test_segment_6(self):
        expected = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', ' '],
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        actual = SevenSegmentDisplay.get_seven_segment_display(6)
        self.assertEqual(expected, actual)

    def test_segment_7(self):
        expected = [
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', '#'],
            [' ', ' ', ' ', '#']
        ]
        actual = SevenSegmentDisplay.get_seven_segment_display(7)
        self.assertEqual(expected, actual)

    def test_segment_8(self):
        expected = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        actual = SevenSegmentDisplay.get_seven_segment_display(8)
        self.assertEqual(expected, actual)

    def test_segment_9(self):
        expected = [
            ['#', '#', '#', '#'],
            ['#', ' ', ' ', '#'],
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', '#'],
            ['#', '#', '#', '#']
        ]
        actual = SevenSegmentDisplay.get_seven_segment_display(9)
        self.assertEqual(expected, actual)

    def test_all_digits(self):
        for i in range(10):
            self.assertIsNotNone(SevenSegmentDisplay.get_seven_segment_display(i))

    def test_invalid_input_negative(self):
        self.assertIsNone(SevenSegmentDisplay.get_seven_segment_display(-1))

    def test_invalid_input_large(self):
        self.assertIsNone(SevenSegmentDisplay.get_seven_segment_display(10))

if __name__ == '__main__':
    unittest.main()
