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


#Write your code below this line 👇
import random

choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
my_choice = random.randint(0, 2)

print(f"Your pick: \n{choices[user_choice]}")
print(f"Computer pick: \n{choices[my_choice]}")

if (user_choice == 0):
    if (my_choice == 0):
        print("It's a draw !")
    elif (my_choice == 1):
        print("You Lose !")
    else:
        print("You Win !")

elif (user_choice == 1):
    if (my_choice == 0):
        print("You Win !")
    elif (my_choice == 1):
        print("It's a draw !")
    else:
        print("You Lose !")

else:
    if (my_choice == 0):
        print("You Lose !")
    elif (my_choice == 1):
        print("You Win !")
    else:
        print("It's a draw !")