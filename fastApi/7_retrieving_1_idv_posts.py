# retrieving 1 individual post.

# NOTE: Ordering do matter in API routes's order. It matches every route as per the order they r created, so ordering is IMP. There may be cases when it goes to other routes instead of 1 which they r meant for. 
# Its more of an issue when u work with 'PATH PARAMETERS'.


from fastapi import FastAPI, Response, status, HTTPException #we will be sending 404 in case when id does not match, instead of by-default 200.
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

# When any thing is created via post req., it must send 201 status code.
# to do that,simply pass it to decorator.
@app.post("/posts", status_code=status.HTTP_201_CREATED)
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

@app.get("/posts/{id}") #id here is PATH param.
def get_post(id:int, response:Response): #if we want id of decorator to be used inside function, just use it as function's arg. Also passing it like int will invoke fastapi's auto-validation and will make sure that it is passed as int or atleast convertable to int.
    for dic in my_posts:
        if dic['id'] == id:
            return {'post': dic}
    # return "No Post Found!!!"
    # response.status_code = 404 #message can be anything, this only makes sure that response code that is sent is 404. 
    # we can also do this ---> here no hard coding
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {'message': "No Post Found!!!"}

    # we can simply raise an exception.
    raise HTTPException(status.HTTP_404_NOT_FOUND, f"post with id {id} is not present.") #its more professional and clean.