# price to pay for roller coster ticket.

print("Welcome to the roller coaster!")
price = 0
height = int(input("Whats your height in cm? "))
if height >= 120:
    print("Congrats! You can ride the roller coaster.")
    # do u want to add a photo to your ticket?
    photoWanted = bool(input("Do you want to add a photo to your ticket? True or False?"))
    if photoWanted == True:
        price += 3
    age = int(input("Enter your age: "))
    if age < 12:
        price += 5
        print("Your ticket price is $5.")
    elif age >= 12 and age <= 18:
        price += 7
        print("Your ticket price is $7.")
    else:
        price += 12
        print("Your ticket price is $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
print(f"Heres your ticket price: ${price}.")
