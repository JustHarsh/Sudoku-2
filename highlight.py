
BACKGROUND_YELLOW = "\033[43m"
BOLD_RED = "\033[1;31m"
RED = "\033[0;31m"
NORMAL = "\033[0m"
PURPLE = "\033[0;35m"
GREEN = "\033[0;32m"



class highlightNumber:

    def __init__(self, number):
        self.number = number

    def highLight(self, _board: list, number):

        for i in range(len(_board)):
            for j in range(len(_board[i])):
                if int(number) == _board[i][j]:
                    _board[i][j] = BOLD_RED + BACKGROUND_YELLOW + str(_board[i][j]) + NORMAL
        
        return _board