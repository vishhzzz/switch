from random import randint

dice_images = [1, 2, 3, 4, 5, 6]
dice_num = randint(1, 6)
print(dice_images[dice_num])

# This is an occasional bug which does not occur everytime, it does occur occasionally
# The problem here is we have dice images from 1 - 6 i.e., 1, 2, 3, 4, 5, 6
# which has an indexes from 0 to 5 i.e., 0, 1, 2, 3, 4, 5
# randint(a, b): gives a random int in between a and b, both included.
# everything works fine till it produces 1, 2, 3, 4, 5. The moment it produces 6 all hell break loose.
# becoz then we will be finding dice_images[6] but indexes are from 0-5. Thus, INDEX_OUT_BOUNDS_ERROR would be there.