# age = int(input("How old are u ???"))
# if age > 18:
#     print("U can drive at age {age}")


# There r 2 types of error:
# 1. these will be shown on editor during writing such as indentation issues or so.
# 2. These will be shown at run time. Such as above error

# What happen if user writes twelve instead of 12 or so???
# Program will break

# in order to save us from this scenario, we need to use:
# Exception handling - try, except
# The idea is we can catch an exception via Python code.
# We know that one of the potential errors here is "VALUE ERROR", so we can catch that and provide an alternative path to go to.


# We trap the potential error causing line inside try block.
try:
    age = int(input("How old are u ???"))
# now we will catch the exact error type which can occur.
except ValueError:
    print("You have typed string representation of number. Please enter something like 15.")
    # we will give them another chance.
    age = int(input("How old are u ???"))

if age > 18:
    print(f"You can drive at age {age}")