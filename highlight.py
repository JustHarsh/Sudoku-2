'''to highlight and un-highlight the number entered by the user'''

# required colors below
BACKGROUND_YELLOW = "\033[43m"
BOLD_RED = "\033[1;31m"
RED = "\033[0;31m"
NORMAL = "\033[0m"
PURPLE = "\033[0;35m"
GREEN = "\033[0;32m"

class highlightNumber:
    '''contains functions to highlight and then un-highlight the number the user entered.'''


    def __init__(self, number):
        '''initialising the number entered by the user.[['''
        self.number = number

    def highLight(self, _board, number):
        '''to highlight the number entered by the user.'''

        for i in range(len(_board)):
            for j in range(len(_board[i])):
                if int(number) == _board[i][j]:
                    _board[i][j] = BOLD_RED + BACKGROUND_YELLOW + str(_board[i][j]) + NORMAL # highlighting
    

    def removeHighlight(self, _board, number):
        '''to un-highlight the number entered by the user.'''

        for i in range(len(_board)):
            for j in range(len(_board[i])):
                if ("\x1b[1;31m\x1b[43m" + number + "\x1b[0m") == _board[i][j]:
                    _board[i][j] = _board[i][j][12] # undoing the highlighting
