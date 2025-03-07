from game import Game
from player import Player
from board import Board

class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")
        self.game = Game(self.board, self.player1, self.player2)

    def play_game(self):
        while not self.game.is_game_over():
            print(self.board.display())
            try:
                move = input(f"{self.game.current_player.name}'s turn. Choose a position (1-9): ")
                
        
                if not move.isdigit():
                    raise ValueError("Please enter a valid number between 1 and 9.")
                
                move = int(move)

                self.game.play(move)
                
               
                winner = self.game.get_winner()
                if winner:
                    print(self.board.display())
                    print(f"{self.game.current_player.name} wins!")
                    return
                
                self.game.switch_turn()
            except ValueError as e:
                print(f"Invalid input: {e}")

        print(self.board.display())
        print("It's a draw!")

def main():
    print("Welcome to TicTacToe!")
    player1_name = input("Enter the name for Player 1: ")
    player2_name = input("Enter the name for Player 2: ")

    game = TicTacToe()
    game.player1.name = player1_name
    game.player2.name = player2_name

    
    game.play_game()

if __name__ == "__main__":
    main()
