# If we try to access elements of a list and by any chance we try to access an index which is out of range, we will get an error called IndexError: list index out of range.

# To avoid this error, we can use nested lists. A nested list is a list that contains other lists as its elements. We can access the elements of the nested list using multiple indices.

# Example of nested list
fruits = ["apple", "banana", "orange"]
vegetables = ["carrot", "broccoli", "spinach"]
eatables = [fruits, vegetables]
print(eatables) # this will print the nested list
print(eatables[0]) # this will print the first element of the nested list which is the fruits list.
print(eatables[1]) # this will print the second element of the nested list which is the vegetables list.
print(eatables[0][1]) # this will print the second element of the fruits list which is "banana".
print(eatables[1][2]) # this will print