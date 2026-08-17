import pandas
nato_data_frame = pandas.read_csv("./DAY26-comprehension/Project/nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_dict = {
    row.letter:row.code for (index, row) in nato_data_frame.iterrows()
}
# both r dict, but first one's representation is clean, clear and sober.
print(nato_dict)
print("=================================\n\n")
print(nato_data_frame.to_dict())


#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ") #vish
word_list = [value for (key, value) in nato_dict.items() if key.lower() in list(word)]
print(word_list)
print("============================\n\n")
# word_list = [nato_dict[ele.upper()] for ele in list(word) if ele.upper() in nato_dict] #last if condition is not necessary becoz we r sure that it will exist in dict.
word_list = [nato_dict[ele.upper()] for ele in list(word)]
print(word_list)
print(nato_dict.items())