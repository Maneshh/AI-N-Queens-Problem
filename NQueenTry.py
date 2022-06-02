def printBoard(): # used to print the board to display the solution 
    for i in range(Q):
        for j in range(Q):
            print(board[i][j], end = " ")
        print("")

def check(row,col): # function used to see if the queen is safe at a particular location in the board ( refering to row and columns )
    
    for i in range (Q):
        if board[row][i] == '[Q]': # checks if there is a Queen in the corresponding row 
            return False

    for j in range(Q):
        if board[j][col] == '[Q]': # checks if there is Queen in the corresponding columns 
            return False # and it returns false if there is a queen

    #Checks for the diagonal directions 
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
    while(i>=0 and j<Q):
        if board[i][j] == '[Q]':
            return False
        i = i-1
        j = j+1

    #Checks the SW Direction
    i = row+1
    j = col-1
    while(i<Q and j>=0):
        if board[i][j] == '[Q]':
            return False
        i = i+1
        j = j-1

    #Checks the SE Direction
    i = row+1
    j = col+1
    while(i<Q and j<Q):
        if board[i][j] == '[Q]':
            return False
        i = i+1
        j = j+1

    return True #if all the conditions are safe it returns true   

def Insert(board, row):
    if row == len(board): # checks for example if a 5 x 5 board it has 5 queens it returns true 
        printSolution(board)
        return

    for col in range(len(board)):
        if check (row, col):
            board[row][col] = '[Q]' # Placing the queen if the cell is safe 
            Insert(board, row + 1)
            board[row][col] = '[-]'

def Userinput():
    #Accepts the size of the chess board
    while True:
        try:
            Q = int(input("Enter the number of Queens: "))
            if Q <= 3:
                print("Enter a value greater than or equal to 4, as there is no valid answer for Queens lesser than 4")
                continue
            return Q
        except ValueError:
            print("Invalid value entered. Enter an Integer")

def printSolution(board):
    for row in board:
        print(row)
    print()


def get_board(Q):
    board = ['[-]']*Q
    for i in range(Q):
        board[i] = ['[-]']*Q
    return board

        
if __name__ == '__main__':

    Q =  Userinput()
    board = get_board(Q)
    Insert(board, 0)