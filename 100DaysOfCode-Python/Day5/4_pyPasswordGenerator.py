import random

print("Welcome to the PyPassword Generator!")

# Data:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+', '(', ')']

no_of_letters = int(input("How many letters would you like in your password? "))
no_of_symbols = int(input("How many symbols would you like in your password? "))
no_of_numbers = int(input("How many numbers would you like in your password? "))

password = ""
# i think i should merge whole list of letters, symbols and numbers and then generate random elements from them.
data_set = letters + symbols + numbers
# + here doing concatenation of lists. we can also use extend() method to merge two lists.
# extend does the same thing but does in place and returns None. + creates a new list and returns it.

no_of_characters = no_of_letters + no_of_symbols + no_of_numbers

for i in range(no_of_characters):
    password += random.choice(data_set)

print(f"Your password is: {password}")


# We can also shuffle the password to make it more secure. we can use random.shuffle() method to shuffle the password.
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list) # join() method is used to join the elements of a list into a string. we can use any string as a separator. here we are using an empty string as a separator to join the characters of the password.
print(f"Your shuffled password is: {password}")

# There is one another way to generate a password.
# Simply go serial wise and add those random char to list and then shuffle it.


