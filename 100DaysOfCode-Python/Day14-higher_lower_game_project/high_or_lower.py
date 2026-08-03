import art
import game_data
import random
import os

print(art.logo)

# We have a list of dictionaries.
# Initially we have to choose 2 random dictionary element.
# then based on who is winner, keep that and choose other element randomly.
# Game only stops when u lost, with correct guess counts.

# choosing a random element from list
# random.choice(list)

def continue_game(player1, score):
    """Proceed with the game"""
    # Player 1
    print(f"Compare A: {player1['name']}, a {player1['description']}, from {player1['country']}.")

    print(art.vs)

    # Player 2
    player2 = random.choice(game_data.data)
    print(f"Against B: {player2['name']}, a {player2['description']}, from {player2['country']}.")

    ques = input("Who has more followers? Type 'A' or 'B':").upper()

    if ques == 'A' and player1["follower_count"] > player2["follower_count"]:
        score += 1
        print(f"You are right! Current score: {score}.")
        continue_game(player1, score)
    elif ques == 'B' and player1["follower_count"] < player2["follower_count"]:
        score += 1
        print(f"You are right! Current score: {score}.")
        continue_game(player2, score)
    else:
        os.system("cls" if os.name == "nt" else "clear") #nt is for windows
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}.")
        return

def play_game():
    """Starting Game."""

    score = 0
    # here we will start with choosing 1st 2 elements
    # 1st element
    info1 = random.choice(game_data.data)
    print(f"Compare A: {info1['name']}, a {info1['description']}, from {info1['country']}.")

    print(art.vs)

    # 2nd element
    info2 = random.choice(game_data.data)
    print(f"Against B: {info2['name']}, a {info2['description']}, from {info2['country']}.")

    ques = input("Who has more followers? Type 'A' or 'B':").upper()

    if ques == 'A' and info1["follower_count"] > info2["follower_count"]:
        score += 1
        print(f"You are right! Current score: {score}.")
        continue_game(info1, score)
    elif ques == 'B' and info1["follower_count"] < info2["follower_count"]:
        score += 1
        print(f"You are right! Current score: {score}.")
        continue_game(info2, score)
    else:
        os.system("cls" if os.name == "nt" else "clear") #nt is for windows
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}.")


play_game()