print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go? Type 'left' or 'right'")
direction = input().lower()

if direction == "left":
    waitOrSwim = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()
    if waitOrSwim == "wait":
        doorColor = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower
        if doorColor == "yellow":
            print("You found the treasure! You Win!")
        elif doorColor == "red":
            print("It's a room full of fire. Game Over.")
            print("Bye!!!")
        elif doorColor == "blue":
            print("You enter a room of beasts. Game Over.")
            print("Bye!!!")
    else:
        print("You get attacked by an angry trout. Game Over.")
        print("Bye!!!")
else:
    print("You fell into a hole. Game Over.")
    print("Bye!!!")