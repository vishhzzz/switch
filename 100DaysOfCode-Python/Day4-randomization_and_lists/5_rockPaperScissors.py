import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input())
if user_choice < 0 or user_choice > 2:
    print("Invalid input. Please enter 0, 1, or 2.")
    exit()

computer_choice = random.randint(0, 2)

# multi line string for rules of the game
print('''Rules of the game:
    Rock beats Scissors
    Scissors beats Paper
    Paper beats Rock \n''')

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]
# either or 3 is correct.
print(f"You choose: {user_choice} {options[user_choice]}")
# print(f"You choose: {user_choice} + rock")

# if user_choice == 0:
#     print(rock)
# elif user_choice == 1:
#     print(paper)
# else:
#     print(scissors)

# print(f"Computer choose: {computer_choice} {options[computer_choice]}")
print(f"Computer choose: {computer_choice}" + options[computer_choice])

# if computer_choice == 0:
#     print(rock)
# elif computer_choice == 1:
#     print(paper)
# else:
#     print(scissors)

if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")