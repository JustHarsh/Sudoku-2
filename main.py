from rules import Rules
from getBoard import board, display_board


if __name__ == "__main__":

    game_on = True
    possible_values = []
    # example board - [[' ', ' ', 2, ' ', ' ', 1, ' ', 4, ' '], [6, ' ', 4, ' ', ' ', ' ', ' ', ' ', 8], [' ', ' ', ' ', ' ', 6, ' ', 5, ' ', ' '], [1, 7, ' ', 2, ' ', 3, ' ', 9, ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 3, ' ', 6, ' ', 9, ' ', 8, 7],[' ', ' ', 3, ' ', 9, ' ', ' ', ' ', ' '], [9, ' ', ' ', ' ', ' ', ' ', 6, ' ', 4],[' ', 1, ' ', 7, ' ', ' ', 3, ' ', ' ']]

    while game_on:

        try:

            attempt = input(
                "Type a row number, a column number, and a letter (e.g., 1 2 9): ")
            
            attempt_cleaned = attempt.split(" ")
            
            if attempt != 'h':

                x = int(attempt_cleaned[0])  # row
                assert x in range(1, 10)

                y = int(attempt_cleaned[1])  # col
                assert y in range(1, 10)

                val = int(attempt_cleaned[2])  # value
                assert val in range(1, 10)

                assert board[x-1][y-1] == " "

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
            
            elif attempt == "h":

                print("=================================HINT=========================")
                hint = input("Type the cell's row number and column number for which you want a hint: ")
                hint_cleaned = hint.split(" ")

                assert len(hint) == 3
                assert hint_cleaned[0].isdigit()
                assert hint_cleaned[1].isdigit()

                hintx = int(hint_cleaned[0])
                assert hintx in range(1, 10)

                hinty = int(hint_cleaned[1])
                assert hinty in range(1, 10)

                assert board[hintx-1][hinty-1] == " "

                for i in range(1, 10):

                    hints = Rules(hintx, hinty, i)                    

                    if hints.square_rule_violated(hintx, hinty, i):
                        del hints
                        continue

                    elif hints.vertical_rule_violated(hintx, hinty, i):
                        del hints
                        continue

                    elif hints.horizontal_rule_violated(hintx, hinty, i):
                        del hints
                        continue

                    else:
                        possible_values.append(i)
                        del hints
                
                print("Possible values for ({}, {}) are {}".format(hintx, hinty, possible_values))

                possible_values.clear()



        except:

            if attempt != "h":

                if (len(attempt) != 5):
                    print("Your input is Wrong! The input length is not 5.")
                    display_board()
                
                elif (x not in range(1, 10)):
                    print("Your input is Wrong! The first input value is wrong.")
                    display_board()
                
                elif (y not in range(1, 10)):
                    print("Your input is Wrong! The second input value is wrong.")
                    display_board()
                
                elif (val not in range(1, 10)):
                    print("Your input is Wrong! The third input value is wrong.")
                    display_board()
                
                elif (board[x-1][y-1] != " "):
                    print("Your input is Wrong! The spot is not empty.")
                    display_board()
            
            elif attempt == "h":

                if len(hint) != 3:
                    print("Your input is Wrong! The input length is not 3.")
                
                elif hintx not in range(1, 10):
                    print("Your input is Wrong! The first input value is wrong.")
                
                elif hinty not in range(1, 10):
                    print("Your input is Wrong! The second input value is wrong.")
                
                elif board[hintx][hinty] != " ":
                    print("Your input is Wrong! The spot is not empty.")



            
