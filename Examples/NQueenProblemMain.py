def get_board(Q):
    board = ['[-]']*Q
    for i in range(Q):
        board[i] = ['[-]']*Q
    return board

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

# count - used to keep the count of number of queens in the board

def Insert(Q, count):
    if count == Q: # checks for example if a 5 x 5 board it has 5 queens it returns true 
        return True

    for i in range(Q):
        for j in range(Q):
            if check(i, j): # going thru every cell in the board and checks if the cell is safe 
                board[i][j] = '[Q]' # Placing the queen if the cell is safe 
                count = count + 1 # keeps track of number of queens in the board
                if Insert(Q, count) == True: # calling the function recursively, now it takes in the new count 
                    return True
                board[i][j] = '[-]' # if the position the queen is placed did not give the correct solution, set the cell back to its original form (BackTracking)
                count = count-1 # and reduce the count again 
    return False

def user_input():
    #Accepts the size of the chess board
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
    print('(-) represents the empty spot where the queen will be able to move and (Q) represents the queens on the board\n')
    print('This is the board for ' + str(Q) + ' number of queens\n')
    #Functions called to get the board
    board = get_board(Q)
    #Function to 
    Insert(Q, 0) # count of queens is 0 at the start 
    #Function to print the board 
    printBoard()
    print(' ')