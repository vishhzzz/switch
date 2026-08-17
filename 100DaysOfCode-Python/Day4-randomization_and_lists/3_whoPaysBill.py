# We need to find out who will pay the bill in a group of friends.
# Everytime when we run the prog., it should randomly select a name from the list of friends and that person will pay the bill.
import random
friends = ["Vishnu", "Suresh", "Ramesh", "alex", "john"]

idx = random.randint(0, 4)
print(f"{friends[idx]} will pay the bill.")

# we can also use random.choice() method to select a random name from the list of friends.
print(f"{random.choice(friends)} will pay the bill.")