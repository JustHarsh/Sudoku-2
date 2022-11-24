# to avoid circular imports

board = eval(input("Enter your 2-d board (4x4): "))

def display_board():

    print('  {:2}{:2}{:2}{:2}'.format(
        1, 2, 3, 4
    ))

    print('  {:2}{:2}{:2}{:3}'.format(
        '+-', '+-', '+-', '+-+'
    ))

    print('{} {}{} {}{}{} {}{}'.format(
        1, '|', board[0][0], board[0][1],
        '|', board[0][2], board[0][3], '|'
    ))

    print('{} {}{} {}{}{} {}{}'.format(
        2, '|', board[1][0], board[1][1],
        '|', board[1][2], board[1][3], '|'
    ))

    print('  {:2}{:2}{:2}{:3}'.format(
        '+-', '+-', '+-', '+-+'
    ))

    print('{} {}{} {}{}{} {}{}'.format(
        3, '|', board[2][0], board[2][1],
        '|', board[2][2], board[2][3], '|'
    ))

    print('{} {}{} {}{}{} {}{}'.format(
        4, '|', board[3][0], board[3][1],
        '|', board[3][2], board[3][3], '|'
    ))

    print('  {:2}{:2}{:2}{:3}'.format(
        '+-', '+-', '+-', '+-+'
    ))

display_board()
