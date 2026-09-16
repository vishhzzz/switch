'''
we have 4 types of requests:
1. Get      -   requests.get()
2. Post     -   requests.post()
3. Put      -   requests.put()
4. Delete   -   requests.delete()

POST: we r only interested in sending data to xternal system rather than interested in response other than success or fail.

PUT: we just update a piece of data in the external service.

DELETE: delete a piece of data in ext. service.

'''

import requests

PIXILA_ENDPOINT = "https://pixe.la/v1/users"

USER_PARAMS = {
    "token": "vishalKumar", #here we r providing token from our side only.
    "username": "vkk123",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url= PIXILA_ENDPOINT, json=USER_PARAMS)
print(response.text) #we r not interested in status response.