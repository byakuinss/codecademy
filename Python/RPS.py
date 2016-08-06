"""
Rock-Paper-Scissors
"""

from random import randint
from time import sleep

options = ["R","P","S"]
lost_msg = "You lost!"
win_msg = "You win!"

def decide_winner(user_choice, computer_choice):
  print "You select: %s" % user_choice
  print "Computer selecting..."
  sleep(1)
  print "Computer select: %s" % computer_choice
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if(user_choice_index == computer_choice_index):
    print "It's a tie!"
  elif(user_choice_index == 0 and computer_choice_index == 2):
    print win_msg
  elif(user_choice_index == 1 and computer_choice_index == 0):
    print win_msg
  elif(user_choice_index == 2 and computer_choice_index == 1):
    print win_msg
  else:
    print lost_msg
    
    
def play_RPS():
  print "Welcome to RPS game"
  user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ")
  sleep(1)
  user_choice = user_choice.upper()
  computer_choice = options[randint(0,len(options)-1)]
  
  if(user_choice not in options):
    print "It's an invalid option"
  else:
    decide_winner(user_choice, computer_choice)

play_RPS()
