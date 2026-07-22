import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Docstring : This is the function to provide the card each time either computer or player hits."""
    card = random.choice(cards)
    return card

def calculate_sum(cards):
    """Return calculated sum of all cards.
        also checks for "Blackjack" - 2 cards with 1 ace and 1 10 value card.
    """

    if 11 in cards and 10 in cards and len(cards) == 2:
        # if sum(cards) == 21 and len(cards) == 2:
        return 0 # 0 represents a blackjack.
    
    # handling ace
    if 11 in cards and sum(cards) > 21:
        cards.remove(11) #find nd remove the very 1st instance of ele.
        cards.append(1)

    return sum(cards)


def compare(player_cards, computer_cards):
    player_cards_sum = sum(player_cards)
    computer_cards_sum = sum(computer_cards)
    
    if player_cards_sum == computer_cards_sum:
        print("DRAW !!!")
    elif calculate_sum(computer_cards) == 0:
        print("LOOSE !!!")
    elif calculate_sum(player_cards) == 0:
        print("WIN !!!")
    elif player_cards_sum > 21:
        print("LOOSE !!!")
    elif computer_cards_sum > 21:
        print("WIN !!!")
    elif player_cards_sum > computer_cards_sum:
        print("WIN !!!")
    elif player_cards_sum < computer_cards_sum:
        print("LOOSE !!!")

def play_game():
    player_cards = []
    computer_cards = []
    is_game_over = False

    # intial 2 cards
    for _ in range(2): # we r using _ becoz here we dont need any variable of any kind.
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    # player...
    while not is_game_over:
        player_card_sum = calculate_sum(player_cards)
        computer_card_sum = calculate_sum(computer_cards)

        if player_card_sum == 0 or computer_card_sum == 0 or player_card_sum > 21:
            is_game_over = True
        else:
            # game not over
            want_to_draw = input("Do u want to take new card? y or n").lower()
            if want_to_draw == 'y':
                # new card added
                player_cards.append(deal_card())
                # score need to be re-checked

            elif want_to_draw == 'n':
                is_game_over = True
                print("Game Ended !!!")
            else:
                print("Please enter either 'y' or 'n'")

    # computer
    # will draw cards till 17 then pass.
    while sum(computer_cards) != 0 and sum(computer_cards) <= 17:
        computer_cards.append(deal_card(cards))

    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer final hand: {computer_cards}, final score: {sum(computer_cards)}")
    print(compare(player_cards, computer_cards))

while input("Do u want to play a game of blackjack ? 'y' or 'n'?").lower() == 'y':
    os.system("clear")
    play_game()