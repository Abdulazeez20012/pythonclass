import unittest
from player import Player
from board import Board
from game import Game

class TestGame(unittest.TestCase):
    def test_that_player_play_game(self):
        board = Board()
        player1 = Player("Azeez", "X")
        player2 = Player("Mario", "O")
        game = Game(board, player1, player2)

        game.play(0)
        self.assertEqual(board.board[0], "X")
        game.switch_turn()
        game.play(1)
        self.assertEqual(board.board[1], "O")
        self.assertIsNone(game.get_winner())

    def test_that_game_can_switch_turn(self):
        board = Board()
        player1 = Player("Azeez", "X")
        player2 = Player("Mario", "O")
        game = Game(board, player1, player2)

        self.assertEqual(game.current_player, player1)
        game.switch_turn()
        self.assertEqual(game.current_player, player2)

if __name__ == "__main__":
    unittest.main()
