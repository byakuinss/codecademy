"""
This is a dice game.
--- Grace
"""

from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input("Guess a number: "))
  return user_guess

def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides * 2
  print "The max possible value: " + str(max_val)
  sleep(1)
  user_guess = get_user_guess()
  if(user_guess > max_val):
    print "Your guess is over the max possible value."
    return
  else:
    print "Rolling..."
    sleep(2)
    print "The first roll: %d" % first_roll
    print "The second roll: %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "Result... %d" % total_roll
    sleep(1)
    if(user_guess > total_roll):
      print "You Win!"
      return
    else:
      print "You Lose!"
      return 

roll_dice(6)    
    
    