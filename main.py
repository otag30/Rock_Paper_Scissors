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
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_choice = random.choice([0, 1, 2])
if player_choice == "0":
    print(rock)
    if computer_choice == 0:
        print(f"Computer chose: \n{rock} \n It's a draw!")
    elif computer_choice == 1:
        print(f"Computer chose: \n{paper} \n You lose!")
    elif computer_choice == 2:
        print(f"Computer chose: \n{scissors} \n You win!")
elif player_choice == "1":
    print(paper)
    if computer_choice == 0:
        print(f"Computer chose: \n{rock}\n You win")
    elif computer_choice == 1:
        print(f"Computer chose: \n{paper} It's a draw!")
    elif computer_choice == 2:
        print(f"Computer chose: \n{scissors} You lose!")
elif player_choice == "2":
    print(scissors)
    if computer_choice == 0:
        print(f"Computer chose: \n{rock} \n You lose!")
    elif computer_choice == 1:
        print(f"Computer chose:\n{paper} \n You win!!")
    elif computer_choice == 2:
        print(f"Computer chose: \n{scissors} It's a draw!")
else:
   print("You typed an invalid number, you lose!")

