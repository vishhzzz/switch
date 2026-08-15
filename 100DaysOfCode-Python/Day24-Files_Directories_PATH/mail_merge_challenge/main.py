#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp

#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp

#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# i have to write code for automating mailing.

# 1st i should have list of names to whom mail needs to be send.
with open("./Day24-Files_Directories_PATH/mail_merge_challenge/Input/Names/invited_names.txt") as file:
    # content = file.read()
    # we will traverse line by line.

    # we can either do this 
    # for line in file:
    #     names.append(line.strip())

    # or
    names = file.readlines()

with open("./Day24-Files_Directories_PATH/mail_merge_challenge/Input/Letters/starting_letter.txt") as file:
    letter = file.read()

    for name in names:
        name = name.strip()
        with open(f"./Day24-Files_Directories_PATH/mail_merge_challenge/Output/ReadyToSend/letter_for_{name}.txt", 'w') as out_file:
            invite = letter.replace("[name]", name)
            out_file.write(invite)

