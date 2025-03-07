class Board:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.available_spaces = set(range(1, 10))

    def display(self):
        return f"""
        {self.board[0]} | {self.board[1]} | {self.board[2]}
        ---------
        {self.board[3]} | {self.board[4]} | {self.board[5]}
        ---------
        {self.board[6]} | {self.board[7]} | {self.board[8]}
        """

    def make_move(self, index, symbol):
        if index < 1 or index > 9:
            raise ValueError("Index out of range. Choose a number between 1 and 9.")

        index -= 1

        if self.board[index] != " ":
            raise ValueError("This position is already taken. Choose another one.")

        self.board[index] = symbol
        self.available_spaces.remove(index + 1)

    def is_full(self):
        return len(self.available_spaces) == 0

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != " ":
                return self.board[combination[0]]
        return None
