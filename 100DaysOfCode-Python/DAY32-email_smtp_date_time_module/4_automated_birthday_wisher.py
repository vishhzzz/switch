##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


'''
either make 3 constants and put it inside a list and choose 1 out of them randomly
WISHER_LETTER_1 = "./DAY32-email_smtp_date_time_module/letter_templates/letter_1.txt"
WISHER_LETTER_2 = "./DAY32-email_smtp_date_time_module/letter_templates/letter_2.txt"
WISHER_LETTER_3 = "./DAY32-email_smtp_date_time_module/letter_templates/letter_3.txt"
'''

# ----------------------------------- Imports ---------------------------------- #
import random
import os
import smtplib
import datetime as dt
import pandas

# ------------------------------- CONSTANTS ------------------------------------ #
# or simply use random + os module for same
WISHER_LETTER_PATH = "./DAY32-email_smtp_date_time_module/letter_templates/"
CSV_FILE_PATH = "./DAY32-email_smtp_date_time_module/birthdays.csv"
SMTP_SERVER_ADD = "smtp.gmail.com"

# ----------------------------- Sending Mail ----------------------------------- #
def send_mail(receiver_mail, content):
    my_email = 'arjun.codes2402@gmail.com'
    my_pass = 'jrdl vtmh vegd tiwz'

    with smtplib.SMTP(SMTP_SERVER_ADD) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs=receiver_mail, msg=f"Subject: Birthday Wishes\n\n{content}")

month = dt.datetime.now().month
day = dt.datetime.now().day

data = pandas.read_csv(CSV_FILE_PATH)

# getting row based on columns
row = data[(data['month'] == 8) & (data['day'] == 30)]

# mail
my_email = row['email'].iloc[0]
print(my_email)

# name
name = row['name'].iloc[0]
print(name)

# choosing templates
files = os.listdir(WISHER_LETTER_PATH)
file = random.choice(files)
file_path = os.path.join(WISHER_LETTER_PATH, file)
print(file_path)

# replacing name in file
with open(file_path, "r+") as file:
    content = file.read()

    content = content.replace('[NAME]', name)

    # i dont need to re-write to file, i has the content and can simply send this to user, also my wishing template remains un-touched.
    # file.seek(0)
    # file.write(named_content)
    # file.seek(0)
    # content = file.read()

# send mail
send_mail(my_email, content)