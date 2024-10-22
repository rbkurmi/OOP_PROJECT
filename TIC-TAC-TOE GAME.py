class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, square, symbol):
        if self.board[square] == " ":
            self.board[square] = symbol
            if self.winner(square, symbol):
                self.current_winner = symbol
            return True
        return False

    def winner(self, square, symbol):
        # Check row, column, and diagonals
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([s == symbol for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([s == symbol for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == symbol for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == symbol for s in diagonal2]):
                return True
        return False

    def play_game(self):
        player1 = Player(input("Enter name for Player 1 (X): "), "X")
        player2 = Player(input("Enter name for Player 2 (O): "), "O")
        current_player = player1

        while True:
            self.print_board()
            move = int(input(f"{current_player.name}, enter your move (0-8): "))

            if move not in self.available_moves():
                print("Invalid move. Try again.")
                continue

            self.make_move(move, current_player.symbol)

            if self.current_winner:
                self.print_board()
                print(f"{current_player.name} wins!")
                break

            if len(self.available_moves()) == 0:
                self.print_board()
                print("It's a tie!")
                break

            # Switch players
            current_player = player2 if current_player == player1 else player1


# Run the Tic Tac Toe game
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
