MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}

RESOURCES = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}

def display_resources():
    print(f"Water: {RESOURCES['Water']}ml\nMilk: {RESOURCES['Milk']}ml\nCoffee: {RESOURCES['Coffee']}g\nMoney: ${RESOURCES['Money']}")

def check_resources(coffee_type):
    if coffee_type == 'espresso':
        if MENU["espresso"]['ingredients']['water'] > RESOURCES["Water"]:
            print("Sorry!, there isn't enought Water!")
            return False
        elif MENU["espresso"]['ingredients']['coffee'] > RESOURCES["Coffee"]:
            print("Sorry!, there isn't enought Coffee!")
            return False
    elif coffee_type == 'latte':
        if MENU["latte"]['ingredients']['water'] > RESOURCES["Water"]:
            print("Sorry!, there isn't enought Water!")
            return False
        elif MENU["latte"]['ingredients']['coffee'] > RESOURCES["Coffee"]:
            print("Sorry!, there isn't enought Coffee!")
            return False
        elif MENU["latte"]['ingredients']['milk'] > RESOURCES["Milk"]:
            print("Sorry!, there isn't enought Coffee!")
            return False
    elif coffee_type == 'cappuccino':
        if MENU["cappuccino"]['ingredients']['water'] > RESOURCES["Water"]:
            print("Sorry!, there isn't enought Coffee!")
            return False
        elif MENU["cappuccino"]['ingredients']['coffee'] > RESOURCES["Coffee"]:
            print("Sorry!, there isn't enought Coffee!")
            return False
        elif MENU["cappuccino"]['ingredients']['milk'] > RESOURCES["Milk"]:
            print("Sorry!, there isn't enought Milk!")
            return False
    return True

def transaction_for_coffee(coffee_type):
    print("Please enter coins.")
    quaters = int(input("How many quaters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    cost = COIN_VALUES["quarter"] * quaters + COIN_VALUES["nickel"] * nickles + COIN_VALUES["penny"] * pennies + COIN_VALUES["dime"] * dimes

    coffee_cost = MENU[coffee_type]['cost']
    if cost < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
        return
    else:
        if cost > coffee_cost:
            print(f"Here is ${cost - coffee_cost} in change.")
        RESOURCES["Money"] += coffee_cost
        print(f"Here's your {coffee_type:.2f}, enjoy!")
    
    # updating resources
    RESOURCES["Coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    RESOURCES["Water"] -= MENU[coffee_type]["ingredients"]["water"]
    if coffee_type != 'espresso':
        RESOURCES["Milk"] -= MENU[coffee_type]["ingredients"]["milk"]

while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'espresso':
        if check_resources(user_choice):
            transaction_for_coffee(user_choice)          
    elif user_choice == 'latte':
        if check_resources(user_choice):
            transaction_for_coffee(user_choice)
    elif user_choice == 'cappuccino':
        if check_resources(user_choice):
            transaction_for_coffee(user_choice)
    elif user_choice == 'off':
        print("Turning of Coffee Machine.")
        break
    elif user_choice == 'report':
        display_resources()

print("Coffee Machine successfully turned off.")