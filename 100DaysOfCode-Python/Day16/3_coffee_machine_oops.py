from menu import Menu
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# menu is an object from Menu class
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    user_choice = "What would you like? ({menu.get_items()}): "
    if user_choice == 'off':
        print("Machine is being turned off for maintenance")
        break
    elif user_choice == 'report':
        coffee_maker.report() #will print the report of coffee machine
    elif user_choice == 'cgh':
        # we need to use find_drink
        menu.find_drink('espresso')
