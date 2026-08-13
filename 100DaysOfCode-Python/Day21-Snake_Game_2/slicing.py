# used when we want to go to certain part of list/tuples

# same for tuples too.

list_slicing = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#             [0,  1,   2,   3,   4,   5,   6,   7]

# suppose i want c, d, e
print(list_slicing[2:5]) #will include 2nd pos till before 5th pos -- c, d, e

# from 2nd char to end
print(list_slicing[2:])

# till x pos
print(list_slicing[:4])

# slicing with gap
print(list_slicing[1:5:2]) #b, d

# every item with specific jump
print(list_slicing[::2]) # a, c, e, g

# reverse
print(list_slicing[::-1])