'''start writing code'''
# 1 set up board
# create merging functions
# set start of game
# set up rounds of the game
# adding new values for every move
# set up win and loss functions

import random
import copy

# create board size variable
BOARD_SIZE = 4

def display():
    '''print board function'''
    # find out which value is the largest
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element
    # set the max number of spaces needed to the length of the largest value
    num_spaces = len(str(largest))

    for row in board:
        curr_row = "|"
        for element in row:
            if element == 0:
                curr_row += " " * num_spaces + "|"
            else:
                curr_row += (" " * (num_spaces - len(str(element)))) + str(element) + "|"
        # print generated row
        print(curr_row)
    print()

def merge_one_row_l(row):
    '''merge one row left'''
    # move every element left
    for _ in range(BOARD_SIZE - 1):
        for i in range(BOARD_SIZE - 1, 0, -1):
        # test for empty space and if so move
            if row[i - 1] == 0:
                row[i - 1] = row[i]
                row[i] = 0
    for i in range(BOARD_SIZE - 1):
        # test if current value is identical to the one next to it
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i +1] = 0
    # move everything to the left again
    for i in range(BOARD_SIZE - 1, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] = row[i]
            row[i] = 0
    return row
def merge_left(current_board):
    '''merge the whole board left'''
    for i in range(BOARD_SIZE):
        current_board[i] = merge_one_row_l(current_board[i])
    return current_board

def reverse(row):
    '''reverse the order of one row'''
    # add all the elements of the row to a new list in reverse order
    new = []
    for i in range(BOARD_SIZE - 1, -1, -1):
        new.append(row[i])
    return new

def merge_right(current_board):
    '''merge the whole board right'''
    for i in range(BOARD_SIZE):
        # reverse the row, merge left, reverse back
        current_board[i] = reverse(current_board[i])
        current_board[i] = merge_one_row_l(current_board[i])
        current_board[i] = reverse(current_board[i])
    return current_board
def transpose(current_board):
    '''this function transposes the board'''
    for j in range(BOARD_SIZE):
        for i in range(j, BOARD_SIZE):
            if not i == j:
                temp = current_board[j][i]
                current_board[j][i] = current_board[i][j]
                current_board[i][j] = temp
    return current_board
def merge_up(current_board):
    '''merges the board up'''
    # transpose board, merge left, transpose back
    current_board = transpose(current_board)
    current_board = merge_left(current_board)
    current_board = transpose(current_board)

    return current_board

def merge_down(current_board):
    '''merge down'''
    current_board = transpose(current_board)
    current_board = merge_right(current_board)
    current_board = transpose(current_board)

    return current_board

def pick_new_value():
    '''pick either a two or four function'''
    if random.randint(1,8) == 1:
        return 4
    else:
        return 2

def add_new_value():
    '''add a new value function'''
    row_num = random.randint(0, BOARD_SIZE - 1)
    col_num = random.randint(0, BOARD_SIZE - 1)

    # pick spots until one found is empty
    while not board[row_num][col_num] == 0:
        row_num = random.randint(0, BOARD_SIZE - 1)
        col_num = random.randint(0, BOARD_SIZE - 1)

    # fill the empty space
    board[row_num][col_num] = pick_new_value()

def won():
    '''test if win'''
    for row in board:
        if 2048 in row:
            return True
    return False

def no_moves():
    '''test if loss'''
    tempboard1 = copy.deepcopy(board)
    tempboard2 = copy.deepcopy(board)
    # test in every possible direction
    tempboard1 = merge_down(tempboard1)
    if tempboard1 == tempboard2:
        tempboard1 = merge_up(tempboard1)
        if tempboard1 == tempboard2:
            tempboard1 = merge_left(tempboard1)
            if tempboard1 == tempboard2:
                tempboard1 = merge_right(tempboard1)
                if tempboard1 == tempboard2:
                    return True
    return False

# create an empty board
board = []
for i in range(BOARD_SIZE):
    row = []
    for j in range(BOARD_SIZE):
        row.append(0)
    board.append(row)

# fill two slots to start the game
NUM_NEEDED = 2
while NUM_NEEDED > 0:
    row_num = random.randint(0, BOARD_SIZE - 1)
    col_num = random.randint(0, BOARD_SIZE - 1)

    if board[row_num][col_num] == 0:
        board[row_num][col_num] = pick_new_value()
        NUM_NEEDED -= 1

print("Welcome to 2048! The goal of this game is to combine numbers to get to 2048, "\
      "by merging the board in different directions. To merge, press 'd' to merge right, "\
      "'a' to merge left, 'w' to merge up, and 's' to merge down. \n\nHere is the starting board:")

display()

GAME_OVER = False

# ask the user for new moves
while not GAME_OVER:
    move = input("which way do you want to merge? ")

    # assume they enter a valid input
    VALID_INPUT = True

    # create a copy of the board
    tempBoard = copy.deepcopy(board)

    if move == "d":
        board = merge_right(board)
    elif move == "w":
        board = merge_up(board)
    elif move == "a":
        board = merge_left(board)
    elif move == "s":
        board = merge_down(board)
    else:
        VALID_INPUT = False
    if not VALID_INPUT:
        print("Your input was not valid, please try again")
    else:
        # test if move was unsuccessful
        if board == tempBoard:
            print("Try a differnt direction")
        else:
            if won():
                display()
                print("You Won!")
                GAME_OVER = True
            else:
                add_new_value()

                display()

                if no_moves():
                    print("Sorry, no more possible moves, you lose!")
                    GAME_OVER = True
