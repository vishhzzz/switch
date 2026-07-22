import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Docstring : This is the function to provide the card each time either computer or player hits."""
    card = random.choice(cards)
    return card

player_cards = []
computer_cards = []

# intial 2 cards
for _ in range(2): # we r using _ becoz here we dont need any variable of any kind.
    player_cards.append(deal_card())
    computer_cards.append(deal_card())