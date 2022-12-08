'''
To display board to user and display hints to the user.
'''

from highlight import RED, NORMAL

# details to the functions will be added later
def display_board(): 
    pass

def displayFake_board():
    pass


while True:

    board = None

    # to create a clone of the user input that will be used to highlight numbers on the board upon appropriate user input.
    fake_board = [[], [], [], [], [], [], [], [], []]

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
                fake_board[i].append(board[i][j])

        def display_board():
            '''displaying the board entered by the user.'''
            
            print('  {:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}'.format(
                1, 2, 3, 4, 5, 6, 7, 8, 9
            ))

            print('  {:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}{:3}'.format(
                '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-+'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                1, '|', board[0][0], board[0][1],
                board[0][2], '|', board[0][3],
                board[0][4], board[0][5], '|',
                board[0][6], board[0][7],
                board[0][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                2, '|', board[1][0], board[1][1],
                board[1][2], '|', board[1][3],
                board[1][4], board[1][5], '|',
                board[1][6], board[1][7],
                board[1][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                3, '|', board[2][0], board[2][1],
                board[2][2], '|', board[2][3],
                board[2][4], board[2][5], '|',
                board[2][6], board[2][7],
                board[2][8], '|'
            ))

            print('  {:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}{:3}'.format(
                '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-+'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                4, '|', board[3][0], board[3][1],
                board[3][2], '|', board[3][3],
                board[3][4], board[3][5], '|',
                board[3][6], board[3][7],
                board[3][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                5, '|', board[4][0], board[4][1],
                board[4][2], '|', board[4][3],
                board[4][4], board[4][5], '|',
                board[4][6], board[4][7],
                board[4][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                6, '|', board[5][0], board[5][1],
                board[5][2], '|', board[5][3],
                board[5][4], board[5][5], '|',
                board[5][6], board[5][7],
                board[5][8], '|'
            ))

            print('  {:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}{:3}'.format(
                '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-+'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                7, '|', board[6][0], board[6][1],
                board[6][2], '|', board[6][3],
                board[6][4], board[6][5], '|',
                board[6][6], board[6][7],
                board[6][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                8, '|', board[7][0], board[7][1],
                board[7][2], '|', board[7][3],
                board[7][4], board[7][5], '|',
                board[7][6], board[7][7],
                board[7][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                9, '|', board[8][0], board[8][1],
                board[8][2], '|', board[8][3],
                board[8][4], board[8][5], '|',
                board[8][6], board[8][7],
                board[8][8], '|'
            ))

            print('  {:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}{:3}'.format(
                '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-+'
            ))


        display_board()


        def displayFake_board(fakeBoard):

            '''displaying the clone of the board entered by the user. It will not have any coloring whatsoever.'''

            print('  {:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}'.format(
                1, 2, 3, 4, 5, 6, 7, 8, 9
            ))

            print('  {:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}{:3}'.format(
                '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-+'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                1, '|', fakeBoard[0][0], fakeBoard[0][1],
                fakeBoard[0][2], '|', fakeBoard[0][3],
                fakeBoard[0][4], fakeBoard[0][5], '|',
                fakeBoard[0][6], fakeBoard[0][7],
                fakeBoard[0][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                2, '|', fakeBoard[1][0], fakeBoard[1][1],
                fakeBoard[1][2], '|', fakeBoard[1][3],
                fakeBoard[1][4], fakeBoard[1][5], '|',
                fakeBoard[1][6], fakeBoard[1][7],
                fakeBoard[1][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                3, '|', fakeBoard[2][0], fakeBoard[2][1],
                fakeBoard[2][2], '|', fakeBoard[2][3],
                fakeBoard[2][4], fakeBoard[2][5], '|',
                fakeBoard[2][6], fakeBoard[2][7],
                fakeBoard[2][8], '|'
            ))

            print('  {:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}{:3}'.format(
                '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-+'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                4, '|', fakeBoard[3][0], fakeBoard[3][1],
                fakeBoard[3][2], '|', fakeBoard[3][3],
                fakeBoard[3][4], fakeBoard[3][5], '|',
                fakeBoard[3][6], fakeBoard[3][7],
                fakeBoard[3][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                5, '|', fakeBoard[4][0], fakeBoard[4][1],
                fakeBoard[4][2], '|', fakeBoard[4][3],
                fakeBoard[4][4], fakeBoard[4][5], '|',
                fakeBoard[4][6], fakeBoard[4][7],
                fakeBoard[4][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                6, '|', fakeBoard[5][0], fakeBoard[5][1],
                fakeBoard[5][2], '|', fakeBoard[5][3],
                fakeBoard[5][4], fakeBoard[5][5], '|',
                fakeBoard[5][6], fakeBoard[5][7],
                fakeBoard[5][8], '|'
            ))

            print('  {:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}{:3}'.format(
                '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-+'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                7, '|', fakeBoard[6][0], fakeBoard[6][1],
                fakeBoard[6][2], '|', fakeBoard[6][3],
                fakeBoard[6][4], fakeBoard[6][5], '|',
                fakeBoard[6][6], fakeBoard[6][7],
                fakeBoard[6][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                8, '|', fakeBoard[7][0], fakeBoard[7][1],
                fakeBoard[7][2], '|', fakeBoard[7][3],
                fakeBoard[7][4], fakeBoard[7][5], '|',
                fakeBoard[7][6], fakeBoard[7][7],
                fakeBoard[7][8], '|'
            ))

            print('{} {}{} {} {}{}{} {} {}{}{} {} {}{}'.format(
                9, '|', fakeBoard[8][0], fakeBoard[8][1],
                fakeBoard[8][2], '|', fakeBoard[8][3],
                fakeBoard[8][4], fakeBoard[8][5], '|',
                fakeBoard[8][6], fakeBoard[8][7],
                fakeBoard[8][8], '|'
            ))

            print('  {:2}{:2}{:2}{:2}{:2}{:2}{:2}{:2}{:3}'.format(
                '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-', '+-+'
            ))
        
        break
    
    except:

            if type(board) != list:
                print(RED + "Your input is wrong! You must enter your board as a nested list." + NORMAL)
                print()

            elif len(board) != 9 or len(board[1]) != 9 or len(board[2]) != 9 or len(board[3]) != 9:
                print(RED + "Your input is wrong! Your input must be a 9x9 board!" + NORMAL)
                print()
            

