'''
ToDo
I need to send a motivational quotes on the present day then change it to monday.
'''

import smtplib
import datetime as dt
import random

MY_EMAIL = "arjun.codes2402@gmail.com"
MY_PASSWORD = 'jrdl vtmh vegd tiwz'
SENDER_EMAIL = 'vishal.kr5202@gmail.com'

def get_quote():
    # open motivational quotes file
    with open("./DAY32-email_smtp_date_time_module/quotes.txt") as file:
        list_of_quotes = file.readlines()
    
        # obtain a quote from list of quotes
        return random.choice(list_of_quotes)

def send_motivational_quotes():

    quote = get_quote()

    # sending mail
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls() #secure connection
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=SENDER_EMAIL, msg=f"Subject:Motivational Quotes\n\n{quote}")

# first lets check today's day
weekday = dt.datetime.now().weekday()
if weekday == 0: #monday check
    send_motivational_quotes()