Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [Rock, Paper, Scissors]
print ("Welcome to Rock, Paper, Scissors!")
print ("Choose Rock (0), Paper (1), or scissors (2)")
user_choice = int(input())
print(game_images[user_choice])
if user_choice == 0:
  print ("You chose Rock.")
elif user_choice == 1:
  print ("You chose Paper.")
elif user_choice == 2:
  print ("You chose Scissors.")
elif user_choice <= 0 or user_choice >=2:
  print ("Your choice is not valid. Try again.")
import random
computer_choice = random.randint(0, 2)
print(game_images[computer_choice])
if computer_choice == 0:
  print ("Computer chose Rock.")
elif computer_choice == 1:
  print ("Computer chose Paper.")
elif computer_choice == 2:
  print ("Computer chose Scissors.")
else:
  print ("Oops! Something went wrong. Please try again.")
if user_choice == 0 and computer_choice == 0:
  print ("It's a tie!")
elif user_choice == 0 and computer_choice == 1:
  print ("You lose!")
elif user_choice == 0 and computer_choice == 2:
  print ("You win!")
elif user_choice == 1 and computer_choice == 0:
  print ("You win!")
elif user_choice == 1 and computer_choice == 1:
  print ("It's a tie!")
elif user_choice == 1 and computer_choice == 2:
  print ("You lose!")
elif user_choice == 2 and computer_choice == 0:
  print ("You lose!")
elif user_choice == 2 and computer_choice == 1:
  print ("You win!")
elif user_choice == 2 and computer_choice == 2:
  print ("It's a tie!")
else:
  print ("Oops! Something went wrong. Please try again.")
         