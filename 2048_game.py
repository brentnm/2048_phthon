# start writing code
# 1 set up board
# create merging functions
# set start of game
# set up rounds of the game
# adding new values for every move
# set up win and loss functions

board = [[0, 0, 2, 2], [2, 2, 2, 0], [4, 0, 0, 4], [0, 2, 0, 0]]

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
                currRow += (" " * (numSpaces - len(str(element))))str(element) + "|"
        # print generated row
        print(currRow)
    print()

display()

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
        