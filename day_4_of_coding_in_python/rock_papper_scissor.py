import random

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

game_image = [rock, paper, scissors]

player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer = random.randint(0, 2)
computer = int(computer)

print("computer answer: ")
print(game_image[computer])

if player_input == computer:
    print("It is a draw")
elif player_input == 1 and computer == 0:
    print(f"You win! {paper}")
elif player_input == 0 and computer == 2:
    print(f"You win! {rock}")
elif player_input == 2 and computer == 1:
    print(f"You win! {scissors}")
else:
    print("You lose!")
