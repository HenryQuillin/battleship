'''
Henry Quillin
10/16/2020
Battleship
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
