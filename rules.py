from getBoard import board


class Rules:

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value

    def square_rule_violated(self, row, col, value):
        _row = row//3
        _col = col//3

        for i in range(_row * 3, _row * 3 + 3):
            for j in range(_col * 3, _col * 3 + 3):
                if board[i][j] == value:
                    return True
        return False

    def horizontal_rule_violated(self, row, col, value):

        if value in board[row-1]:
            return True

        return False

    def vertical_rule_violated(self, row, col, value):

        for i in range(len(board)):
            if value == board[i][col-1]:
                return True

        return False

    def all_cells_filled(self):

        for i in range(len(board)):
            if " " in board[i]:
                return False
        return True
