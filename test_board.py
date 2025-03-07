import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def test_for_initial_board(self):
        board = Board()
        self.assertEqual(board.board, [" "] * 9)

    def test_Than_can_make_move(self):
        board = Board()
        board.make_move(0, "X")
        self.assertEqual(board.board[0], "X")
        self.assertNotIn(0, board.available_spaces)

    def test_that_when_an_invalid_move_is_inputed_raise_value_error(self):
        board = Board()
        board.make_move(0, "X")
        with self.assertRaises(ValueError):
            board.make_move(0, "O")

    def test_that_user_input_value_more_than_the_range_to_raise_out_of_range_move(self):
        board = Board()
        with self.assertRaises(ValueError):
            board.make_move(10, "X")

    def test_for_winner_detection(self):
        board = Board()
        board.make_move(0, "X")
        board.make_move(1, "X")
        board.make_move(2, "X")
        self.assertEqual(board.check_winner(), "X")

    def test_full_board(self):
        board = Board()
        for i in range(9):
            board.make_move(i, "X" if i % 2 == 0 else "O")
        self.assertTrue(board.is_full())


if __name__ == "__main__":
    unittest.main()
