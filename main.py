from rules import Rules
from getBoard import board, fake_board, display_board, displayFake_board
from highlight import NORMAL, RED, PURPLE, GREEN, highlightNumber


if __name__ == "__main__":

    game_on = True
    possible_values = []

    while game_on:

        try:

            attempt = input(
                '''Type a row number, a column number, and a value (e.g., 1 2 9) (If you
type only one number, all the cells having the number will be highlighted
in the board.) (If you want a hint, type h): ''')
                        
            attempt_cleaned = attempt.split(" ")

            assert len(attempt_cleaned) == 3

            if len(attempt) == 1 and attempt != "h":

                assert attempt_cleaned[0].isdigit()
                
                color_number = highlightNumber(attempt_cleaned[0])
                color_number.highLight(fake_board, attempt_cleaned[0])
                displayFake_board(fake_board)

                del color_number

            
            elif attempt == "h":

                print("=================================HINT=========================")
                hint = input("Type the cell's row number and column number for which you want a hint: ")
                hint_cleaned = hint.split(" ")

                assert len(hint) == 3
                assert len(hint_cleaned) == 2

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

                        
            elif len(attempt) == 5:

                assert attempt_cleaned[0].isdigit(), attempt_cleaned[1].isdigit()
                
                x = int(attempt_cleaned[0])  # row
                assert x in range(1, 10)

                y = int(attempt_cleaned[1])  # col
                assert y in range(1, 10)

                val = int(attempt_cleaned[2])  # value
                assert val in range(1, 10)

                assert board[x-1][y-1] == " "

                restriction = Rules(x, y, val)

                if restriction.square_rule_violated(x, y, val):
                    print(RED + "Square rule violated! Try again." + NORMAL)
                    print()
                    display_board()

                elif restriction.vertical_rule_violated(x, y, val):
                    print(RED + "Vertical rule violated! Try again." + NORMAL)
                    print()
                    display_board()

                elif restriction.horizontal_rule_violated(x, y, val):
                    print(RED + "Horizontal rule violated! Try again." + NORMAL)
                    print()
                    display_board()

                elif restriction.all_cells_filled():
                    print(GREEN + "===================================" + NORMAL)
                    print(GREEN + "You solved the sudoku! Congratulations!!!!" + NORMAL)
                    print(GREEN + "===================================" + NORMAL)
                    game_on = False

                else:
                    board[x-1][y-1] = PURPLE + str(val) + NORMAL
                    print()
                    display_board()

                    fake_board[x-1][y-1] = str(val)

        except:

            if len(attempt) != 1:

                if (not attempt_cleaned[0].isdigit()) or (not attempt_cleaned[1].isdigit()) or (not attempt_cleaned[2].isdigit()):
                    print(RED + "Your input is wrong! You must enter numbers ONLY." + NORMAL)
                    print()
                    display_board()

                elif len(attempt) != 5:
                    print(RED + "Your input is Wrong! The input length is not 5." + NORMAL)
                    print()
                    display_board()

                elif len(attempt_cleaned) != 3:
                    print(RED + "Your input is Wrong! You did not input three separate numbers." + NORMAL)
                    print()
                    display_board()
                
                elif x not in range(1, 10):
                    print(RED + "Your input is Wrong! The first input value is wrong." + NORMAL)
                    print()
                    display_board()
                
                elif y not in range(1, 10):
                    print(RED + "Your input is Wrong! The second input value is wrong." + NORMAL)
                    print()
                    display_board()
                
                elif val not in range(1, 10):
                    print(RED + "Your input is Wrong! The third input value is wrong." + NORMAL)
                    print()
                    display_board()
                
                elif board[x-1][y-1] != " ":
                    print(RED + "Your input is Wrong! The spot is not empty." + NORMAL)
                    print()
                    display_board()
            
            elif len(attempt) == 1 and attempt != "h":

                if not attempt_cleaned[0].isdigit():
                    print(RED + "Your input is wrong! If you want a hint then type 'h'." + NORMAL)
                    print()
                    displayFake_board(fake_board)
            
            elif attempt == "h":

                if (not attempt_cleaned[0].isdigit()) or (not attempt_cleaned[1].isdigit()):
                    print(RED + "Your input is wrong! You must enter numbers ONLY." + NORMAL)
                    print()
                    display_board()

                elif len(hint) != 3:
                    print(RED + "Your input is Wrong! The input length is not 3." + NORMAL)
                    print()
                    display_board()
                
                elif len(hint_cleaned) != 3:
                    print(RED + "Your input is Wrong! You did not input two separate numbers." + NORMAL)
                    print()
                    display_board()
                
                elif hintx not in range(1, 10):
                    print(RED + "Your input is Wrong! The first input value is wrong." + NORMAL)
                    print()
                    display_board()

                                 
                elif hinty not in range(1, 10):
                    print(RED + "Your input is Wrong! The second input value is wrong." + NORMAL)
                    print()
                    display_board()
                                   
                elif board[hintx-1][hinty-1] != " ":
                    print(RED + "Your input is Wrong! The spot is not empty." + NORMAL)
                    print()
                    display_board()
