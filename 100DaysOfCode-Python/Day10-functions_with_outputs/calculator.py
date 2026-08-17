# Note
# We can store functions as some other name too.
# def add(num1, num2):
    # return num1 + num2

# my_fav_op = add

# to add 2 numbers, now i can do this also
# my_fav_op(num1, num2)

# Basically we can store functions inside variables.


import ascii_art
import os
import sys

#---------------------------------------------------------------- functions operations
def add(num1, num2):
    '''
    Perform addidition between 2 numbers
    
    :param num1: operand1
    :param num2: operand2
    :return: will return operand1 + operand2
    '''
    print(f"{num1} + {num2} = {num1 + num2}")
    return num1 + num2

def sub(num1, num2):
    '''
    Perform subtraction between 2 numbers
    
    :param num1: operand1
    :param num2: operand2
    :return: will return operand1 - operand2
    '''
    print(f"{num1} - {num2} = {num1 - num2}")
    return num1 - num2

def multiply(num1, num2):
    '''
    Perform multiplication between 2 numbers
    
    :param num1: operand1
    :param num2: operand2
    :return: will return operand1 * operand2
    '''
    print(f"{num1} * {num2} = {num1 * num2}")
    return num1 * num2

def divide(num1, num2):
    '''
    Perform division between 2 numbers
    
    :param num1: operand1.
    :param num2: operand2.
    :return: will return operand1 / operand2
    :raises ZeroDivisionError: If num2 is 0
    '''
    if num2 == 0:
        print("Can't divide by 0.")
        return None
    print(f"{num1} / {num2} = {num1 / num2}")
    return num1 / num2

# ---------------------------------------------------------------------------------operators list
# list of all operators stored as key in dictionary with relevant functions as value.
operators = {
    '+': add,
    '-': sub,
    '*': multiply,
    '/': divide,
}

def operatorsAvailable():
    for operator in operators:
        print(operator)

# --------------------------------------------------------------------------------calculation logic
def calculate(num1, num2, operation):
    # best functionality
    # basically functions is an object like other things in python so it can be stored like others.
    # Simply funcitons are triggered via () apart from that they r just good little baby which can be assigned to stored somewhere else.
    return operators[operation](num1, num2)

# --------------------------------------------------------------------------------user inputs
def userInputs(num = None):
    '''
    Docstring for userInputs
    if user passes number then it is assigned otherwise we ask user to enter number.
    :param num: user given number
    '''
    if num is None:
        num1 = float(input("What's the first number?: "))
    else:
        num1 = num

    operatorsAvailable()

    operation = input("Pick an operation: ")

    # if operation != '+' and operation != '-' and operation != '*' and operation != '/':
    if operation not in operators:
        print("Enter operations from list only.")
        return None
    num2 = float(input("What's the next number?: "))

    return calculate(num1, num2, operation)

# --------------------------------------------------------------------------------- code part
print(ascii_art.logo)

value = userInputs()
if value == None:
    print("Enter correct inputs.")
    sys.exit(1) #we r exiting with error message.

while True:
    os.system('cls' if os.name == 'nt' else 'clear') #cross platform.
    choice = input(f"Type 'y' to continue calculating with {value} or type 'n' to start a new calculation, 'stop' to exit: ")
    if choice == 'y':
        num1 = value
    elif choice == 'n':
        num1 = float(input("What's the first number?: "))
    elif choice == 'stop':
        print("Thanks for using my calci...")
        break
    else:
        print("Enter correct option.")
        continue

    value = userInputs(num1)
    if value is None:
        print("Enter correct inputs.")
        break