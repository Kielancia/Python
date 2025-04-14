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

# Table of choices as Strings
r_p_s = [rock, paper, scissors]

# Input from user as a String
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper'"
                    " or 2 for Scissors.\n")

# Random choice of computer from Table of choices as a Number (needed to do comparisons later)
computer_choice = random.randint(0,2)

# Random choice of computer from Table of choices as a String
computer_choice_2 = r_p_s[computer_choice]

if type(user_choice) == int or user_choice == "0" or user_choice == "1" or user_choice == "2":
    # Input from user as a String
    user_choice_2 = r_p_s[int(user_choice)]
    user_choice = int(user_choice)
    # Printing both choices, Computer's and User's
    print(user_choice_2)
    print(f"Computer chose: {computer_choice_2}")
    # Checking conditions of winning in Rock, Paper, Scissors game
    if user_choice != computer_choice:
        if user_choice == 0: # User chose Rock
            if computer_choice == 1: # Computer chose Paper
                print("You lose. Pathetic.")
            else: # Computer chose Scissors
                print("Congratulation! You won.")
        elif user_choice == 1: # User chose Paper
            if computer_choice == 0: # Computer chose Rock
                print("Congratulation! You won.")
            else: # Computer chose Scissors
                print("You lose. Pathetic.")
        elif user_choice == 2: # User chose Scissors
            if computer_choice == 0: # Computer chose Rock
                print("You lose. Pathetic.")
            else: # Computer chose Paper
                print("Congratulation! You won.")
        else: # User typed something other than 0, 1 or 2
            print("You're stupid or what? Type 0 for Rock, 1 for Paper'"
                        " or 2 for Scissors, Dumbass.")
    else:
        print("Draw. Do better next time.")
else:
    print("You're stupid or what? Type 0 for Rock, 1 for Paper'"
          " or 2 for Scissors, Dumbass.")