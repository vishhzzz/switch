# Tuple
# Another data type
# it is shown as : () <--- round brackets 
# with each element surrounded by ,

# (1, 3, 6, 8)

# Very similar to list

# but the tuples are 'ORDERED'.
# ORDERED: they keep the position in which they r stored.
# ORDERED: does not means that they r sorted or in a sequence, it just means python remember the sequence or index and will always keep elements that way.

# compared to set, which is unordered i.e., when we try to print it, it prints elements in diff order.


# we cant change the values stored in a 'tuple' ---> STONE CARVED
# We cant modify tuple in any way.  <--- IMMUTABLE


# we can access each element via their indexes through [].
my_tuple = (1, 3, 6, 100, 20)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
# no matter how many times, i print my_tuple it will always display in same order <--- Ordered.



# To change a tuple which is non-modifiable or immutable, there is a hack:
# first change it to list and then change it and later convert that to tuple again :)

