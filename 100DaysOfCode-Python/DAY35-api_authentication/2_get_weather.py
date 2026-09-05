import requests

API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = '51146d3d129213a9bb592487b8e8831e'
LAT  = 28.457523
LONG = 77.026344

parameters = {
    'lat': LAT,
    'lon': LONG,
    'appid': API_KEY
}

response = requests.get(
    API_ENDPOINT, params=parameters
)

print(response.json()['cod'])
for dictt in response.json()['list']:
    weather=dictt['weather']
    id = weather[0]['id']
    desc = weather[0]['description']
    print(id, desc)
    print("\n")