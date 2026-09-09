# we dont actually need full data, we just need 1st 4 data/predictions which covers for 12 hrs.

# so we can limit ourself with just enough data. 

# there is a param called cnt, to achieve this.

import requests

API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = '51146d3d129213a9bb592487b8e8831e'
LAT  = 28.457523
LONG = 77.026344

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
