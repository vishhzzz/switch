# We can have other datatype present inside our dict, which we refer to as nested dict.
# It could be dict inside dict or list inside dict.

# example
dict1 = {
    'key' : ['list1', 'list2'],
    'key2': {'dict1': 'val1', 'dict2': 'val2'}
}

travel_log = {
    "France" : ["Paris", "Lille", "Dijion"],
    "Germany" : ["Stuttgart", "Berlin"]
}

print(travel_log['France'][1])

# 2D list
nested_list = ['A', 'B', ['C', 'D']]
print(nested_list[2][1])

travel_log = {
    "France" : {
        'no_of_times_visited' : 8,
        'cities' : ["Paris", "Lille", "Dijion"]
    },
    "Germany" : ["Stuttgart", "Berlin"]
}
print(travel_log)
print(travel_log['France'])
print(travel_log['France']['no_of_times_visited'])
print(travel_log['France']['cities'])