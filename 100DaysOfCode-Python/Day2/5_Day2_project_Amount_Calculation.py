print("Welcome to the amount calculator.")
# this will take amount in string
# amount = input("What was the total bill?")

amount = float(input("What was the total bill? $"))

# we are consider tip in %
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
tipAmount = tip * amount / 100

noOfPeople = int(input("How many people to split the bill?"))

perPersonAmount = (amount + tipAmount) / noOfPeople
print(f"Each person should pay: ${perPersonAmount:.2f}")