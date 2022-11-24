from getBoard import board

class Errors:

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value

    def square_rule_violated(self, row, col, value):
        pass

    def horizontal_rule_violated(self, row, col, value):

        if value in board[row-1]:
            return True

        return False

    def vertical_rule_violated(self, row, col, value):

        for i in range(0,4):
            if value in board[i][col-1]:
                return True

        return False
    

    def all_cells_filled(self):

        if " " not in board[0] and " " not in board[1] and " " not in board[2] and " " not in board[3]:
            return True