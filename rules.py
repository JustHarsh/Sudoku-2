'''defining rules that the user has to play by to finish the puzzle.'''

from getBoard import board # importing board entered by the user.


class Rules:

    def __init__(self, row, col, value):
        '''initialising row, column and value entered by the user.'''

        self.row = row
        self.col = col
        self.value = value

    def square_rule_violated(self, row, col, value):
        '''
        checks if there is a duplication of letters in the nearest surrounding of its place on the board. 
        For example, 

        1 2 3 4
        +-+-+-+-+
       1|   |B  |
       2|B  |   |
        +-+-+-+-+
       3|C  |  D|
       4|A C|B  |
        +-+-+-+-+

        The square rule is violated in the example above because C at (4,2) is one of the nearest neighbours of
        C at (3,1). However, the below would NOT be an example of this violation.

        1 2 3 4
        +-+-+-+-+
       1|   |B  |
       2|B  |   |
        +-+-+-+-+
       3|C  |C D|
       4|A C|B  |
        +-+-+-+-+

        Here, C at (3,3) does NOT violate the square rule because it is not in its local square coordinates i.e., 
        nearest neighbour, [(3,1), (3,2), (4,1), (4,2)].

        Hence, if the square rule is violated, the function returns True. 
        '''
        

        starter_row = (row-1)//3
        starter_col = (col-1)//3

        for i in range(starter_row * 3, starter_row * 3 + 3):
            for j in range(starter_col * 3, starter_col * 3 + 3):
                if board[i][j] == value:
                    return True
        return False

    def horizontal_rule_violated(self, row, col, value):
        '''
        if there is a duplication of letters along a horizontal line on the board, then function 
        returns True, else it returns False. 
        '''

        if value in board[row-1]:
            return True

        return False

    def vertical_rule_violated(self, row, col, value):
        '''
        if there is a duplication of letters along a vertical line on the board, then function 
        returns True, else it returns False. 
        '''

        for i in range(len(board)):
            if value == board[i][col-1]:
                return True

        return False

    def all_cells_filled(self):
        '''to check if the entire board is filled. Returns True when there is no coordinate is " ".'''

        for i in range(len(board)):
            if " " in board[i]:
                return False
        return True
