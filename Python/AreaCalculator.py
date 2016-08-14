"""
It's a calculator
"""
from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
print "The calculator is starting up ..."

print "%s/%s/%s %s:%s" % (datetime.month,datetime.day,datetime.year,datetime.hour,datetime.minute)

sleep(1)

hint = "Don\'t forget to include the corrent units! \nExiting..."

option = raw_input("Enter C for Circle or T for Triangle:")
option = option.upper()

if(option == 'C'):
  radius = float(raw_input("Enter radius: "))
  area = pi * (radius ** 2)
  print "The pie is baking..."
  sleep(1)
  print "%.2f" % area
elif(option == 'T'):
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height:"))
  area = base * height / 2
  print "Uni Bi Tri..."
  sleep(1)
  print "%.2f" % area
else:  
  print "WTF"