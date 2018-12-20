"""In this project you will build a simplified, one-player version of the classic board game Battleship!
In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid.
The player will have 4 guesses to try to sink the ship."""

from random import randint

board = []

for x in range(5): 
  board.append(["O"] * 5) #creates a 4x4 list with zeroes

def print_board(board):
  for row in board:
    print (" ".join(row)) #Ads spaces inbetween each element

print_board(board)

#Functions to for the computer to guess the location of the ship
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

"""The below two print statements are to test the program for different inputs with computer's guess.
Also like a cheat code. Commented out on purpose"""
#print ship_row
#print ship_col

for turn in range(4): #The game runs 4 times
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col: #win Condition (When guesses the correct answer)
    print ("Congratulations! You sunk my battleship!")
    break #The program exists after this condition runs (ie. when the user wins)
  else:
    #To test whether the user input is within the range
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print ("Oops, that's not even in the ocean.")
    #To remind the user has already guessed these values
    elif(board[guess_row][guess_col] == "X"):
      print ("You guessed that one already.")
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    #To monitor the user to play 4 times. Not more than that
    if turn<3:
      print ("Turn", turn+1)
    else:
      print ("Game Over")
      
print_board(board)
