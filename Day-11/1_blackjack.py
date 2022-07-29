############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###############################################################
import art
import random
from replit import clear

def turn():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[random.randint(0, 12)]


def blackjack():
    clear()
    print(art.logo)

    game_over = False
    comp_score = 0
    user_score = 0
    user_cards = []
    comp_cards = []

    while(game_over == False):
        if (comp_score == 0 and user_score == 0):

            card = turn()
            card_2 = turn()
            user_cards.append(card)
            user_cards.append(card_2)
            user_score += card + card_2
            print(f"Your cards: {user_cards}")

            card = turn()
            card_2 = turn()
            comp_cards.append(card)
            comp_cards.append(card_2)
            comp_score += card + card_2
            print(f"Computer's first card: {card}")

        else: 
            card = turn()
            user_cards.append(card)
            user_score += card
            print(f"\nYour cards: {user_cards}")

            card = turn()
            comp_score += card
            comp_cards.append(card)

        if (comp_score > 21 or user_score > 21):
            game_over = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'n':
                game_over = True

    print(f"Your final hand: {user_cards} = {user_score}")
    print(f"Computer's final hand: {comp_cards} = {comp_score}")

    if(comp_score == user_score):
        print("It was a draw !")
    elif(comp_score > 21 and user_score < 21):
        print("You Won !")
    elif(user_score > 21 and comp_score < 21):
        print("You Lost..")
    elif(comp_score > user_score):
        print("You lost.. ")
    else:
        print("You Won !")

    if input("\nDo you want to play again? 'y' for yes, 'n' for no: ") == 'y':
        blackjack()

blackjack()