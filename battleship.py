'''
Henry Quillin
10/16/2020
Battleship
'''
import random
import time
from colored import fg, bg, attr
def intro():
    print(r'''
                   Welcome to Battleship
                   --------------------
                   
                                  )___(
                           _______/__/_
                  ___     /===========|   ___
 ____       __   [\\\]___/____________|__[///]   __
 \   \_____[\\]__/___________________________\__[//]___
  \40A                                                 |
   \                                                  /
%s~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~%s
'~' = unknown location 
'O' = your battleship 
'V' = missed shot 
'X' = sunken ship 
''' % (fg(4), attr(0)))


board = [
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    'Friendly Waters'
]
battlefield = [
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    'Enemy Waters'
]
comp_board = [
    ["O", " ", " ", " ", "~"],
    ["~", "~", "~", "~", "~"],
    [" ", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    'Enemy Waters'
]
letter2num = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
}

comp_ships_left = 5
user_ships_left = 5


def drawboard(board):
    if board == battlefield:
        location = 'Enemy Waters'
    else:
        location = 'Friendly Waters'
    
    print(f'''
     {board[5]}
           --
     %s   A B C D E 
       ___________
    0 | {board[0][letter2num['A']]} {board[0][letter2num['B']]} {board[0][letter2num['C']]} {board[0][letter2num['D']]} {board[0][letter2num['E']]} |                                  
    1 | {board[1][letter2num['A']]} {board[1][letter2num['B']]} {board[1][letter2num['C']]} {board[1][letter2num['D']]} {board[1][letter2num['E']]} |
    2 | {board[2][letter2num['A']]} {board[2][letter2num['B']]} {board[2][letter2num['C']]} {board[2][letter2num['D']]} {board[2][letter2num['E']]} |                                
    3 | {board[3][letter2num['A']]} {board[3][letter2num['B']]} {board[3][letter2num['C']]} {board[3][letter2num['D']]} {board[3][letter2num['E']]} |
    4 | {board[4][letter2num['A']]} {board[4][letter2num['B']]} {board[4][letter2num['C']]} {board[4][letter2num['D']]} {board[4][letter2num['E']]} |
       -----------
    %s''' % (fg(4), attr(0)))
    

def user_place_ships():
    global board
    print('Commander, where should we send our battleships?')
    drawboard(board)
    for ship in range(5):
        user_ships_input = input(f'Please enter the location of ship number {ship + 1} (example:A3) -> ')
        user_ship_letter = user_ships_input[0]
        user_ship_num = int(user_ships_input[1])
        board[user_ship_num][letter2num[user_ship_letter]] = 'O'
        drawboard(board)


def comp_place_ships():
    global comp_board
    i = 0
    while i < 5:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if comp_board[row][col] != 'O':
            comp_board[row][col] = 'O'
            i = i + 1


def user_turn():
    global comp_ships_left
    global battlefield
    print('Commander where should we fire? ')
    drawboard(battlefield)
    user_guess = input('(example:B3) -> ')
    user_guess_letter = (letter2num[user_guess[0]])
    user_guess_num = int(user_guess[1])
    if battlefield[user_guess_num][user_guess_letter] == 'X' or battlefield[user_guess_num][user_guess_letter] == 'v':
        print(f"We have already fired in that location!")
        user_turn()
    elif comp_board[user_guess_num][user_guess_letter] == 'O':
        comp_ships_left -= 1
        print(f"That's a hit! We have sunk one of the enemy ships! There are {comp_ships_left} left")
        battlefield[user_guess_num][user_guess_letter] = 'X'
        drawboard(battlefield)

    else:
        print("That's a miss")
        battlefield[user_guess_num][user_guess_letter] = 'v'
        drawboard(battlefield)



def comp_turn():
    row = random.randint(0, 4)
    col = random.randint(0, 4)
    if board[row][col] == 'O':
        board[row][col] = 'X'
        print('The enemy has sunk one of our battleships!')
        drawboard(board)
    elif board[row][col] == 'v' or board[row][col] == 'X':
        comp_turn()
    else:
        board[row][col] = 'v'
        print('The enemy has missed our battleship')
        drawboard(board)


def wincheck():
    if user_ships_left <= 0:
        print('The enemy has sunk all our battleships!')
        return False
        exit()
    elif comp_ships_left <= 0:
        print('Congratulations commander. We have sunk all enemy battleships!')
        exit()

def gameplay():
    intro()
    user_place_ships()
    print('Enemy ships have entered the AO!')
    comp_place_ships()
    print('''
    _      _      _      _      _      _      _      _
    )`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_
    
    ''')
    while wincheck is not False:
        user_turn()
        print('The enemy is making their move...')
        time.sleep(3.5)
        comp_turn()
        time.sleep(2)
        wincheck()


# comp_place_ships()
# user_turn()
gameplay()

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
