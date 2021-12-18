# Author: Mike Filburn
# Date: 12/2/20
# Description: Program is a minesweeper game. Select a row and column to feveal what is under the selected tile. If it
# is a bomb, the game is over and the user looses. If it is not a bomb, it will reveal an integer of the amount of
# adjacent bombs to the selected tile helping the user deduce where the bombs are located. In the event there are no
# bombs adjacent all adjacent tiles will be revealed recursively until all adjacent tiles have an integer value or
# the adjacent tiles go out of bounds of the board. If all tiles are revealed other than the ones covering bombs,
# the user wins.

from os import system, name
import random #used for random board generation

"""
Below function that is called recursively. it is assumed that the selected tile that called this function 
was an empty tile so all adjacent tiles to that one don't have a bomb. therefore we have at least 8
adjacent tiles without a bomb which may have more adjacent bombs to that. that is why it is nessisary to have
a recursive function. In addition special care was taken to prevent checking outside the game boundries (outside the 
arrays).
Takes in (integer, integer, list, list) and returns nothing.
field is modified but all other variables are not modified.
"""
# below we know that we will only be getting a empty tile going in. therefore we can surmise that all 8 surrounding tiles
# do not have a bomb. Knowing this we can traverse to those 8 squares recursively until one is found.
def empty_tile(guess_row, guess_col, field, answer_field):
        # Uncover the selected tile
        field[int(guess_row)][int(guess_col)] = answer_field[int(guess_row)][int(guess_col)]

        # need to get all adjacent tiles with bombs and sum them up.
        # Below if/elif statements make sure we do not go out of bounds in the array.
        if int(guess_col) == 0 and int(guess_row) == 0:
            temp = 0
            if answer_field[int(guess_row) - 0][int(guess_col) + 1] == '*':  # mid right
                temp = temp + 1
            if answer_field[int(guess_row) + 1][int(guess_col) - 0] == '*':  # bottom mid
                temp = temp + 1
            if answer_field[int(guess_row) + 1][int(guess_col) + 1] == '*':  # bottom right
                temp = temp + 1

            if temp > 0:
                field[int(guess_row)][int(guess_col)] = temp

            if temp == 0:
                if field[int(guess_row) - 0][int(guess_col) + 1] == "■":
                    empty_tile(int(guess_row) - 0, int(guess_col) + 1, field, answer_field)
                if field[int(guess_row) + 1][int(guess_col) - 0] == "■":
                    empty_tile(int(guess_row) + 1, int(guess_col) - 0, field, answer_field)
                if field[int(guess_row) + 1][int(guess_col) + 1] == "■":
                    empty_tile(int(guess_row) + 1, int(guess_col) + 1, field, answer_field)

        elif int(guess_col) == 8 and int(guess_row) == 8:
            temp = 0
            if answer_field[int(guess_row) - 1][int(guess_col) - 1] == '*':  # top left
                temp = temp + 1
            if answer_field[int(guess_row) - 1][int(guess_col) - 0] == '*':  # top middle
                temp = temp + 1
            if answer_field[int(guess_row) - 0][int(guess_col) - 1] == '*':  # mid left
                temp = temp + 1
            if temp > 0:
                field[int(guess_row)][int(guess_col)] = temp
            if temp == 0:
                if field[int(guess_row) - 1][int(guess_col) - 1] == "■":
                    empty_tile(int(guess_row) - 1, int(guess_col) - 1, field, answer_field)
                if field[int(guess_row) - 1][int(guess_col) - 0] == "■":
                    empty_tile(int(guess_row) - 1, int(guess_col) - 0, field, answer_field)
                if field[int(guess_row) - 0][int(guess_col) - 1] == "■":
                    empty_tile(int(guess_row) - 0, int(guess_col) - 1, field, answer_field)

        elif int(guess_col) == 0 and int(guess_row) == 8:
            temp = 0
            if answer_field[int(guess_row) - 1][int(guess_col) - 0] == '*':  # top middle
                temp = temp + 1
            if answer_field[int(guess_row) - 1][int(guess_col) + 1] == '*':  # top right
                temp = temp + 1
            if answer_field[int(guess_row) - 0][int(guess_col) + 1] == '*':  # mid right
                temp = temp + 1
            if temp > 0:
                field[int(guess_row)][int(guess_col)] = temp
            if temp == 0:
                if field[int(guess_row) - 1][int(guess_col) - 0] == "■":
                    empty_tile(int(guess_row) - 1, int(guess_col) - 0, field, answer_field)
                if field[int(guess_row) - 1][int(guess_col) + 1] == "■":
                    empty_tile(int(guess_row) - 1, int(guess_col) + 1, field, answer_field)
                if field[int(guess_row) - 0][int(guess_col) + 1] == "■":
                    empty_tile(int(guess_row) - 0, int(guess_col) + 1, field, answer_field)

        elif int(guess_col) == 8 and int(guess_row) == 0:
            temp = 0
            if answer_field[int(guess_row) - 0][int(guess_col) - 1] == '*':  # mid left
                temp = temp + 1
            if answer_field[int(guess_row) + 1][int(guess_col) - 1] == '*':  # bottom left
                temp = temp + 1
            if answer_field[int(guess_row) + 1][int(guess_col) - 0] == '*':  # bottom mid
                temp = temp + 1
            if temp > 0:
                field[int(guess_row)][int(guess_col)] = temp
            if temp == 0:
                if field[int(guess_row) - 0][int(guess_col) - 1] == "■":
                    empty_tile(int(guess_row) - 0, int(guess_col) - 1, field, answer_field)
                if field[int(guess_row) + 1][int(guess_col) - 1] == "■":
                    empty_tile(int(guess_row) + 1, int(guess_col) - 1, field, answer_field)
                if field[int(guess_row) + 1][int(guess_col) - 0] == "■":
                    empty_tile(int(guess_row) + 1, int(guess_col) - 0, field, answer_field)

        elif int(guess_col) == 0 and int(guess_row) > 0:
            temp = 0
            if answer_field[int(guess_row) - 1][int(guess_col) - 0] == '*':  # top middle
                temp = temp + 1
            if answer_field[int(guess_row) - 1][int(guess_col) + 1] == '*':  # top right
                temp = temp + 1
            if answer_field[int(guess_row) - 0][int(guess_col) + 1] == '*':  # mid right
                temp = temp + 1
            if answer_field[int(guess_row) + 1][int(guess_col) - 0] == '*':  # bottom mid
                temp = temp + 1
            if answer_field[int(guess_row) + 1][int(guess_col) + 1] == '*':  # bottom right
                temp = temp + 1
            if temp > 0:
                field[int(guess_row)][int(guess_col)] = temp
            if temp == 0:
                if field[int(guess_row) - 1][int(guess_col) - 0] == "■":
                    empty_tile(int(guess_row) - 1, int(guess_col) - 0, field, answer_field)
                if field[int(guess_row) - 1][int(guess_col) + 1] == "■":
                    empty_tile(int(guess_row) - 1, int(guess_col) + 1, field, answer_field)
                if field[int(guess_row) - 0][int(guess_col) + 1] == "■":
                    empty_tile(int(guess_row) - 0, int(guess_col) + 1, field, answer_field)
                if field[int(guess_row) + 1][int(guess_col) - 0] == "■":
                    empty_tile(int(guess_row) + 1, int(guess_col) - 0, field, answer_field)
                if field[int(guess_row) + 1][int(guess_col) + 1] == "■":
                    empty_tile(int(guess_row) + 1, int(guess_col) + 1, field, answer_field)

        elif int(guess_col) > 0 and int(guess_row) == 0:
            temp = 0
            if answer_field[int(guess_row) - 0][int(guess_col) - 1] == '*':  # mid left
                temp = temp + 1
            if answer_field[int(guess_row) - 0][int(guess_col) + 1] == '*':  # mid right
                temp = temp + 1
            if answer_field[int(guess_row) + 1][int(guess_col) - 1] == '*':  # bottom left
                temp = temp + 1
            if answer_field[int(guess_row) + 1][int(guess_col) - 0] == '*':  # bottom mid
                temp = temp + 1
            if answer_field[int(guess_row) + 1][int(guess_col) + 1] == '*':  # bottom right
                temp = temp + 1
            if temp > 0:
                field[int(guess_row)][int(guess_col)] = temp
            if temp == 0:
                if field[int(guess_row) - 0][int(guess_col) - 1] == "■":
                    empty_tile(int(guess_row) - 0, int(guess_col) - 1, field, answer_field)
                if field[int(guess_row) - 0][int(guess_col) + 1] == "■":
                    empty_tile(int(guess_row) - 0, int(guess_col) + 1, field, answer_field)
                if field[int(guess_row) + 1][int(guess_col) - 1] == "■":
                    empty_tile(int(guess_row) + 1, int(guess_col) - 1, field, answer_field)
                if field[int(guess_row) + 1][int(guess_col) - 0] == "■":
                    empty_tile(int(guess_row) + 1, int(guess_col) - 0, field, answer_field)
                if field[int(guess_row) + 1][int(guess_col) + 1] == "■":
                    empty_tile(int(guess_row) + 1, int(guess_col) + 1, field, answer_field)

        elif int(guess_col) == 8 and int(guess_row) < 8:
            temp = 0
            if answer_field[int(guess_row) - 1][int(guess_col) - 1] == '*':  # top left
                temp = temp + 1
            if answer_field[int(guess_row) - 1][int(guess_col) - 0] == '*':  # top middle
                temp = temp + 1
            if answer_field[int(guess_row) - 0][int(guess_col) - 1] == '*':  # mid left
                temp = temp + 1
            if answer_field[int(guess_row) + 1][int(guess_col) - 1] == '*':  # bottom left
                temp = temp + 1
            if answer_field[int(guess_row) + 1][int(guess_col) - 0] == '*':  # bottom mid
                temp = temp + 1
            if temp > 0:
                field[int(guess_row)][int(guess_col)] = temp
            if temp == 0:
                if field[int(guess_row) - 1][int(guess_col) - 1] == "■":
                    empty_tile(int(guess_row) - 1, int(guess_col) - 1, field, answer_field)
                if field[int(guess_row) - 1][int(guess_col) - 0] == "■":
                    empty_tile(int(guess_row) - 1, int(guess_col) - 0, field, answer_field)
                if field[int(guess_row) - 0][int(guess_col) - 1] == "■":
                    empty_tile(int(guess_row) - 0, int(guess_col) - 1, field, answer_field)
                if field[int(guess_row) + 1][int(guess_col) - 1] == "■":
                    empty_tile(int(guess_row) + 1, int(guess_col) - 1, field, answer_field)
                if field[int(guess_row) + 1][int(guess_col) - 0] == "■":
                    empty_tile(int(guess_row) + 1, int(guess_col) - 0, field, answer_field)

        elif int(guess_col) < 8 and int(guess_row) == 8:
            temp = 0
            if answer_field[int(guess_row) - 1][int(guess_col) - 1] == '*':  # top left
                temp = temp + 1
            if answer_field[int(guess_row) - 1][int(guess_col) - 0] == '*':  # top middle
                temp = temp + 1
            if answer_field[int(guess_row) - 1][int(guess_col) + 1] == '*':  # top right
                temp = temp + 1
            if answer_field[int(guess_row) - 0][int(guess_col) - 1] == '*':  # mid left
                temp = temp + 1
            if answer_field[int(guess_row) - 0][int(guess_col) + 1] == '*':  # mid right
                temp = temp + 1
            if temp > 0:
                field[int(guess_row)][int(guess_col)] = temp
            if temp == 0:
                if field[int(guess_row) - 1][int(guess_col) - 1] == "■":
                    empty_tile(int(guess_row) - 1, int(guess_col) - 1, field, answer_field)
                if field[int(guess_row) - 1][int(guess_col) - 0] == "■":
                    empty_tile(int(guess_row) - 1, int(guess_col) - 0, field, answer_field)
                if field[int(guess_row) - 1][int(guess_col) + 1] == "■":
                    empty_tile(int(guess_row) - 1, int(guess_col) + 1, field, answer_field)
                if field[int(guess_row) - 0][int(guess_col) - 1] == "■":
                    empty_tile(int(guess_row) - 0, int(guess_col) - 1, field, answer_field)
                if field[int(guess_row) - 0][int(guess_col) + 1] == "■":
                    empty_tile(int(guess_row) - 0, int(guess_col) + 1, field, answer_field)


        # since we are not out of bounds find all adjacent tiles with bombs.

        else:
            temp = 0
            if answer_field[int(guess_row) - 1][int(guess_col) - 1] == '*':  # top left
                temp = temp + 1
            if answer_field[int(guess_row) - 1][int(guess_col) - 0] == '*':  # top middle
                temp = temp + 1
            if answer_field[int(guess_row) - 1][int(guess_col) + 1] == '*':  # top right
                temp = temp + 1
            if answer_field[int(guess_row) - 0][int(guess_col) - 1] == '*':  # mid left
                temp = temp + 1
            if answer_field[int(guess_row) - 0][int(guess_col) + 1] == '*':  # mid right
                temp = temp + 1
            if answer_field[int(guess_row) + 1][int(guess_col) - 1] == '*':  # bottom left
                temp = temp + 1
            if answer_field[int(guess_row) + 1][int(guess_col) - 0] == '*':  # bottom mid
                temp = temp + 1
            if answer_field[int(guess_row) + 1][int(guess_col) + 1] == '*':  # bottom right
                temp = temp + 1

            if temp > 0:
                field[int(guess_row)][int(guess_col)] = temp

            if temp == 0:
                if field[int(guess_row) - 1][int(guess_col) - 1] == "■":
                    empty_tile(int(guess_row) - 1, int(guess_col) - 1, field, answer_field)
                if field[int(guess_row) - 1][int(guess_col) - 0] == "■":
                    empty_tile(int(guess_row) - 1, int(guess_col) - 0, field, answer_field)
                if field[int(guess_row) - 1][int(guess_col) + 1] == "■":
                    empty_tile(int(guess_row) - 1, int(guess_col) + 1, field, answer_field)
                if field[int(guess_row) - 0][int(guess_col) - 1] == "■":
                    empty_tile(int(guess_row) - 0, int(guess_col) - 1, field, answer_field)
                if field[int(guess_row) - 0][int(guess_col) + 1] == "■":
                    empty_tile(int(guess_row) - 0, int(guess_col) + 1, field, answer_field)
                if field[int(guess_row) + 1][int(guess_col) - 1] == "■":
                    empty_tile(int(guess_row) + 1, int(guess_col) - 1, field, answer_field)
                if field[int(guess_row) + 1][int(guess_col) - 0] == "■":
                    empty_tile(int(guess_row) + 1, int(guess_col) - 0, field, answer_field)
                if field[int(guess_row) + 1][int(guess_col) + 1] == "■":
                    empty_tile(int(guess_row) + 1, int(guess_col) + 1, field, answer_field)


