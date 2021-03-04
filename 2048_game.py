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
                currRow += (" " * (numSpaces - len(str(element)))) + str(element) + "|"
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


merge_up(board)
display()
