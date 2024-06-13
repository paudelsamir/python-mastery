import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice = ["R", "P", "S"]

user_choice = input("R for Rock, P for Paper and S for Scissors: \n").upper()
print(f"You chose:")
if user_choice == "R":
    print(rock)
elif user_choice == "P":
    print(paper)
elif user_choice == "S":
    print(scissors)
else:
    print("Invalid choice! ")


random_choice = random.choice(choice)
print(f"Opponent chose:")
if random_choice == "R":
    print(rock)
elif random_choice == "P":
    print(paper)
elif random_choice == "S":
    print(scissors)

if user_choice == random_choice:
    print("Draw. Try again!")
elif (user_choice == "R" and random_choice == "S") or \
     (user_choice == "P" and random_choice == "R") or \
     (user_choice == "S" and random_choice == "P"):
    print("You won!")
else:
    print("Opponent won!")
