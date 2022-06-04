#Function to check users input to make sure it is valid
def user_input():
    while True:
        try:
            Q = int(input("Enter the number of Queens: "))
            if Q <= 3:
                print("Enter a value greater than or equal to 4")
                continue
            return Q
        except ValueError:
            print("Invalid value entered. Enter an Integer")

#Function to get a Q x Q board
def get_board(Q):
    board = ['[-]']*Q
    for i in range(Q):
        board[i] = ['[-]']*Q
    return board

# function used to see if the queen is safe at a particular location in the board ( refering to row and columns )
def check(board, row, col): 
    
    for i in range (row):
        if board[row][i] == '[Q]': # checks if there is a Queen in the corresponding row 
            return False

    for j in range(row):
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

# The backtracing function where it checks when to place the queen
def insert(board, row, Q):

    if row == Q: # Out of bounds, you have iterated through every row
        print_solution(board) # prints out the solution everytime a full board is reached
        copy = [row] # Array to keep track of all the solutions
        results.append(copy) # Appends to results to print out for the users
        return True

    for col in range(Q): # checks every column in the row
        if check(board, row, col): # checks if the cell has been used and is safe to place the queen
            board[row][col] = '[Q]' # if it hasnt been used, place the queen
            insert(board, row+1, Q) # backtracking for the next row
            board[row][col] = '[-]' # if the solution is not reached replace the Q with - 
    return False

#prints out solution for the problem
def print_solution(board):
    for row in board:
        print(str(row).replace(',', '').replace("'", '')) #makes the row looks cleaner 
    print()

if __name__ == '__main__':
    Q =  user_input()
    board = get_board(Q)
    results = []
    insert(board, 0, Q)
    print()
    print("For {0} Number of Queens there are a total of {1} Solutions".format(Q,len(results)) + "\n")