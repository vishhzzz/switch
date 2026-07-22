import random

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

player_cards = []
computer_cards = []

# intial 2 cards
for _ in range(2): # we r using _ becoz here we dont need any variable of any kind.
    player_cards.append(deal_card())
    computer_cards.append(deal_card())