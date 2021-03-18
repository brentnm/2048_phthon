# start writing code
# 1 set up board
# create merging functions
# set start of game
# set up rounds of the game
# adding new values for every move
# set up win and loss functions

import random
import copy

# create board size variable
boardSize = 4

# print board function
def display():
    # find out which value is the largest
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element
    
    # set the max number of spaces needed to the length of the largest value
    numSpaces = len(str(largest))

    for row in board:
        currRow = "|"
        for element in row:
            if element == 0:
                currRow += " " * numSpaces + "|"
            else: 
                currRow += (" " * (numSpaces - len(str(element)))) + str(element) + "|"
        # print generated row
        print(currRow)
    print()

# merge one row left
def mergeOneRowL(row):
    # move every element left
    for j in range(boardSize - 1):
        for i in range(boardSize - 1, 0, -1):
        # test for empty space and if so move
            if row[i - 1] == 0:
                row[i - 1] = row[i]
                row[i] = 0
    for i in range(boardSize - 1):
        # test if current value is identical to the one next to it
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i +1] = 0
    # move everything to the left again
    for i in range(boardSize - 1, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] = row[i]
            row[i] = 0
    return row
# merge the whole board left
def merge_left(currentBoard):
    for i in range(boardSize):
        currentBoard[i] = mergeOneRowL(currentBoard[i])
    
    return currentBoard

# reverse the order of one row
def reverse(row):
    # add all the elements of the row to a new list in reverse order
    new = []
    for i in range(boardSize - 1, -1, -1):
        new.append(row[i])
    return new 

# merge the whole board right
def merge_right(currentBoard):
    for i in range(boardSize):
        # reverse the row, merge left, reverse back
        currentBoard[i] = reverse(currentBoard[i])
        currentBoard[i] = mergeOneRowL(currentBoard[i])
        currentBoard[i] = reverse(currentBoard[i])
    return currentBoard

# this function transposes the board 
def transpose(currentBoard):
    for j in range(boardSize):
        for i in range(j, boardSize):
            if not i == j:
                temp = currentBoard[j][i]
                currentBoard[j][i] = currentBoard[i][j]
                currentBoard[i][j] = temp
    return currentBoard

# merges the board up
def merge_up(currentBoard):
    # transpose board, merge left, transpose back
    currentBoard = transpose(currentBoard)
    currentBoard = merge_left(currentBoard)
    currentBoard = transpose(currentBoard)

    return currentBoard

# merge down
def merge_down(currentBoard):
    currentBoard = transpose(currentBoard)
    currentBoard = merge_right(currentBoard)
    currentBoard = transpose(currentBoard)

    return currentBoard

# pick either a two or four function
def pickNewValue():
    if random.randint(1,8) == 1:
        return 4
    else:
        return 2

# add a new value function
def addNewValue():
    rowNum = random.randint(0, boardSize - 1)
    colNum = random.randint(0, boardSize - 1)

    # pick spots until one found is empty
    while not board[rowNum][colNum] == 0:
        rowNum = random.randint(0, boardSize - 1)
        colNum = random.randint(0, boardSize - 1)

    # fill the empty space
    board[rowNum][colNum] = pickNewValue()

# test if win
def won():
    for row in board:
        if 2048 in row:
            return True
    return False

# test if loss
def noMoves():
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
for i in range(boardSize):
    row = []
    for j in range(boardSize):
        row.append(0)
    board.append(row)

# fill two slots to start the game
numNeeded = 2
while numNeeded > 0:
    rowNum = random.randint(0, boardSize - 1)
    colNum = random.randint(0, boardSize - 1)

    if board[rowNum][colNum] == 0:
        board[rowNum][colNum] = pickNewValue()
        numNeeded -= 1

print("Welcome to 2048! The goal of this game is to combine numbers to get to 2048, by merging the board in different directions. To merge, press 'd' to merge right, 'a' to merge left, 'w' to merge up, and 's' to merge down. \n\nHere is the starting board:")

display()

gameOver = False

# ask the user for new moves
while not gameOver:
    move = input("which way do you want to merge? ")

    # assume they enter a valid input
    validInput = True

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
        validInput = False
    
    if not validInput:
        print("Your input was not valid, please try again")
    else:
        # test if move was unsuccessful 
        if board == tempBoard:
            print("Try a differnt direction")
        else:
            if won():
                display()
                print("You Won!")
                gameOver = True
            else:
            addNewValue()

            display()

            if noMoves():
                print("Sorry, no more possible moves, you lose!")
                gameOver = True