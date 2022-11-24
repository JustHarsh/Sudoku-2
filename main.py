from rules import Rules
from getBoard import board, display_board

if __name__ == "__main__":

    game_on = True
    # example board - [[' ', ' ', 2, ' ', ' ', 1, ' ', 4, ' '], [6, ' ', 4, ' ', ' ', ' ', ' ', ' ', 8], [' ', ' ', ' ', ' ', 6, ' ', 5, ' ', ' '], [1, 7, ' ', 2, ' ', 3, ' ', 9, ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 3, ' ', 6, ' ', 9, ' ', 8, 7],[' ', ' ', 3, ' ', 9, ' ', ' ', ' ', ' '], [9, ' ', ' ', ' ', ' ', ' ', 6, ' ', 4],[' ', 1, ' ', 7, ' ', ' ', 3, ' ', ' ']]

    while game_on:

        try:

            attempt = list(input(
                "Type a row number, a column number, and a letter (e.g., 1 2 A): "))

            x = int(attempt[0])  # row
            y = int(attempt[2])  # col
            val = int(attempt[4])  # value

            restriction = Rules(x, y, val)

            PURPLE = "\033[0;35m"
            NORMAL = "\033[0m"

            if restriction.square_rule_violated(x, y, val):
                print("Square rule violated! Try again.")
                display_board()

            elif restriction.vertical_rule_violated(x, y, val):
                print("Vertical rule violated! Try again.")
                display_board()

            elif restriction.horizontal_rule_violated(x, y, val):
                print("Horizontal rule violated! Try again.")
                display_board()

            elif restriction.all_cells_filled():
                print("Good game!")
                game_on = False

            else:
                board[x-1][y-1] = PURPLE + str(val) + NORMAL
                display_board()



        except:

            if len(attempt) < 5 or len(attempt) > 5:
                print("Length of input is less than 5! Try again.")
                display_board()
            else:
                print("Invalid input.")
                display_board()
