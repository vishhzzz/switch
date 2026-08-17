# Dictionary 
# key-value pair
# Understand it as a table with key as LHS entry and value as RHS entry.

singleEleDict = {'key': 'value'}

multiEleDict = {'key1': 'value1',
                'key2': 'value2'}

# accessing element of dictionary.
# same as list but here we provide key name instead of index.
print(singleEleDict['key'])
print(type(singleEleDict))
print(type(singleEleDict['key']))

# adding new entry
multiEleDict["key3"] = "value3"
print(multiEleDict)

# empty dictionary
emptyDict = {}

# wipe an existing dictionary
emptyDict['key1'] = 'val1'
print(emptyDict)
# emptyDict.clear()
# print(emptyDict)
# or we can do this
emptyDict = {}
print(emptyDict)

# modifying content of dict
modifyDict = {'key': 'val1'}
print(modifyDict)
modifyDict['key'] = 'val'
print(modifyDict)

for thing in modifyDict:
    # will print key
    print(thing)
    # will print value
    print(modifyDict[thing])