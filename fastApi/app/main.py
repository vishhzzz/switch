# Updating individual post.


from fastapi import FastAPI, Response, status, HTTPException 
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

# acting DB
my_posts = [{'title': "title1", 'content': "content1", 'id': 1}, {'title': "title2", 'content': "content2", 'id': 2}]

@app.get("/")
async def root():
    '''
    Hello World.
    '''
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    '''
    Retrieving Posts.
    '''
    return {'post': my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def creating_post(posts: Post):
    '''
    Create Posts.
    '''
    posts_dict = posts.dict()
    posts_dict['id'] = randrange(1, 10000000)
    my_posts.append(posts_dict)
    return {"data": posts_dict}

@app.get("/posts/{id}")
def get_post(id:int, response:Response): 
    '''
    Retrieving Individual Post
    '''
    for dic in my_posts:
        if dic['id'] == id:
            return {'post': dic}

    raise HTTPException(status.HTTP_404_NOT_FOUND, f"post with id {id} is not present.")

@app.delete("/del_post/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id:int, response:Response):
    '''
    Deleting Individual Post
    '''
    for dic in my_posts:
        if dic['id'] == id:
            my_posts.remove(dic) #delete that id wali post
            # return {"posts": my_posts} - We should not sending any kind of data when we r sending 204.
            return Response(status_code=status.HTTP_204_NO_CONTENT) 

    # no matching id
    raise HTTPException(status.HTTP_404_NOT_FOUND, f"No post with id {id} found!!!")

@app.put("/post/{id}")
def update_post(id:int, post:Post):
    '''
    Updating Post
    '''
    for idx, dic in enumerate(my_posts):
        if dic['id'] == id:
            my_posts[idx] = post.dict()
            return {'message': post}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)