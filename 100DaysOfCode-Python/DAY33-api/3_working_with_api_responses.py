'''
Response Codes: Tells whether our requests succedded or failed.

[404] ---> thing u r looking for doesn't exists

Nomenclature:
[1xx] ---> hold on, something is going on, this is not final...
[2xx] ---> here u go, everything was successfull. [will get the data that u r expecting...]
[3xx] ---> u dont have any permission for that particular data, so go away...
[4xx] ---> u screwed up
[5xx] ---> i as in SERVER screwed up
'''

import requests

# .get() helps us to get the data from endpoint. ---> gives response object
response = requests.get('http://api.open-notify.org/iss-now.json') 


print(response)
print(type(response))

# we can directly go for response code from response object.
print(response.status_code)

'''
status code: 200 means success
             404 means not found
'''

'''
Request is the most famous module for working with API amoung Python devs.

Now, we have a lot of STATUS_CODES and we cant manually handle those in our code, so we have request model take care for us.
It will raise exception on behalf of us.
'''
response.raise_for_status() # <--- handle everything for us.

print(response.raise_for_status())
print(type(response.raise_for_status()))

'''
getting hold of actual data.
'''
print(response.json()['message'])
print(response.json()['timestamp'])
print(response.json()['iss_position']['latitude'])