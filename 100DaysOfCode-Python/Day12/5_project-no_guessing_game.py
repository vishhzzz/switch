# Number Guessing Game
import random

def start_game(no_of_chances, initial_guessed_number):
    """Starting Game in order to play"""
    print(f"You have {no_of_chances} attempts remaining to guess the number.")

    while no_of_chances:
        guessed_number = int(input("Make a guess: "))
        if guessed_number < initial_guessed_number:
            print("Too Low !!!")
            print("Guess Again ...")
            no_of_chances -= 1
            print(f"You have {no_of_chances} attempts remaining to guess the number.")
        elif guessed_number > initial_guessed_number:
            print("Too High !!!")
            print("Guess Again ...")
            no_of_chances -= 1
            print(f"You have {no_of_chances} attempts remaining to guess the number.")
        else:
            print("You Won !!!")
            return
    
    print("You have run out of guesses, you loose....")
    print(f"Original Number was {initial_guessed_number}")

def welcome_message():
    """Welcoming User to GAME !!!"""
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    initial_guessed_number = random.randint(1, 100) #both 1 and 100 are inclusive, this will give a random interger in between them
    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if game_level == 'easy':
        no_of_chances = 10
    elif game_level == 'hard':
        no_of_chances = 5
    else:
        print("Kindly choose either 'easy' or 'hard'")
        return
    
    # starting game
    start_game(no_of_chances, initial_guessed_number)


welcome_message()