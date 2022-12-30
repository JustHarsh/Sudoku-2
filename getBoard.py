'''
To display board to user and display hints to the user.
'''

from highlight import RED, NORMAL

# details to the functions will be added later
def display_board(): 
    pass


while True:

    board = None

    # to create a clone of the user input that will be used to highlight numbers on the board upon appropriate user input.
    board_clone = [[], [], [], [], [], [], [], [], []]

    try:

        board = eval(input("Enter your 2-d board (9x9): ")) # user input

        assert type(board) == list # check if the user input is a list
        assert len(board) == 9 # check if the length of outer list is 9

        # check if each inner list has 9 elements in it
        assert len(board[1]) == 9 
        assert len(board[2]) == 9
        assert len(board[3]) == 9

        # if all checks for board pass, create the clone of the board
        for i in range(len(board)):
            for j in range(len(board[i])):
                board_clone[i].append(board[i][j])

        def display_board(_board):
            '''displaying the board entered by the user.'''
            
            print('  {:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}'.format(
                1, 2, 3, 4, 5, 6, 7, 8, 9
            ))

            print('  {:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}{:3}'.format(
                '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-+'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                1, '|', _board[0][0], _board[0][1],
                _board[0][2], '|', _board[0][3],
                _board[0][4], _board[0][5], '|',
                _board[0][6], _board[0][7],
                _board[0][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                2, '|', _board[1][0], _board[1][1],
                _board[1][2], '|', _board[1][3],
                _board[1][4], _board[1][5], '|',
                _board[1][6], _board[1][7],
                _board[1][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                3, '|', _board[2][0], _board[2][1],
                _board[2][2], '|', _board[2][3],
                _board[2][4], _board[2][5], '|',
                _board[2][6], _board[2][7],
                _board[2][8], '|'
            ))

            print('  {:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}{:3}'.format(
                '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-+'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                4, '|', _board[3][0], _board[3][1],
                _board[3][2], '|', _board[3][3],
                _board[3][4], _board[3][5], '|',
                _board[3][6], _board[3][7],
                _board[3][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                5, '|', _board[4][0], _board[4][1],
                _board[4][2], '|', _board[4][3],
                _board[4][4], _board[4][5], '|',
                _board[4][6], _board[4][7],
                _board[4][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                6, '|', _board[5][0], _board[5][1],
                _board[5][2], '|', _board[5][3],
                _board[5][4], _board[5][5], '|',
                _board[5][6], _board[5][7],
                _board[5][8], '|'
            ))

            print('  {:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}{:3}'.format(
                '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-+'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                7, '|', _board[6][0], _board[6][1],
                _board[6][2], '|', _board[6][3],
                _board[6][4], _board[6][5], '|',
                _board[6][6], _board[6][7],
                _board[6][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                8, '|', _board[7][0], _board[7][1],
                _board[7][2], '|', _board[7][3],
                _board[7][4], _board[7][5], '|',
                _board[7][6], _board[7][7],
                _board[7][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                9, '|', _board[8][0], _board[8][1],
                _board[8][2], '|', _board[8][3],
                _board[8][4], _board[8][5], '|',
                _board[8][6], _board[8][7],
                _board[8][8], '|'
            ))

            print('  {:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}{:3}'.format(
                '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-+'
            ))


        display_board(board)

        break
    
    except:
            
            # if the user does not enter a list
            if type(board) != list: 
                print(RED + "Your input is wrong! You must enter your board as a nested list." + NORMAL)
                print()

            # if the length of the board, or length of any of its nested list is NOT 9
            elif len(board) != 9 or len(board[1]) != 9 or len(board[2]) != 9 or len(board[3]) != 9:
                print(RED + "Your input is wrong! Your input must be a 9x9 board!" + NORMAL)
                print()
            

