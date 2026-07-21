# We are going to build a game named - blackjack.

# Here are the rules:
# *** Card Values ***
# Number Cards (2-10) = Face Value
# Jack, Queen, King - 10
# Ace = 11 (default), 1 in order to prevent burst.

# *** Initial Deal ***
# Player gets 2 cards.
# Computer dealer gets 2 cards.
# The Player can only see 1 of the dealer's cards initially.

# *** BlackJack ***
# A BlackJack is an ACE + any 10 value card in initial 2 cards. Basically 21 in intial 2 cards combo.
# BlackJack beats any normal 21 made with more than 2 cards.

# *** Player Turns ***
# Choose:
# HIT   ---> take another card
# STAND ---> end your turn
# If your total exceeds 21, burst and loose.

# *** Dealer's Turn ***
# The dealer automatically keeps drawing while score is less than 17.
# Once the dealer reaches 17 or more, they stand.

# *** ACE HANDLING ***
# If:
#   hand contains an ACE - 11 
#   total > 21, 
#  then one ACE  is converted from 11 to 1.
# Example:
# [11, 9, 5] = 25
#  25 > 21, ACE converts to 1
# [11, 9, 5] ---> [1, 9, 5] = 15

# *** Wining Conditions ***
# Both have BLACKJACK, "DRAW"
# Dealer has BLACKJACK, "LOOSE"
# I have BLACKJACK, "WIN"
# I burst (>21), "LOOSE"
# Dealer burst (>21), "WIN"
# Higher scorer wins.
# Equal Score, draw.





# ************************** Implementations ***************************

# storing Card Values - list [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
#                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, K, Q, J]
# Ace is either 11 or 1

# imports
import random


# ascii art
logo = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/           
"""

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def handlingAce(playerCard):
    if sum(playerCard) > 21 and 11 in playerCard:
        playerCard.remove(11)
        playerCard.append(1)

def concludeGame(playerCard, computerCard):
    # player
    print(f"Your final hand: {playerCard}, final score: {sum(playerCard)}")

    # computer
    print(f"Computer's final hand: {computerCard}, final score: {sum(computerCard)}")

    # handling ace
    handlingAce(playerCard)

    # comparing
    if sum(playerCard) == sum(computerCard):
        print("DRAW !!!")
    elif sum(playerCard) > 21:
        print("LOOSE !!!")
    elif sum(computerCard) < sum(playerCard):
        print("WIN !!!")
    elif sum(computerCard) < 21 and sum(computerCard) > sum(playerCard):
        print("LOOSE !!!")



def proceedGame(playerCard, computerCard):
    # player
    playFurther = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if playFurther == 'n':
        # this is the moment of calculations i.e., who won and who not!!!!
        concludeGame(playerCard, computerCard)
    elif playFurther == 'y':
        handlingAce(playerCard)
        # player
        playerCard.append(random.choice(cards))
        print(f"Your cards : {playerCard}, current score: {sum(playerCard)}")
        if sum(playerCard) > 21:
            print(f"Computer's final hand: {computerCard}, final score: {sum(computerCard)}")
            print("LOOSE !!!")
        # computer
        # computer will take till 17 and will stand afterwards.
        if sum(computerCard) < 17:
            computerCard.append(random.choice(cards))            

def startGame():
    print(logo)

    # need to display player 1st 2 cards

    # option 1
    # playerCard.append(random.choice(cards))
    # playerCard.append(random.choice(cards))
    # option 2
    # range(2) -> 0, 1
    # for _ in range() --> _ variable for iteration
    # this simply means i dont care about this variable name, i just wanna use it.
    playerCard = [random.choice(cards) for _ in range(2)]
    # display player cards
    print(f"Your cards: {playerCard}, current score:  {sum(playerCard)}")
    computerCard = [random.choice(cards) for _ in range(2)]
    # displaying Computer's 1st card
    print(f"Computer's first card: {computerCard[0]}")

    # win or loose : at this point we r sure that each has couple of cards so we can check for early "BLACKJACK here only."
    if sum(playerCard) == 21 and sum(computerCard) == 21:
        print("DRAW !!!")
    elif sum(playerCard) == 21:
        print("WIN !!!")
    elif sum(computerCard) == 21:
        print("Loose")
    else:
        # this part or block moves game further by letting user choose cards.
        proceedGame(playerCard, computerCard)




# Endless Game loop
while True:
    playGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if playGame == 'y':
        startGame()
    elif playGame == 'n':
        print("Sad!!!, Please be back...")
        break
    else:
        print("Kindly enter only 'y' or 'n'")
        break