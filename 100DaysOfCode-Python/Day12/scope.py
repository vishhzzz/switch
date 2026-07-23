enemies = 1

def increase_enemies():
    enemies = 2 # LOCAL SCOPE, if this enemies was not there then global enemies would have been read
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}") # GLOBAL SCOPE

# everything that u can name has a namespace.
# that namespace is valid within certain scope.
# 2 scopes:
# local - within functions / wherever declared
# global - within, outside functions