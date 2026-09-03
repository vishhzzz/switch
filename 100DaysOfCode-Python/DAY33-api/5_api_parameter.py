'''
We can also pass inputs which r api parameters which later acts as inputs.

We can pass parameters with api directly to browser by simply adding ? at the end of api endpoint to specify browser we are adding param. 
The added param is in the form of key-value and we add more and more such params with &.
'''

import requests
import datetime

MY_LAT = 28.704060
MY_LONG = 77.102493

# if i normally run this without any parameters then it will raise exception as in order for this api to work, it needs some param.
# response = requests.get('https://api.sunrise-sunset.org/json')
# response.raise_for_status() -> right now will return STATUS_CODE: 400 --> bad request 

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}
response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
print(response.json())

sunrise = response.json()['results']['sunrise']
sunset = response.json()['results']['sunset']

print(sunrise)

print(sunrise.split('T')[1].split(':')[0])
print((sunrise.split('T')[1].split(':'))[0])

sunrise_hour = (sunrise.split('T')[1].split(':'))[0]
sunset_hour = (sunset.split('T')[1].split(':'))[0]
print(sunrise_hour)
print(sunset_hour)

current_time_hour = datetime.datetime.now().hour
print(current_time_hour)