import pandas
nato_data_frame = pandas.read_csv("./DAY26-comprehension/Project/nato_phonetic_alphabet.csv")

nato_dict = {
    row.letter:row.code for (index, row) in nato_data_frame.iterrows()
}

while True:
    word = input("Enter a word: ")
    try:
        word_list = [nato_dict[ele.upper()] for ele in word]
    except KeyError:
        print("Sorry, only letters in alphabet please!!!")
    else:
        break
print(word_list)