"""
clear is used only to clear the screen making readability better. clear is operating system specific, so needed to add
an if statement. No parameters are taken in and nothing is returned.
"""
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')





#create the covered map tiles
field = []
for i in range(0, 9):
    field.append([])
    for j in range(0, 9):
        field[i].append("■") # alt 254 = ■

#create the answer key (uncovered) hard coded.
answer_field = []
for i in range(0, 9):
    answer_field.append([])
    for j in range(0, 9):
        answer_field[i].append("_")

#BOMBS AWAY ! ! ! (Don't look here or it will ruin the fun)

#commented out non-random board. used for troubleshooting
#answer_field[0][0] = '*'
#answer_field[1][1] = '*'
#answer_field[6][3] = '*'
#answer_field[4][0] = '*'
#answer_field[4][8] = '*'
#answer_field[2][7] = '*'
#answer_field[8][2] = '*'
#answer_field[2][0] = '*'
#answer_field[8][8] = '*'
#answer_field[7][8] = '*'
#answer_field[7][7] = '*'

#random board generation
for i in range(0, random.randint(5,25)): #9x9 board randomly placed pieces at most 25 boombs and minimum 5 bombs
    answer_field[random.randint(0,8)][random.randint(0,8)] = '*'


#----------------show answer----------------------
# used for troubleshooting
#for i in range(0, 9):
#    print(i, " ", end='')
#    for j in range(0, 9):
#        print(answer_field[i][j] + ' ', end='')
#    print('')
#print("\n")



