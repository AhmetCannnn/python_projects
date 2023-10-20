# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:36:04 2023

@author: AHMET CAN
"""

import random
from gamedata import data
from art import vs
from art import logo
import os

score = 0
ansver = "A"
print(logo)
first_famous = random.choice(data)
second_famous = random.choice(data)
print(f"Compare A: {first_famous['name']},{first_famous['description']},{first_famous['country']}.")
print(vs)
print(f"Compare A: {second_famous['name']}, {second_famous['description']}, {second_famous['country']}.")
users_ansver = input("Whos has more followers? Type 'A' or 'B': ")


while_value = True
while while_value:
  if first_famous['follower_count'] > second_famous['follower_count']:
     ansver = "A"
  else:
     ansver = "B"
  if (ansver == "A" and users_ansver == "A") or (ansver == "B" and users_ansver == "B"):
      os.system('clear')
      score += 1
      first_famous = second_famous
      second_famous = random.choice(data)
      print(logo)
      print(f"You are right! Current score: {score}")
      print(f"Compare A: {first_famous['name']}, {first_famous['description']}, {first_famous['country']}")
      print(vs)
      print(f"Compare A: {second_famous['name']}, {second_famous['description']}, {second_famous['country']}.")
      users_ansver = input("Whos has more followers? Type 'A' or 'B': ")
  elif (ansver == "A" and users_ansver == "B") or (ansver == "B" and users_ansver == "A"):
    print(logo)
    print(f"Sorry. that's wrong. Final score: {score}")
    while_value = False
     
    
   
   
   
     

    










  

  

