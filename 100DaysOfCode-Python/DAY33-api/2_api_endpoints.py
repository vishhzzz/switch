'''
API Endpoints: one of the imp. aspect of API is an API Endpoint.

in laymen terms, endpoint is just a location, we want data from a particular ext. service, then we must know the locn. where it is stored.

endpoint usually is a URL.

apart from API endpoint, we have api requests <- the request we make to internet for getting out task done.

Here, we will learn API via using api of International Space Station Current Location.

'''

# in order to work with api we need a module which does not come pre-installed ---> requests

import requests

# .get() helps us to get the data from endpoint
response = requests.get('http://api.open-notify.org/iss-now.json') 

print(response) # we get 200 <--- response code
# response code is more likely the status of our process i.e., is it successfully completed or was there any issue or has it failed... Something like that....