from rules import Rules
from getBoard import board, display_board
from custom_functions import Input_manipulation

if __name__ == "__main__":

    game_on = True
    # example board - [[' ', ' ', 2, ' ', ' ', 1, ' ', 4, ' '], [6, ' ', 4, ' ', ' ', ' ', ' ', ' ', 8], [' ', ' ', ' ', ' ', 6, ' ', 5, ' ', ' '], [1, 7, ' ', 2, ' ', 3, ' ', 9, ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 3, ' ', 6, ' ', 9, ' ', 8, 7],[' ', ' ', 3, ' ', 9, ' ', ' ', ' ', ' '], [9, ' ', ' ', ' ', ' ', ' ', 6, ' ', 4],[' ', 1, ' ', 7, ' ', ' ', 3, ' ', ' ']]

    while game_on:

        try:

            attempt = input(
                "Type a row number, a column number, and a letter (e.g., 1 2 A): ")
            strip = Input_manipulation(attempt)

            # tuple(strip.fstrip(attempt)) = ("1", "2", "A")
            attempt_cleaned = tuple(strip.fstrip(attempt))

            x = int(attempt_cleaned[0])  # row
            y = int(attempt_cleaned[1])  # col
            val = int(attempt_cleaned[2])  # value

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

            else:
                board[x-1][y-1] = PURPLE + val + NORMAL
                display_board()

        except:

            if len(attempt) < 5 or len(attempt) > 5:
                print("Length of input is less than 5! Try again.")
            else:
                print("Invalid input.")
                display_board()

        finally:
            '''
            finally, after each try or except round, check if all cells are filled. If yes, print
            "Good game!" and stop the game.
            '''

            if restriction.all_cells_filled():
                print("Good game!")
                game_on = False