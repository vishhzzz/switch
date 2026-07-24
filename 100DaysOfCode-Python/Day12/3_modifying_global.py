enemies = 1

def increase_enemies():
    # enemies = 2 # LOCAL SCOPE, if this enemies was not there then global enemies would have been read
    # these 2 r entirely seperate variable.

    # if i want to use global one here i.e., if i wanna modify global variable value then we use like this

    # global <variable_name>
    global enemies
    enemies = 2 # now these 2 are same both r tapping into global variable.
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}") # GLOBAL SCOPE

# everything that u can name has a namespace.
# that namespace is valid within certain scope.
# 2 scopes:
# local - within functions / wherever declared
# global - within, outside functions