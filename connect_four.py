class ConnectFour:

    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.players = ['X', 'O']
        self.turn = 0

    def print_board(self):
        """Print the Connect Four board."""
        print('+---------------+')
        for row in self.board:
            print('|', end=' ')
            for cell in row:
                print(cell, end=' ')
            print('|')
        print('+---------------+')

    def is_valid_move(self, column):
        """Check if a move is valid in the specified column."""
        return self.board[0][column] == ' '

    def make_move(self, column, player):
        """Place a player's piece in the specified column."""
        for row in range(5, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = player
                return True
        return False

    def is_board_full(self):
        """Check if the board is full."""
        return all(cell != ' ' for row in self.board for cell in row)

    def play(self):
        """Run the Connect Four game."""
        while True:
            self.print_board()
            player = self.players[self.turn % 2]

            # Adjust the user input to be 0 - based
            column = int(input(f"Player {player}, enter your move (column 1-7): ")) - 1

            # Checks if user input is valid for the board
            if not (0 <= column <= 6):
                print("Invalid column. Please choose a number between 1 and 7.")
                continue

            if not self.is_valid_move(column):
                print("Column is full. Please choose another column.")
                continue

            if not self.make_move(column, player):
                print("Invalid move. Please choose another column.")
                continue

            if self.check_winner(player):
                self.print_board()
                print(f"Player {player} wins!")
                break

            if self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break

            self.turn += 1

        return input("Do you want to play again? (yes/no): ").lower() == "yes"

    def check_winner(self, player):
        """Check if the specified player has won."""
        for row in range(6):
            for col in range(4):
                if all(self.board[row][col + i] == player for i in range(4)):
                    return True

        for row in range(3):
            for col in range(7):
                if all(self.board[row + i][col] == player for i in range(4)):
                    return True

        for row in range(3):
            for col in range(4):
                if all(self.board[row + i][col + i] == player for i in range(4)):
                    return True

                if all(self.board[row + i][col + 3 - i] == player for i in range(4)):
                    return True

        return False
