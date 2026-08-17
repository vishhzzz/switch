# List is a DS which can store multiple items in a single variable. It is a collection of items which are ordered and changeable. It allows duplicate members.
# DS : Data Structure -> way of organizing and storing data in a computer so that it can be accessed and modified efficiently.
# ordered : the items in a list have a defined order, and that order will not change unless we explicitly change it.
# changeable : we can change, add, and remove items in a list after it has been created.
# allows duplicate members : since lists are indexed, they can have items with the same value.

# representation
myList = ["apple", "banana", "cherry"]

# printing list
print(myList)

# accessing items in list
print(myList[0]) # prints the first item in the list
print(myList[1]) # prints the second item in the list
print(myList[2]) # prints the third item in the list
print(myList[-1]) # prints the last item in the list
print(myList[-2]) # prints the second last item in the list
print(myList[-3]) # prints the third last item in the list

# Why index starts from 0?
# Think it like offset from the first item. The first item is at offset 0, the second item is at offset 1, and so on. This is a convention that has been followed in many programming languages and it helps in simplifying the calculations for accessing items in the list.

myList[0] = "grapes" # we can change the value of an item in the list since it is changeable.
print(myList)

# adding items to list at end
myList.append("orange") # this will add "orange" at the end of the list.
print(myList)

# adding items to list at specific position
myList.insert(1, "kiwi") # this will add "kiwi" at index 1 in the list.
print(myList)

# adding list at last
myList.extend(["mango", "papaya"]) # this will add "mango" and "papaya" at the end of the list.
print(myList)