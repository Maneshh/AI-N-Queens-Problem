N = int(input("Enter the number of Queens: "))
board = []


def getBoard():
    for i in range(N):
        emptyLists = []
        for j in range(N):
            emptyLists.append('[-]')
        board.append(emptyLists)

def printBoard():
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print("")


def isSafe(row,col):
    for i in range (N):
        if board[row][i] == '[Q]':
            return False
    for j in range(N):
        if board[j][col] == '[Q]':
            return False

    #Checks the NW Direction
    i = row-1
    j = col-1
    while(i>=0 and j>=0):
        if board[i][j] == '[Q]':
            return False
        i = i-1
        j = j-1

    #Checks the NE Direction
    i = row-1
    j = col+1
    while(i>=0 and j<N):
        if board[i][j] == '[Q]':
            return False
        i = i-1
        j = j+1

    #Checks the SW Direction
    i = row+1
    j = col-1
    while(i<N and j>=0):
        if board[i][j] == '[Q]':
            return False
        i = i+1
        j = j-1

    #Checks the SE Direction
    i = row+1
    j = col+1
    while(i<N and j<N):
        if board[i][j] == '[Q]':
            return False
        i = i+1
        j = j+1
    return True    

# count - used to keep the count of number of queens in the board
# check every cell is safe using the isSafe Function
def Put(N, count):
    if count == N:
        return True
    for i in range(N):
        for j in range(N):
            if isSafe(i, j):
                board[i][j] = '[Q]' # Placing the queen
                count = count+1
                if Put(N, count) == True:
                    return True
                board[i][j] = '[-]'
                count = count-1
    return False

print('(-) represents the empty spot where the queen will be able to move and (Q) represents the queens on the board\n')
print('This is the board for ' + str(N) + ' number of queens\n')

getBoard()
Put(N, 0)
printBoard()

print(' ')