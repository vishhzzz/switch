# uvicorn is the server - listens for web requests, passes them to fastapi app and sends the app's response back. Handles the network connection so requests can reach the app.

from fastapi import FastAPI

# app here is an instance of FastAPI.
app = FastAPI()

# we r defining what happens when someone visits '/'.
@app.get("/")
async def root():
    return {"message": "Hello World"} #message is Python's Dictionary and it is auto converted into JSON format.

# command to install uvicorn
# pip3 install uvicorn

# command to run this program
# uvicorn main:app --reload
# uvicorn - server
# main - python file
# app - object created by app = FastAPI()
# reload - restarts the server when u make changes in code.

# explaining each lines of code. ---- PATH OPERATIONS
# @app.get("/"). ----> decorator
# async def root(): ----> function / 'path operation' or route function | name must be as descriptive as possible.
    # return {"message": "Hello World"} ---> whatever we return from here is the Data that we sent back to user.

# Above lines r path operation as explained by FastAPI docs.
# also refered to as Route.

# async is needed only when u need to perform aynchronous task.

# without decorator, this works as a normal function.
# with decorator, works as API.
# Basically it converts this into a path operation/route so that who so ever wants to use our API can hit this endpoint.

# DECORATOR 
# @ -> decorator
# app -> fastapi instance
# http methods -> get/set/put/patch...
# path -> path or url endpoint where user will hit, its basically after the domain name or simply after the local host's ip.




# making another dummy path operation
@app.get("/posts")
def get_posts():
    return {"post": "This is your post."}


# FASTAPI --- DOCS 
# there is an interesting thing that u can witness
# when u add docs at the end of endpoint URL then it will take u to Interactive UI which is basically 'SWAGGER UI', thats an interactive docs of fastapi where u can try out diff http methods.
# Working:
# FastAPI does not manually build the Swagger page from your endpoints. It first generates an OpenAPI JSON schema from your Python code, and Swagger UI reads that schema and renders the interactive documentation.

# If there 2 same endpoints defined then?
# FastApi actually goes through all the routes and stops at the first match.
# So for 2 consecutive same endpoints - 1 first one wins.

# API - order does matters.
