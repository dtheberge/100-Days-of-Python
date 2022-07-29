import art
import random

def difficulty():
    diff = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()
    if (diff == 'easy'):
        return 10
    else:
        return 5

def guessing_game():
    rand_answer = random.randint(1, 100)
    guess = -1
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    guesses_remaining = difficulty()

    while(guesses_remaining > 0 and not guess == rand_answer):
        print(f"\nYou have {guesses_remaining} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if (guess < rand_answer):
            print("Too low.\nGuess again.")
        elif(rand_answer < guess):
            print("Too high.\nGuess again.")
        
        guesses_remaining -= 1

    if(guess == rand_answer):
        print(f"You got it! The answer was {rand_answer}")
    else:
        print("You've run out of guesses, you lose.")

    if input("\nDo you want to play again? 'y' for yes, 'n' for no: ") == 'y':
        guessing_game()

guessing_game()