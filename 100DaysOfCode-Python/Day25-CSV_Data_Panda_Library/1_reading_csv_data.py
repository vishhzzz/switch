# we need to open csv file and then do some work

# opening csv file
with open("./Day25-CSV_Data_Panda_Library/weather_data.csv") as file:
    list_of_data = file.readlines()

# readlines() read each line and turn it into single item in a list.

# printing data
print(list_of_data)

# its still little painfull to work on this data.
# so we have panda to our rescue.....

# importing csv library
import csv 

with open("./Day25-CSV_Data_Panda_Library/weather_data.csv") as file:
    # reader is a function provided via CSV lib.
    # it takes a '.csv' file and gives an object ---> which is iterable but its not a list that lets u operate through the csv line by line i.e., row-by-row.
    content = csv.reader(file)
    # content is an object [CSV reader object] which will help me to iterate through the csv file row by row.
    # can also understand it as it gives list of columns in a better format unlike .read.
    print(content)
    # for item in content:
    #     # will print individual row
    #     # print(item)
    #     pass

    # actually we cant iterate through same reader object multiple times as on 1st parsing it moves to end.

    # we need to now extract temperature from content list.
    temperatures = []
    # see what i had done here is content is a reader object.
    # so first convert it to list
    # we dont need 0th element of list so we use slicing.
    for item in list(content)[1:]:
        temperatures.append(int(item[1]))

    print(temperatures)