# DB Integration

from fastapi import FastAPI, Response, status, HTTPException 
from fastapi.params import Body #take out content from body.
from pydantic import BaseModel  #creating API schema.
from typing import Optional
from random import randrange
import psycopg
import time

app = FastAPI()

# API schema - class
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

# we will do DB operations here and it is very likely that these operations may fail.
# Thus, using try catch for safer side.
while True:
    try:
        # connecting to DB via connect
        # right now, this is very bad practise for keeping things like this, we will use environment variable to store sensitive data perfectly.
        conn = psycopg.connect(host="localhost",
            dbname="fastapi",
            user='postgres',
            password='vishal',
        )

        # opening cursor to perform DB operations
        cur = conn.cursor()
        print("connecting to DB succeeded !!!")
        break

    except Exception as error:
        print(f"Connecting to DB failed, error: {error}")

        # before retrying, we would like to wait for few seconds.
        time.sleep(2) #will sleep for 2 seconds.


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
    cur.execute("""SELECT * FROM posts""") #execute returns the cursor itself, so no need to store it in posts.
    #print(posts) #this will not print what we want, we need to use dedicated functions which shows the rows.
    posts = cur.fetchall()
    print(posts)
    return {'post': posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def creating_post(posts: Post):
    '''
    Create Posts.
    '''
    # this was without DB
    # posts_dict = posts.dict()
    # posts_dict['id'] = randrange(1, 10000000)
    # my_posts.append(posts_dict)

    # with DB
    cur.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (posts.title, posts.content, posts.published))

    new_post = cur.fetchone()

    # still this post will not be saved inside the db, we need to run one more command i.e., commit.
    conn.commit()

    return {"data": new_post}

@app.get("/posts/{id}")
def get_post(id:int, response:Response): 
    '''
    Retrieving Individual Post
    '''
    # without DB
    # for dic in my_posts:
    #     if dic['id'] == id:
    #         return {'post': dic}

    # raise HTTPException(status.HTTP_404_NOT_FOUND, f"post with id {id} is not present.")

    # with DB
    cur.execute("""SELECT * FROM posts WHERE id = %s""", (id,)) #it needs tuple and rejects plain string.
    post = cur.fetchone()
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"post with id {id} is not present.")
    
    return {"post_detail": post}


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