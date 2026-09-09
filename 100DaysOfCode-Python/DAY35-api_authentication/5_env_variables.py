'''
env - environment variables

this consists of various pairs in form of key-value, those r set in env in which our code runs.

Usage:
1. Convinience  : we can change code part without even touching the code and simply changing the env variables.
                eg: like we have made an application for sending mail but mail id of receiver changes day to day then we can directly change the mail id from env rather than code.

2. Security     : we tend to upload our software somewhere and its not a good idea to store api keys or auth keys to store in same place as them. We store them inside env variables.

We can tap into env keys via os module.
'''

# we dont actually need full data, we just need 1st 4 data/predictions which covers for 12 hrs.

# so we can limit ourself with just enough data. 

# there is a param called cnt, to achieve this.

import requests
import os

API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = os.environ.get('OWM_API_KEY')
LAT  = 28.457523
LONG = 77.026344
print(API_KEY)
parameters = {
    'lat': LAT,
    'lon': LONG,
    'appid': API_KEY,
    'cnt': 4,
}

response = requests.get(
    API_ENDPOINT, params=parameters
)

# handling any other response code
response.raise_for_status()

print(response.json()['cod'])
for dictt in response.json()['list']:
    weather=dictt['weather']
    id = weather[0]['id']
    if id < 700:
        print("Bring an Umbrella.\n")
