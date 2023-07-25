import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if user_chose >= 3 or user_chose < 0:
  print("You typed invalıd number. You lose!")
else:
  print(game_images[user_chose])

computer_chose = random.randint(0, 2)


print("Computer chose:")
print(game_images[computer_chose])

if user_chose == 0 and computer_chose == 1:
  print("You lose!")
elif user_chose == 0 and computer_chose == 2:
  print("Wou win!")
elif user_chose == 1 and computer_chose == 0:
  print("Wou win!")
elif user_chose == 1 and computer_chose == 2:
  print("You lose!")
elif user_chose == 2 and computer_chose == 0:
  print("You lose!")
elif user_chose == 2 and computer_chose == 1:
  print("Wou win!")
elif user_chose == computer_chose:
  print("It's a draw")
