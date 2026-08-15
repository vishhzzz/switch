# create a csv called squirel count.csv
# containing Fur color and count

import pandas

squirel_data_set = pandas.read_csv("./Day25-CSV_Data_Panda_Library/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

count_cinnamon = squirel_data_set['Primary Fur Color'].count == 'Cinnamon'
count_gray = squirel_data_set['Primary Fur Color'].count == 'Gray'
count_black = squirel_data_set['Primary Fur Color'].count == 'Black'


# this is little futuristics
# fur_color_list = squirel_data_set['Primary Fur Color'].dropna().unique().tolist()
# fur_color_count = squirel_data_set['Primary Fur Color'].value_counts().tolist()


# stand with basics
fur_color_list = ['Cinnamon', 'Gray', 'Black']
cinnamon_squirel_color_count = len(squirel_data_set[squirel_data_set['Primary Fur Color'] == 'Cinnamon'])
gray_squirel_color_count = len(squirel_data_set[squirel_data_set['Primary Fur Color'] == 'Gray'])
black_squirel_color_count = len(squirel_data_set[squirel_data_set['Primary Fur Color'] == 'Black'])
fur_color_count = [cinnamon_squirel_color_count, gray_squirel_color_count, black_squirel_color_count]


squirel_dict = {
    'fur_color': fur_color_list,
    'count': fur_color_count
}

csv_data = pandas.DataFrame(squirel_dict)

# converting to a table or csv format
csv_data.to_csv("./Day25-CSV_Data_Panda_Library/squirel_data.csv")
print(csv_data)