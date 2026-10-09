from fastapi import FastAPI
from fastapi.params import Body #take out content from body.
from pydantic import BaseModel  #creating API schema.
from typing import Optional

app = FastAPI()

# API schema - class
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"post": "This is your post."}

# POST request - creating post
@app.post("/create_post")
# def creating_post(payload: dict = Body(...)):
def creating_post(posts: Post):
    print(posts)
    print(posts.rating)
    print(type(posts), type(posts.dict()), posts.dict())
    return {"data": posts}

# ------------------------ New Day -------------------------- #
# CRUD - acronym - for 4 main functions of applications
# Create
# Read
# Update
# Delete

# for any app to be said as CRUD app, it should do following 4 things
# C -> Create - [POST]     - creating post in our case.
# R -> Read   - [GET]      - reading post either 1 post at a time or all the posts.
# U -> Update - [PUT/PATCH]- updating a post
# D -> Delete - [DELETE]   - deleting a post

# There r some conventions for naming:
# always use plural such as posts, users...

# in PUT ---  have to send each and every fields even if they r not required.
# in PATCH -- send only those fields which requires change.