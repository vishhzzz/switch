import requests
from datetime import datetime
import smtplib

MY_LAT = 28.704060 # Your latitude
MY_LONG = 77.102493 # Your longitude

def is_my_pos_with_in_range(lat, long):
    if MY_LAT - 5 <= lat <= MY_LAT + 5 and MY_LONG - 5 <= long <= MY_LONG + 5:
        return True
    return False

def is_it_dark_night(current_hour, sunset, sunrise):
    if current_hour >= sunset or current_hour <= sunrise:
        return True
    return False

def send_mail():

    my_email = "arjun.codes2402@gmail.com"
    password = 'jrdl vtmh vegd tiwz'

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='vishal.kr5202@gmail.com')

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

is_iss_current_to_my_pos = is_my_pos_with_in_range(iss_latitude, iss_longitude)

is_it_dark = is_it_dark_night(current_hour, sunset, sunrise)

if is_iss_current_to_my_pos and is_it_dark:
    send_mail()
else:
    print("Not up right now.")

# we can make code run every 60 sec by a simple trick
'''
while true:
    time.sleep(60)
    code block
'''