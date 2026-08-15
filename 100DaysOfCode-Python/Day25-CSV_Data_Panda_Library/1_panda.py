# its super-powerfull and super-userfull to work upon tabular data.
# is used majorily in Data Analysis.
import pandas
# reading csv file
# requires various arg but only path is non-optional rest r optional.
data = pandas.read_csv("./Day25-CSV_Data_Panda_Library/weather_data.csv")
print(type(data)) #panda.dataframe object
print(data) #data is shown in form of beautifull table

# we can get to indidual colum or row very easily
print(type(data['temp']))
print(data['temp'])

