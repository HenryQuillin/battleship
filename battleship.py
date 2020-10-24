'''
Henry Quillin
10/16/2020
Battleship
'''
import random


def intro():
    print('Welcome to Battleship')


board = [
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
]
comp_board = [
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
]



def draw_comp_board():
    '''for i in range(5):
        for j in range(5):
            comp_board[i][j] = '~'''''

    for i in range(5):
        print(comp_board[i])


def drawboard():
    for i in range(5):
        for j in range(5):
            board[i][j] = '~'

    for i in range(5):
        print(board[i])

    print(f'''
        0 1 2
       _______
    0 | {board[0][0]}|{board[0][1]}|{board[0][2]} |
      | -+-+- | 
    1 | {board[1][0]}|{board[1][1]}|{board[1][2]} |
      | -+-+- |                                    
    2 | {board[2][0]}|{board[2][1]}|{board[2][2]} | 
       -------
    ''')


def comp_place_ships():

    i = 0
    while i < 5:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if comp_board[row][col] != 'X':
            comp_board[row][col] = 'X'
            i = i + 1
            print(i)
            print(row, col)
        draw_comp_board()





comp_place_ships()


'''
# In the first version of my battleship game, the board will be a 5 x 5 board with letters on the x - axis and numbers on the y axis
# Battleships will only take up one space
# You will play against the computer

def welcome_msg():
    # Print out the welcome message

def drawboard():
    # Draw the 5x5 board with numbers on the y and letters on the x
    # Board will be a 2d array with empty strings

def letter_to_num():
	# Uses a dictionary to convert the str input to an int

def place_ships():
	# Ask the user to enter the location of 5 battleships

def computer_place_ships():
	# Randomly places the computer's ships on the board

def user_turn():
	# Asks the user to enter a location to guess
	# Checks if that location is on the computer's ship
		# If true: add an X to that location on the board
		# If false: add a + to that location on the board

def comp_turn():
    # Will randomly make the computer's guess
	# Checks if that location is on the user's ship
		# If true: add an X to that location on the board
		# If false: add a + to that location on the board
	# Cannot make the same guess twice

def win_check():
	# Checks if a win condition is true
	# if yes, win_condition = True

def end_game():
	# Asks the user if they want to play again

def gameplay():
	# Will loop through user_turn() and comp_turn()
	# Check if win_condition = True
		# If True: run endgame()
'''
