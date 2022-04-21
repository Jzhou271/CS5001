"""
CS5001
Jing Zhou
Homework 7
Design a board by 6 rows and 7 columns and players cannot put a piece anywhere.
The piece will "fall" to the lowest empty space in that column.
While any direction of 4 pieces are connected, the winner wins the game,
otherwise, consider the game as a stalemate result
"""
board_column = 7
board_row = 6


class ConnectFour:
    def __init__(self):
        """
        initialize function of ConnectFour
        """
        self.board = [[" " for _ in range(board_column)]
                      for _ in range(board_row)]
        # next turn
        self.turns = 0
        # representation of operation stack
        self.operation_stack = []
        self.winner = ' '
        self.finished = False

    def __str__(self):
        """
        Returns a string that represents the board
        :param: self | the word string
        """
        board = ""
        for r in range(board_row):
            board += "|"
            for c in range(board_column):
                board += f"{self.board[r][c]}|"
            board += "\n"
            board += f"{'-' * 15}"
            board += "\n"
        return board

    def whose_turn(self):
        """
        get current player according to the value of self.turn
        :return: String | 'X' if step is odd, 'O' if step is even
        """
        players = ['X', 'O']
        return players[self.turns % 2]

    def add_piece(self, column):
        """
        add an item to colum of board
        :param column: indicate the destination
        :return: None
        """
        if column < 0 or column >= board_column:
            raise ValueError("invalid index")
        if self.finished:
            raise ValueError("game was already finished!")
        if self.board[0][column] != ' ':
            raise ValueError("full column specified!")
        for row in range(board_row - 1, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.whose_turn()
                self.operation_stack.append((self.turns, column))
                self.turns += 1
                break
        self.is_win()

    def undo(self):
        """
        cancel the newest operation
        :return: list | the list of board corresponding last step
        """
        if not self.operation_stack:
            raise ValueError("no operation")
        operation = self.operation_stack.pop(-1)
        column = operation[1]
        for i in range(board_row):
            if self.board[i][column] != ' ':
                self.board[i][column] = ' '
                break
        return self.board

    def check_index(self, row, col):
        """
        check whether the index is valid
        :param row: integer | the number of row
        :param col: integer | the number of column
        :return: True
        """
        return board_row > row >= 0 and board_column > col >= 0

    def check_pos(self, row, col):
        """
        check count of the symbol at the position specified by row and col
        :param row: integer | the number of row
        :param col: integer | the number of column
        :return: None
        """
        sym = self.board[row][col]
        if sym == ' ':
            return
        deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1)]
        for delta in deltas:

            count = 0
            cur_row = row
            cur_col = col
            while self.check_index(cur_row, cur_col):
                if self.board[cur_row][cur_col] == sym:
                    count += 1
                else:
                    break
                cur_row += delta[0]
                cur_col += delta[1]
            cur_row = row - delta[0]
            cur_col = col - delta[1]
            while self.check_index(cur_row, cur_col):
                if self.board[cur_row][cur_col] == sym:
                    count += 1
                else:
                    break
                cur_row -= delta[0]
                cur_col -= delta[1]
            if count >= 4:
                return True
        return False

    def is_full(self):
        """
        check whether the game board is full
        :return: False | False for game continue
        """
        space_count = sum([self.board[row].count(' ') for row
                           in range(board_row)])
        return space_count == 0

    def is_win(self):
        """
        check whether game is finished, and find the winner
        :return: boolean | True when X or O wins the game, False for game
        continue or stalemate result
        """
        if self.is_full():
            self.finished = True
        for row in range(board_row):
            for col in range(board_column):
                sym = self.board[row][col]
                if sym == ' ':
                    continue
                if self.check_pos(row, col):
                    self.winner = self.board[row][col]
                    self.finished = True
                    return True
        return False

    def get_winner(self):
        """
        get result for who wins the game or no winner
        :return: None | no winner's case
        """
        if self.winner != ' ':
            return self.winner
        return None

    def is_game_over(self):
        """
        finish the game
        :return: False | continue
        """
        self.is_win()
        return self.finished
