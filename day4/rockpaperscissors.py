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
possibilities = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(possibilities[user_choice])

print("Computer choose:")
computer_choice = random.randint(0,2)
print(possibilities[computer_choice])

if user_choice != computer_choice:
    if computer_choice == 2 and user_choice == 0:
        print("You Win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You Lose!")
    else:
        if user_choice < computer_choice:
            print("You Lose!")
        else:
            print("You Win!")
else:
    print("Empate")