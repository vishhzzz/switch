from fastapi import FastAPI
from fastapi.params import Body #take out content from body.
from pydantic import BaseModel  #creating API schema.
from typing import Optional

app = FastAPI()

# API schema - class
class Post(BaseModel): # special Pydantic Model - extending Base Model.
    # title, content --- datatype
    title: str
    content: str
    published: bool = True #default value it user doesn't provide published then it is true otherwise false.
    rating: Optional[int] = None #fully optional field, if user does not pass anything dont store anything.


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"post": "This is your post."}

# POST request - creating post
@app.post("/create_post")
# def creating_post(payload: dict = Body(...)):
def creating_post(posts: Post): #referencing Post Pydantic model and then save it in posts variable
    # As we r now using Pydantic Model, now FastApi will auto validate few things:
    # does requests/user data contains - title, content
    # is it string or not
    # otherwise will throw error
    print(posts) # posts contains all the data extracted from Post.
    print(posts.rating)
    print(type(posts), type(posts.dict()), posts.dict())
    return {"data": posts}
    # we can also individually use title/content via posts.title

# ------------------------ New Day -------------------------- #
# Q. Why current scheme sucks. and Why do we need Schema...
# -> Its pain to get all the values from body.
# -> Client can send any whatever data they want. [but i want only particular fields but client can send any data it want.]
# -> Data isn't getting validated. [suppose user sends me a blank title then there is no validation and hence there will be a post with blank title which we dont want.]
# -> We want to force user to send data in 1 particular format only -> schema - API Schema which is more likely a contract between frontend and backend which in simple terms tells that this is the format in which i expect data so send me in this way.

# PYDANTIC LIBRARY
# not associated with FastAPI, seperate library which u can use with any python app.
# we use it to define 'how our schema should look like'?

# currently, i want 2 things:
# title - str
# content - str
# i.e., user must send me these 2 and nothing else.
# published - bool <--- optional

# With help of Pydantic Model - frontend is sending us exact format of data as we want.
# we can also do the same for sending the data back to user via pydantic models.

# when we save pydantic model to a variable, posts: Post
# it gets saved in form of Pydantic Model and each pydantic model has a associated .dict with it to convert it to a dictionary.
