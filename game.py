class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1

    def switch_turn(self):
        """ Switch turn to the other player """
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def play(self, index):
        """ Handle the gameplay logic """
        try:
            self.board.make_move(index, self.current_player.symbol)
        except ValueError as e:
            raise ValueError(str(e))

    def get_winner(self):
        """ Check if there's a winner """
        return self.board.check_winner()

    def is_game_over(self):
        """ Check if the game is over (either a winner or draw) """
        return self.board.is_full() or self.get_winner() is not None
