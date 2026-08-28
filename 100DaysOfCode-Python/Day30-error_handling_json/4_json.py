'''
We will convert our data storage from raw to JSON

JSON: Java Script Object Notation

most popular way of transferring data mainly across internet.

JSON is simply a bunch of nested lists and dictionaries.

To work with JSON data in Python, we have an inbuilt library
json.dump() <--- write
json.load() <--- read
json.update() <--- update
'''

from tkinter import * 
from tkinter import messagebox
import random
import pyperclip
import json

#  ------------------------------ CONSTANTS ----------------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# --------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # List Comprehension
    password_list = [random.choice(LETTERS) for ele in range(nr_letters)]
    password_list += [random.choice(SYMBOLS) for ele in range(nr_symbols)]
    password_list += [random.choice(NUMBERS) for ele in range(nr_numbers)]

    random.shuffle(password_list)

    password = ''.join(password_list)

    print(f"Your password is: {password}")

    # fill the password input.
    password_input.insert(0, password)

    # making it available for clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# clear labels
def clear_data_field():
    website_input.delete(0, END)
    password_input.delete(0, END)

def add_password():
    # Label -> .cget()
    # Input -> .get()
    # get me the current value of text property of website label.
    website_data = website_input.get()
    email_data = email_username_input.get()
    password_data = password_input.get()

    # json.dump needs a dictionary as a args 
    data_json = {
        website_data: {
            'username': email_data,
            'password': password_data,
        }
    }

    # we should not ask for user confirmation without validating user entries
    if website_data == '' or password_data == '':
    # if len(website_data) == 0: both above and this r perfectly fine.
        messagebox.showerror(title='Oops !!!', message="Looks like u let some fields empty, \nPlease don't leave any field empty")
    else:
        data = data_json
        try:
            with open("./DAY30-error_handling_json/store_info.json", 'r') as file:
                # json.dump(dictionary, file)
                # json.dump(data_json, file) this is not human readable 
                # json.dump(data_json, file, indent=4)

                # to read or load json data.
                # json.load(file_path)
                # load simply reads the json data and convert it to dictionary.
                # data = json.load(file) 
                # print(data)

                # load the data
                data = json.load(file)
                # update the json with new data
                data.update(data_json)
        except FileNotFoundError:
            print("File is not present.\n")
        finally:
            with open("./DAY30-error_handling_json/store_info.json", 'w') as file:
                # write json data
                json.dump(data, file, indent=4)

            # we also need to clear all field data.
            clear_data_field()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.minsize(width=300, height=300)

# e and ew
'''
by default each widget lies in middle of row/column space.
for even layout, we need to specify the widget to stretch to get all the available space.
e: east - right
w: west - left
ew: stretch from left to right.
e: put widget against right side of cell
'''


# canvas
password_image_canvas = Canvas(width=200, height=200)
img_path = PhotoImage(file='./DAY29-Password_Manager/logo.png')
password_image_canvas.create_image(100, 100, image=img_path)
password_image_canvas.grid(row=0, column=1)

# labels
website = Label(text='Website:')
website.grid(row=1, column=0, sticky="e")

email_username = Label(text='Email/Username:')
email_username.grid(row=2, column=0, sticky="e")

password = Label(text='Password:')
password.grid(row=3, column=0, sticky="e")

# inputs
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="ew")
website_input.focus() #so that as soon as user opens the app, cursor should be at this field.

email_username_input = Entry(width=35)
email_username_input.grid(row=2, column=1, columnspan=2, sticky="ew")
# insert(index, str)
# index is the position where u wanna insert the text, 0 means very begining
# we also have END whcih means at the very end of the text, insert this text
# text is what u wanna insert
email_username_input.insert(0, "vishal.kr5202@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="ew")

# buttons
gen_pass = Button(text='Generate Password', width=14, command=pass_gen)
gen_pass.grid(row=3, column=2, sticky="ew")

add = Button(text='Add', width=36, command=add_password)
add.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
