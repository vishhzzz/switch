from menu import Menu
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# menu is an object from Menu class
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    user_choice = input(f"What would you like? ({menu.get_items()}): ")
    if user_choice == 'off':
        print("Machine is being turned off for maintenance")
        break
    elif user_choice == 'report':
        coffee_maker.report() #will print the report of coffee machine
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            # we now need to process payments...
            if money_machine.make_payment(drink.cost):
                # make coffee
                coffee_maker.make_coffee(drink)