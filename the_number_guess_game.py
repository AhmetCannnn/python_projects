import random
from art import logo

#You can find a logo and use it at the beginning of your game.

print(logo)
print("Welcome the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy or hard':")

if difficulty == "easy" :
  attemps = 10
else:
  attemps = 5
  
print(f"You have {attemps} attemps to guess the remaining number.")

def get_guess(attemps):
  ansver = random.randint(1,100)
  
  guess = int(input("Make a guees: "))
  for attemps in range(attemps,1,-1):
    if guess > ansver:
      attemps = attemps - 1
      print(f"Too high.")
      print(f"You have {attemps} attemps remaining to guees the number.")
      guess = int(input("Guess again:"))
    elif guess < ansver:
      attemps = attemps -1
      print(f"Too less.")
      print(f"You have {attemps} attemps remaining to guees the number.")
      guess = int(input("Guess again:"))
    elif guess == ansver:
      print(f"You got it. Ansver was {ansver}")
      break
    else:
      print(f"You've run out of guesses,You lose.")
    
get_guess(attemps)
