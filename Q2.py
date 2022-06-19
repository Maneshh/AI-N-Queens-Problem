# -*- coding: utf-8 -*-
"""
@author: manesh
"""

# Creates board of size Q x Q
def get_board(Q):
    board = ['[-]']*Q
    for i in range(Q):
        board[i] = ['[-]']*Q
    return board

def print_board():
    for i in range(Q):
        for j in range(Q):
            print(board[i][j], end = " ")
        print("")

# Check if Queen is safe at a particular cell in the board (not under threat)
def check(board,row,col): 
    
    for i in range (Q):
        if board[row][i] == '[Q]': # check if there is a Queen in the corresponding row 
            return False

    for j in range(Q):
        if board[j][col] == '[Q]': # check if there is Queen in the corresponding columns 
            return False # return false if there is a queen

    # Check for diagonal directions 
    # Check the NW Direction 
    i = row-1
    j = col-1
    while(i>=0 and j>=0):
        if board[i][j] == '[Q]':
            return False
        i = i-1
        j = j-1

    # Check the NE Direction
    i = row-1
    j = col+1
    while(i>=0 and j<Q):
        if board[i][j] == '[Q]':
            return False
        i = i-1
        j = j+1

    # Check the SW Direction
    i = row+1
    j = col-1
    while(i<Q and j>=0):
        if board[i][j] == '[Q]':
            return False
        i = i+1
        j = j-1

    # Check the SE Direction
    i = row+1
    j = col+1
    while(i<Q and j<Q):
        if board[i][j] == '[Q]':
            return False
        i = i+1
        j = j+1

    return True # if Queen is safe, return true   

# Recursive Backtracking function to place the Queens on the board
def insert(board, Q, count):
    if count == Q: # Check if all Queens are placed
        return True

    for row in range(Q):
        for col in range(Q):
            if check(board, row, col): # Check if cell is safe for Queen
                board[row][col] = '[Q]' # Placing the queen 
                count = count + 1 
                if insert(board, Q, count) == True: # Calling function recursively 
                    return True
                board[row][col] = '[-]' # replace the Q with [-] if no solution found (backtrack)
                count = count-1 # Reduce count of Queen placed 
    return False

# Check user input to match conditions
def user_input():
    while True:
        try:
            Q = int(input("Enter the number of Queens (minimum 4): "))
            if Q <= 3:
                print("Enter a value greater than or equal to 4")
                continue
            return Q
        except ValueError:
            print("Invalid value entered. Enter an Integer")

if __name__ == '__main__':
    Q =  user_input()

    print('\n(-) represents the empty cells on the board')
    print('(Q) represents the Queens\n')
    print('Solution for ' + str(Q) + ' Queens on a ' + str(Q) + 'x' + str(Q) + ' board:\n')


    board = get_board(Q)
    insert(board, Q, 0) # count of queens is 0 at the start 
    print_board()
    print()