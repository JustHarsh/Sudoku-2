from rules import Rules
from getBoard import board, fake_board, display_board, displayFake_board
from highlight import NORMAL, RED, PURPLE, GREEN, highlightNumber

# example board
# [[' ', ' ', 2, ' ', ' ', 1, ' ', 4, ' '], [6, ' ', 4, ' ', ' ', ' ', ' ', ' ', 8], [' ', ' ', ' ', ' ', 6, ' ', 5, ' ', ' '], [1, 7, ' ', 2, ' ', 3, ' ', 9, ' '], [' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '], [' ', 3, ' ', 6, ' ', 9, ' ', 8, 7], [' ', ' ', 3, ' ', 9, ' ', ' ', ' ', ' '], [9, ' ', ' ', ' ', ' ', ' ', 6, ' ', 4], [' ', 1, ' ', 7, ' ', ' ', 3, ' ', ' ']]

if __name__ == "__main__": # when the program is run...

    game_on = True
    possible_values = []

    while game_on:

        try:

            attempt = input(
                '''Type a row number, a column number, and a value (e.g., 1 2 9) (If you
type only one number, all the cells having the number will be highlighted
in the board.) (If you want a hint, type h): ''')
            print()
                        
            attempt_cleaned = attempt.split(" ")

            if len(attempt) in range(2, 6):
                
                # check if length of attempt_cleaned is 3. If assertion fails, skip to except block.
                assert len(attempt_cleaned) == 3

                # to check if user entered digits
                assert attempt_cleaned[0].isdigit() 
                assert attempt_cleaned[1].isdigit()
                assert attempt_cleaned[2].isdigit()

                # check if user entered digits. If assertion fails, skip to except block.
                x = int(attempt_cleaned[0])  # row
                assert x in range(1, 10) # to check if x is in between 1 and 9. If not, skip to except block.
                
                y = int(attempt_cleaned[1])  # col
                assert y in range(1, 10) # to check if y is in between 1 and 9. If not, skip to except block.
                
                val = int(attempt_cleaned[2])  # value
                assert val in range(1, 10) # to check if value is in between 1 and 9. If not, skip to except block.

                # check if the spot user wants to enter number in is empty. If assertion fails, skip to except block.
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

                else:
                    board[x-1][y-1] = PURPLE + str(val) + NORMAL
                    print()
                    display_board()

                    fake_board[x-1][y-1] = str(val)
                
                if restriction.all_cells_filled():
                    print(GREEN + "======================================================" + NORMAL)
                    print(GREEN + "You solved the sudoku! Congratulations!!!!" + NORMAL)
                    print(GREEN + "======================================================" + NORMAL)
                    game_on = False


            elif len(attempt) == 1 and attempt != "h":

                # check if user is indeed trying to highlight a number. If assertion fails, skip to except block.
                assert attempt_cleaned[0].isdigit() 
                
                color_number = highlightNumber(attempt_cleaned[0]) # creating instance
                color_number.highLight(fake_board, attempt_cleaned[0]) # highlighting

                displayFake_board(fake_board) # displaying the highlighted numbers
                
                color_number.removeHighlight(fake_board, attempt_cleaned[0]) # removing highlight

                del color_number # deleting instance
            
            elif attempt == "h":

                print("=================================HINT=========================")
                hint = input("Type the cell's row number and column number for which you want a hint: ")
                hint_cleaned = hint.split(" ")

                assert len(hint) == 3 # check if length of hint is 3. If not, skip to except block.
                assert len(hint_cleaned) == 2 # check if length of hint_cleaned is 2.

                # to check if user entered digits
                assert hint_cleaned[0].isdigit() 
                assert hint_cleaned[1].isdigit()

                hintx = int(hint_cleaned[0])
                assert hintx in range(1, 10) # check if the row is within the range of len(board)

                hinty = int(hint_cleaned[1])
                assert hinty in range(1, 10) # check if the column is within the range of len(board)

                assert board[hintx-1][hinty-1] == " " # check if the spot user wants a hint at is empty.

                for i in range(1, 10):

                    hints = Rules(hintx, hinty, i)  # creating instance                  

                    # if no rule is violated by i, then append it to possible_values

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
                        del hints # delete instance

                print("Possible values for ({}, {}) are {}".format(hintx, hinty, possible_values)) # display hint

                # clear the list so that the next time user wants a hint they do not get the old hint too. 
                possible_values.clear() 

        except:

            if len(attempt) != 1:

                if len(attempt) != 5: # run when assert len(attempt) == 5 is false
                    print(RED + "Your input is Wrong! The input length is not 5." + NORMAL)
                    print()

                elif len(attempt_cleaned) != 3: # run when assert len(attempt_cleaned) == 3 is false
                    print(RED + "Your input is Wrong! You did not input three separate numbers." + NORMAL)
                    print()
                
                # checking if the user entered numbers
                elif not attempt_cleaned[0].isdigit():
                    print(RED + "Your input is Wrong! The first input value is wrong." + NORMAL)
                    print()
                
                elif not attempt_cleaned[1].isdigit():
                    print(RED + "Your input is Wrong! The second input value is wrong." + NORMAL)
                    print()
                
                elif not attempt_cleaned[2].isdigit():
                    print(RED + "Your input is Wrong! The third input value is wrong." + NORMAL)
                    print()

                # run when row is not in the bounds of the board.
                elif x not in range(1, 10):
                    print(RED + "Your input is Wrong! The first input value is wrong." + NORMAL)
                    print()

                # run when column is not in the bounds of the board.             
                elif y not in range(1, 10):
                    print(RED + "Your input is Wrong! The second input value is wrong." + NORMAL)
                    print()

                # run when assertion to check if value is withing the permitted range of allowed numbers fails.
                elif val not in range(1, 10):
                    print(RED + "Your input is Wrong! The third input value is wrong." + NORMAL)
                    print()
                
                # runs when the spot user wants to enter a value is already occupied.
                elif board[x-1][y-1] != " ":
                    print(RED + "Your input is Wrong! The spot is not empty." + NORMAL)
                    print()

                display_board()
            
            elif len(attempt) == 1 and attempt != "h": # if user types just one letter or number.

                if not attempt_cleaned[0].isdigit(): # if user enters a letter instead of number
                    print(RED + "Your input is wrong! If you want a hint then type h." + NORMAL)
                    print()
                    displayFake_board(fake_board)
            
            elif attempt == "h": # when user wants hint but...

                # when row/col is missing
                if len(hint) != 3:
                    print(RED + "Your input is Wrong! The input length is not 3." + NORMAL)
                    print()

                # when user enters numbers without space
                elif len(hint_cleaned) != 2:
                    print(RED + "Your input is Wrong! You did not input two separate numbers." + NORMAL)
                    print()

                # checking if the user entered numbers
                elif not hint_cleaned[0].isdigit():
                    print(RED + "Your input is Wrong! The first input value is wrong." + NORMAL)
                    print()
                
                elif not hint_cleaned[1].isdigit():
                    print(RED + "Your input is Wrong! The second input value is wrong." + NORMAL)
                    print()

                # run when row value is outside the bounds of the board.             
                elif hintx not in range(1, 10):
                    print(RED + "Your input is Wrong! The first input value is wrong." + NORMAL)
                    print()
                    
                # run when column value is outside the bounds of the board.             
                elif hinty not in range(1, 10):
                    print(RED + "Your input is Wrong! The second input value is wrong." + NORMAL)
                    print()

                # run when user wants a hint at a place that is already occupied.                   
                elif board[hintx-1][hinty-1] != " ":
                    print(RED + "Your input is Wrong! The spot is not empty." + NORMAL)
                    print()

                display_board()
