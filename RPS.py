"""
This a python program for playing Rock, Paper and Scissor with the computer
"""
#importing files
from random import randint
from time import sleep


option = ["ROCK", "PAPER", "SCISSOR"] #defining the options
LOSS_MESSAGE = "You Lost! LOL"
WIN_MESSAGE = "You Won!"

def decide_winner (user_choice, comp_choice): #Function to decide winner
  print "You selected: %s" %user_choice
  print "Computer selecting..."
  sleep (1)
  print "Computer selected: %s" %comp_choice
  sleep (1)
  
  #Given an item that belongs to a list, the index() function will return the index of that item.
  user_choice_index = option.index(user_choice)
  comp_choice_index = option.index(comp_choice)
  
  #Conditions to decide the winner
  if user_choice_index == comp_choice_index:
    print "It's tie!"
  elif user_choice_index == 0 and comp_choice_index == 2:
    print WIN_MESSAGE
  elif user_choice_index == 1 and comp_choice_index == 0:
    print WIN_MESSAGE
  elif user_choice_index == 2 and comp_choice_index == 1:
    print WIN_MESSAGE
  elif user_choice_index > 2:
    print "Nope... Just Nope"
    return
  else:
    print LOSS_MESSAGE
def play_RPS():
  user_choice = raw_input ("Rock, Paper or Scissor? ")
  user_choice = user_choice.upper() #To convert all characters in the string to UPPER CASE
  sleep(1)
  comp_choice = option [randint (0, 2)]
  if (user_choice == "ROCK" or user_choice == "PAPER" or user_choice == "SCISSOR" or user_choice == "SCISSORS"): #To check weather the user has given the correct input
    decide_winner (user_choice, comp_choice) #Execute this function for correct input
  else:
    print ("Wrong Choice bruh!!") #Print this for wrong input

play_RPS()
    
