from random import randrange

def display_board(board):
    print("+-------" * 3, "+", sep="") # Prints top row
    for row in range(3):
        print("|       " * 3,"|", sep="") # Prints cols
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="") # Prints contents of 2D array
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")

def enter_move(board):
    ok = False # Fake assumption - we need it to enter the loop
    while not ok: # While True
        move = input("Enter your move: ")
        ok = len(move) == 1 and move >= '1' and move <= '9' # Is user's input valid?
        if not ok: 
            print("Bad move - repeat your input!") # No, it isn't - do the input again
            continue
        move = int(move) - 1 # Cell's number from 0 to 8
        row  = move // 3 # Cell's row
        col = move % 3 # Cell's column
        sign = board[row][col] # Check the selected square
        ok = sign not in ['O', 'X']
        if not ok: # It's occupied - to the input again
            print("Field is already occupied - repeat your input")
            continue
        board[row][col] = 'O' # Set '0' at the selected square

def make_list_of_free_fields(board):
    free = []
    for row in range(3): # Iterate through rows
        for col in range(3): # Iterate through columns
            if board[row][col] not in ['O', 'X']: # Is the cell free?
                free.append((row,col)) # Yes, it is - append new tuple to the list
    return free

def victory_for(board, sgn):
    if sgn == 'X': # Are we looking for X?
        who = 'me' # Yes - it's computer's side
    elif sgn == 'O': # ... or for O?
        who = 'you' # Yes - it's our side
    else:
        who = None # We should not fall here!
    cross1 = cross2 = True  # For diagonals
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn: # Checks row rc
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # Checks col rc
            return who
        if board[rc][rc] != sgn: # Check cross1 diagonal
            cross1 = False
        if board[2- rc][2 - rc] != sgn: # Check cross2 diagonal
            cross2 = False
    if cross1 or cross2:
        return who
    return None

def draw_move(board):
    free = make_list_of_free_fields(board) # Make a list of free fields
    cnt = len(free)
    if cnt > 0: # If free fields exist
         this = randrange(cnt) # Select a random free field
         row, col = free[this]
         board[row][col] = 'X' # Set 'X' at the selected square

board = [[3 * i + j + 1 for i in range(3)] for j in range(3)] # Create board
board[1][1] = 'X'  # Set first 'X' in the middle
free = make_list_of_free_fields(board) # Create free fields board
human_turn = True # Which turn is it now?
while len(free): # While free fields exist
    display_board(board)
    if human_turn:
        enter_move(board) # Human move
        victor = victory_for(board, 'O')
    else:
        draw_move(board) # Computer move
        victor = victory_for(board, 'X')
    if victor != None:
        break
    human_turn = not human_turn # Change turn
    free = make_list_of_free_fields(board) # Update free fields board

display_board(board) # Display final board
if victor == 'you': # If human victory
	print("You won!")
elif victor == 'me': # If computer victory
	print("I won")
else: # Tie
	print("Tie!")



