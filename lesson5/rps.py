import sys
import random
from enum import Enum

# Enumeration means assigning a fixed value to each item in a list to easily identify them. 
# In Python, you use the Enum class from the enum module to do this. 
# These items are usually written in uppercase letters.

class RPS(Enum):
  ROCK = 1
  PAPER = 2
  SCISSORS = 3


print('')

player_choice = input("Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors: \n\n")

player = int(player_choice)

if player < 1 or player > 3:
  sys.exit("You must enter 1, 2, or 3.")


computer_choice = random.choice("123")
computer = int(computer_choice)

print("")

print("You chose " + str(RPS(player)).replace('RPS', "") + ".")
print("Python chose " + str(RPS(computer)).replace('RPS', "") + ".")
print("")

if player == 1 and computer == 3:
  print("🎊 You win!")
elif player == 2 and computer == 1:
  print("🎊 You win!")
elif player == 3 and computer == 2:
  print("🎊 You win!")
elif player == computer:
  print("🫣 Tie game!")
else: 
  print("🐍 Python win!")