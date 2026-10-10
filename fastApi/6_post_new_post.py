from fastapi import FastAPI
from fastapi.params import Body #take out content from body.
from pydantic import BaseModel  #creating API schema.
from typing import Optional
from random import randrange

app = FastAPI()

# API schema - class
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{'title': "title1", 'content': "content1", 'id': 1}, {'title': "title1", 'content': "content1", 'id': 2}]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    # return {"post": "This is your post."}
    # instead of this, we need to return the posts that we saved above.
    return {'post': my_posts} #it automatically serializes it into JSON.

@app.post("/posts")
# def creating_post(payload: dict = Body(...)):
def creating_post(posts: Post):
    # ui sends the data.
    # posts contains the data
    # we just had to add it to db, list in this case.
    # we usally return that newly added post to user.
    posts_dict = posts.dict()
    posts_dict['id'] = randrange(1, 10000000)
    my_posts.append(posts_dict)
    return {"data": posts_dict}