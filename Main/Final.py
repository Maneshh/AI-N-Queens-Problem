#Function to define the board
def get_board(Q):
    board = ['[-]']*Q
    for i in range(Q):
        board[i] = ['[-]']*Q
    return board

#Function to print out the board
def print_board():
    for i in range(Q):
        for j in range(Q):
            print(board[i][j], end = " ")
        print("")

#Function used to see if the queen is safe at a particular location in the board ( refering to row and columns )
def check(board,row,col): 
    
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

#Recursive Backtracking function to place the queens on the board
def insert(board, Q, count):
    if count == Q: # checks for example if a 5 x 5 board it has 5 queens it returns true 
        return True

    for row in range(Q):
        for col in range(Q):
            if check(board, row, col): # going thru every cell in the board and checks if the cell is safe 
                board[row][col] = '[Q]' # Placing the queen if the cell is safe
                count = count + 1 
                if insert(board, Q, count) == True: # calling the function recursively, now it takes in the new count 
                    return True
                board[row][col] = '[-]' # replace the Q with [-] and go back to check
                count = count-1 # and reduce the count again 
    return False

#Function to check users Input to match the conditions
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

if __name__ == '__main__':

    Q =  user_input()

    # Instructions to make the code clear 
    print()
    print('(-) represents the empty spot where the queen will be able to move and (Q) represents the queens on the board\n')
    print('This is the board for ' + str(Q) + ' number of queens\n')

    #Functions called to get the board
    board = get_board(Q)

    #Function to place all the queens on the baord
    insert(board, Q, 0) # count of queens is 0 at the start 

    #Function to print the board and its final solution
    print_board()
    print(' ')