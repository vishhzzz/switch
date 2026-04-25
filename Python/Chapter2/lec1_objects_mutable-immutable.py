# Objects - Mutable vs Immutable

# In Python, mostly everything is an object. 
# Everything in Python is an object be it:
    # Numbers
    # Strings
    # Lists
    # Dictionaries
    # Functions
    # Classes
    # Modules
# Visualize object as container which has 3 properties:
    # Identity - which is unique for each object and can be obtained using id() function
    # Type - which can be obtained using type() function
    # Value - which is the data stored in the object

# Mutable vs Immutable Objects
# Mutable objects are those whose value can be changed after they are created.
# Immutable objects are those whose value cannot be changed after they are created.

# Mutable Objects:
# Lists
# Dictionaries
# Sets
# User-defined classes (by default)

# Immutable Objects:
# Numbers (int, float, complex)
# Strings
# Tuples
# Frozensets
# User-defined classes (if __slots__ is not used)

# numbers are immutable.
x = 10
print(f"x is : {x}, id(x) is: {id(x)}")

x = 20
print(f"x is : {x}, id(x) is: {id(x)}")

# set is mutable.
set1 = set()
print(f"intial set is: {set1}, id is : {id(set1)}")

set1.add(1)
print(f"set after adding 1 is: {set1}, id is : {id(set1)}")
