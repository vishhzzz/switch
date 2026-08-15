# We will deep dive into 2 of the most popular data structures of PANDAS.

# Series : 1D data : column.
# DataFrame : 2D data : table or matrix.

# we have a dict method available
# converts data to a dict with column head as key and rest of column as value.

import pandas

data = pandas.read_csv("./Day25-CSV_Data_Panda_Library/weather_data.csv")

print(type(data)) #panda.dataframe object
print(data) #data is shown in form of beautifull table

# getting hold of a single column of table or a single column.
print(data['temp']) #treating data as dictionary

# lets convert it to a dictionary.
print(data.to_dict())

# convert individual series to list.
print(data['temp'].to_list())
print(type(data['temp'].to_list()))

# lets find out the average of temperature in this table.

# either this - TRADITIONAL way
temperatures = data['temp'].to_list()

average_temp = sum(temperatures) / len(temperatures)
print(f"Average Temperature here is: {average_temp:.2f}")

# or Library way
print(f"Average Temperature here is: {data['temp'].mean()}")

# getting max value
print(f"Maximum value of Temperature here is: {data['temp'].max()}")

# get hold of columns
print(data.condition) #treating data as object.
print(data.temp)
print(data.day)

# The fact that this works is bts PANDA has took these columns and converted those headings as its attributes.


# getting hold of Row values
# inside data table go to day column and print which row is Monday
print(data[data['day'] == 'Monday'])
print(data[data.day == 'Monday'])

# print row data where highest temp is present.
print(data[data.temp == data.temp.max()])

# data[...] <- column
# data[<exp>] <- row : we filter on some basis

# get hold of row's particular data
print(data[data.temp == data.temp.max()].temp)
print(data[data.temp == data.temp.max()].condition)
print(data[data.temp == data.temp.max()].day)

# monday's temp but in Farenheit
monday = data[data.day == 'Monday']
monday_temp = monday.temp * 9/5 + 32
print(monday)
print(monday_temp)


# generating DataFrame from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
print(data_dict)

# convert this into dataframe.
ele = pandas.DataFrame(data_dict)
print(ele)
print(type(ele))

# we can even save our data to a csv file.
ele.to_csv("./Day25-CSV_Data_Panda_Library/student_data.csv")
