import random


class TicTT:

    def __init__(self):
        self.board = []

    def new_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_first_player(self):
        return random.randint(0, 1)

    def spot(self, row, col, player):
        self.board[row][col] = player

    def player_winning(self, player):
        n = len(self.board)
        win = None
        # check all rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # check all columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.new_board()

        player = 'X' if self.get_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers (#row #column) ").split()))
            print()

            # fixing spot
            self.spot(row - 1, col - 1, player)

            
            if self.player_winning(player):
                print(f"Player {player} wins the game!")
                break

            if self.board_filled():
                print("Match Draw!")
                break

            player = self.player_turn(player)

        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTT()
tic_tac_toe.start()