# main loop for mine-sweeper game.
while(True):
    clear()

    # check to see if the user won
    win = True
    for i in range(0, len(field)):
        for j in range(0, len(field[i])):
            if field[i][j] == "■" and answer_field[i][j] != '*':
                win = False
                break
        if win == False:
            break
    if win == True:
        clear()
        print("!!! ~YOU WIN~ !!!")
        print("    GREAT JOB")
        print("   0  1  2  3  4  5  6  7  8")
        for i in range(0, 9):
            print(i, " ", end='')
            for j in range(0, 9):
                if answer_field[i][j] == '*':
                    print('*', ' ', end="")
                else:
                    print(field[i][j], ' ', end='')
            print('')
        input("press return to exit")
        break  # end the game here

    #the user has not won yet, so print out the board to play/continue playing
    print("   0  1  2  3  4  5  6  7  8")
    for i in range(0, 9):
        print(i, " ", end ='')
        for j in range(0,9):
            print(field[i][j], ' ', end='')
        print('')

    #Get user inputs. Quit if thats what they want to do.
    guess_row = input("Select Row (0 - 8) or Q to quit")
    if guess_row == 'Q' or guess_row == 'q':
        print("user selected 'Q' to quit. Goodbye!")
        input("press return to exit")
        break #end game here
    guess_col = input("Select Column(0 - 8) or Q to quit")
    if guess_col == 'Q' or guess_col == 'q':
        print("user selected 'Q' to quit. Goodbye!")
        input("press return to exit")
        break #end game here

    #check to see if the input is valid
    if int(guess_col) > 8 or int(guess_col) < 0 or int(guess_row) > 8 or int(guess_col) < 0:
        print("Incorrect Column or Row selected, You have angered the MINDSWEEPER gods. Goodbye!")
        input("press return to exit")
        break

    # Was the bomb selected? Game Over
    if answer_field[int(guess_row)][int(guess_col)] == '*':
        clear()
        print("!!! ~OH NO, YOU BLEW UP~ !!!")
        print("All bombs have been revealed.")
        print("   0  1  2  3  4  5  6  7  8")
        for i in range(0, 9):
            print(i, " ", end='')
            for j in range(0, 9):
                if answer_field[i][j] == '*':
                    print('*', ' ', end="")
                else:
                    print(field[i][j], ' ', end='')
            print('')
        input("press return to exit")
        break  # end the game here

    else:
        # Check the answer field  at the location. If a bomb, blow up and end game. if not count the surrounding 8 squares and make the location n = total in squares > 0. 0 = blank.

        # Uncover the selected tile
        field[int(guess_row)][int(guess_col)] = answer_field[int(guess_row)][int(guess_col)]

        #need to get all adjacent tiles and sum them up. This has to be done recursively
        empty_tile(guess_row, guess_col, field, answer_field)
