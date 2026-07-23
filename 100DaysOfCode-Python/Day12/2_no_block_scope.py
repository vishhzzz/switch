# There is no BLOCK scope in PYTHON.

# Block : a block of code i.e., indented and within :
#           like-> if, for, while...

game_level = 3
enemies = ["Zombie", "Skeletons", "Alien"]

# CASE 1
# if game_level < 5:
#     # this is block scope
#     new_enemy = enemies[0]

# print(new_enemy) #new_enemy has global scope

# CASE 2
def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]
    
    print(new_enemy) # perfectly fine. but here there may be a case when game_level is above 5 then it does not go inside if and hence no new_enemy is created so we should always have a backup

print(new_enemy) # name error -> as new_enemy has local scope within create_enemy function