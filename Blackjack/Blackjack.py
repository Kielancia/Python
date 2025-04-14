import random

import art
# The deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def what_number_is_ace(some_cards):
    """Checking if Ace is 11 or 1"""
    next_card = random.choice(cards)
    if next_card == 11:
        if (sum(some_cards) + next_card) > 21:
            next_card = 1
    some_cards.append(next_card)

def scores_printing(users, computers):
    """Displaying user's and computer's scores"""
    print(f"Your hand: {users}. Total score: {sum(users)}")
    print(f"Computer's hand: {computers}. Total score: {sum(computers)}")

def who_won(users, computers):
    """Checking who won the game"""
    if 21 >= sum(computers) > sum(users):
        print("You lose.")
    elif sum(computers) > 21:
        print("Opponent went over. You win! ")
    elif sum(computers) == sum(users):
        print("Draw.")
    else:
        print("You win!")

def blackjack():
    """Blackjack game. You have to be as near to 21 as possible but cannot go over it."""
    wanna_play = input("Do you wanna play Blackjack? Type 'y' for yes and 'n' for no. ")

    if wanna_play == "y":
        print(art.logo)
        not_game_over = True
        computer_cards = []

        while not_game_over:
            user_cards = random.choices(cards,None,k=2)
            computer_cards.append(random.choice(cards))
            scores_printing(user_cards,computer_cards)

            if sum(user_cards) == 21:
                print("You have Blackjack. You won!")
                not_game_over = False
            else:
                wanna_card = input("Do you want another card? Type 'y' for yes and 'n' for no. ")

                while wanna_card == "y":
                    what_number_is_ace(user_cards)
                    scores_printing(user_cards,computer_cards)

                    if sum(user_cards) > 21:
                        print("You went over. You lose! ")
                        not_game_over = False
                        wanna_card = "n"
                    elif sum(user_cards) == 21:
                        print("Congratulation. You won! ")
                        not_game_over = False
                        wanna_card = "n"
                    else:
                        wanna_card = input("Do you want another card? Type 'y' for yes and 'n' for no. ")

                if sum(user_cards) < 21:
                    while sum(computer_cards) < 17:
                        what_number_is_ace(computer_cards)

                    scores_printing(user_cards,computer_cards)
                    who_won(user_cards,computer_cards)
                    not_game_over = False

        blackjack()

blackjack()