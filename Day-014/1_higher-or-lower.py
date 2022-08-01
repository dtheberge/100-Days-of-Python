import art
import game_data
import random
from replit import clear

def game():

    game_over = False
    first_guess = True
    score = 0

    while(not game_over):
        clear()
        print(art.logo)

        if(not first_guess):
            score += 1
            print(f"You're right! Current Score: {score}.")
        
        first_guess = False

        data_A = random.choice(game_data.data)
        data_B = random.choice(game_data.data)

        print(f"Compare A: {data_A['name']}, {data_A['description']}, from {data_A['country']}.")
        print(art.vs)
        print(f"Against B: {data_B['name']}, {data_B['description']}, from {data_B['country']}.")
        guess = input("Who has more followers? Type 'A' or 'B': ")

        if(data_A['follower_count'] > data_B['follower_count']):
            if (guess == 'B'):
                game_over = True
        elif(data_B['follower_count'] > data_A['follower_count']):
            if (guess == 'A'):
                game_over = True

    print(f"\nSorry, that's wrong. Your final score was {score}.")

game()