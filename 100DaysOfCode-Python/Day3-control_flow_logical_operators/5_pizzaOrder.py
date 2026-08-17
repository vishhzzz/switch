# Automatic Pizza Order Program
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
if add_pepperoni != 'Y' and add_pepperoni != 'N':
    print("Invalid input for pepperoni. Please enter Y or N.")
add_cheese = input("Do you want extra cheese? Y or N ")
if add_cheese != 'Y' and add_cheese != 'N':
    print("Invalid input for extra cheese. Please enter Y or N.")

bill = 0
if size == 'S':
    bill += 15
    if add_pepperoni == 'Y':
        bill += 2
elif size == 'M':
    bill += 20
    if add_pepperoni == 'Y':
        bill += 3
elif size == 'L':
    bill += 25
    if add_pepperoni == 'Y':
        bill += 3
else:
    print("Invalid size entered.")

if add_cheese == 'Y':
    bill += 1

print(f"Your final bill is: ${bill}.")