# Unique to Python
# it increases readablity and decreases no. of code lines.

# Comprehension can applied on any sequence:
# list
# tuple
# string
# range

# List Comprehension: creates a new list from old list.

# Old Way
no_list = [1, 2, 3]
new_list = []

for ele in no_list:
    new_ele = ele + 1
    new_list.append(new_ele) #2, 3, 4


# MENTOS way / Comprehension
# new_list = [new_item for item in list]
new_list = [ele + 1 for ele in no_list ]
print(new_list)

# Comprehension works for any sequence
# like - string
name = "vishal"
new_list = [letter for letter in name]
print(new_list) #--> ['v', 'i', 's', 'h', 'a', 'l']


# Comprehension for range
new_list = [ele * 2 for ele in range(1, 5)]
print(new_list)


# Condition List Comprehension
'''
new_list = [new_ele for ele in list if test_expression]
'''

names = ['Alex', 'Beth', 'Caroline', 'Dava', 'Elanor', 'Freddie']
new_list = [name.upper() for name in names if len(name) >= 5]
print(new_list)