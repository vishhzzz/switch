import random
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = new_item + item
    b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

# The error here is simple, we miss to add append of b_list inside for loop, i.e., only 1 element is being added to list.