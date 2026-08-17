'''
Dictionary Comprehension
- very usefull
- used to create a new dictionary using existing list or dictionary.
- new_dict = {new_key:new_value for item in list}
- new_dict = {new_key:new_value for (key, value) in dict.items()}
- new_dict = {new_key:new_value for (key, value) in dict.items() if test}
'''
from random import randint
names = ['Alex', 'Beth', 'Caroline', 'Dava', 'Elanor', 'Freddie']
dict_names_scores = {
    name: randint(1, 100) for name in names
}
print(dict_names_scores)

passed_dict = {
    student:value for (student, value) in dict_names_scores.items() if dict_names_scores[student] >= 50
}
print(passed_dict)

print(dict_names_scores)
print(dict_names_scores.items()) #.items() returns a dictionary view of dictionary ele as key, value in form of tuples
