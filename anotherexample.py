import copy

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

def get_board(Q):
    #Returns an n by n board
    board = ['[-]']*Q
    for i in range(Q):
        board[i] = ['[-]']*Q
    return board

def check(board, row, col, Q): # function used to see if the queen is safe at a particular location in the board ( refering to row and columns )
    
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

def insert(board, row, Q):

    if row == Q:
        return True

    for i in range(Q):
        if check(board, i, row, Q):
            board[i][row] = '[Q]'
            if row == Q-1:
                add_solution(board)
                board[i][row] = '[-]'
                return True
            insert(board, row+1, Q)
            board[i][row] = '[-]'


def add_solution(board):
    global solutions
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)


def print_solution(solutions, Q):
    for row in solutions:
        print((row))
    print()


if __name__ == '__main__':
    Q =  Userinput()
    board = get_board(Q)
    solutions = []
    insert(board, 0, Q)
    print_solution(solutions, Q)

    print()
    print("Total number of solutions=", len(solutions))