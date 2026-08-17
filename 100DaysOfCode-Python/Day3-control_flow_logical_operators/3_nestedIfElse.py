# price to pay for roller coster ticket.

print("Welcome to the roller coaster!")

height = int(input("Whats your height in cm? "))
if height >= 120:
    print("Congrats! You can ride the roller coaster.")
    print("Heres your ticket price.")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Your ticket price is $5.")
    elif age >= 12 and age <= 18:
        print("Your ticket price is $7.")
    else:
        print("Your ticket price is $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
