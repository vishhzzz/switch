import ascii_art
import os

print(ascii_art.logo)
print("Welcome to the secret auction program\n.")

def auction(auctioner):
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: "))
    bidder = {
        'name': name,
        'bid': bid,
    }
    auctioner.append(bidder)

def secretAuction(auctioner):
    maxBidder = {'name' : "", 'bid': 0}
    for bidder in auctioner:
        if maxBidder['bid'] < bidder['bid']:
            maxBidder['bid'] = bidder['bid']
            maxBidder['name'] = bidder['name']
    print(f"The winner is {maxBidder['name']} with a bid of {maxBidder['bid']}.")


auctioner = []
auction(auctioner)
while True:
    anyMorePlayers = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if anyMorePlayers == 'no':
        secretAuction(auctioner)
        break
    elif anyMorePlayers == 'yes':
        os.system("clear") #will only work for ubuntu and mac
        # for windows
        # os.system("cls")
        auction(auctioner)
    else:
        print("Please enter 'yes' or 'no'.")