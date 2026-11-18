# DB Integration

from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body #take out content from body.
from typing import Optional
from random import randrange
import psycopg
import time
from app.database import engine, SessionLocal, get_db
from app import models
from sqlalchemy.orm import Session
from app.schemas import PostCreate

# NOTE: if i do something like this -- import app.database.engine
# then it creates a variable called app in my file which points to the package
# Later app = FastAPI() overwrites it.

models.Base.metadata.create_all(bind=engine) # Create every table defined in my models in the DB, if it doesn't already exists.
# models ---> models.py file
# .Base  ---> the Base class from database.py, which models.py imported.
# .metadata ---> registry inside Base that records every class inheriting from it.
# .create_all(...) ---> Turns everything in that registry into CREATE TABLE SQL and runs it.
# bind=engine ---> whcih DB to run it on.

# create_all ---> creates the table only if its not already been created.

# here dot simply represents the file go through i.e., go inside models and get Base and so on...

# we need to pass a path param in path operations or api endpoints.
# Session = Depends(get_db) --> will create dependency.
# going to create session for us to our DB, we can perform some operations and then close it once the request is done.

# As it is a path param embedded in path operations, we can repeat that process for every single one of our path operations.

app = FastAPI()

# have moved Pydantic/Schema model to a seperate file.

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
def get_posts(db: Session = Depends(get_db)):
    '''
    Retrieving Posts.
    '''
    # RAW SQL
    # cur.execute("""SELECT * FROM posts""") #execute returns the cursor itself, so no need to store it in posts.
    # #print(posts) #this will not print what we want, we need to use dedicated functions which shows the rows.
    # posts = cur.fetchall()
    
    # ORM
    posts = db.query(models.Post).all()
    print(posts)
    return {'post': posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def creating_post(posts: PostCreate, db: Session = Depends(get_db)):
    '''
    Create Posts.
    '''
    # this was without DB
    # posts_dict = posts.dict()
    # posts_dict['id'] = randrange(1, 10000000)
    # my_posts.append(posts_dict)

    # with DB - RAW SQL
    # cur.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (posts.title, posts.content, posts.published))

    # new_post = cur.fetchone()

    # # still this post will not be saved inside the db, we need to run one more command i.e., commit.
    # conn.commit()

    # ORM
    # assigning individually is little ineffecient
    # new_post = models.Post(title = posts.title, content = posts.content, published = posts.published)

    # posts.dict()
    # → {'title': 'Hello', 'content': 'World', 'published': True, 'rating': None}
    #models.Post(**{'title': 'Hello', 'content': 'World', 'published': True})

    # ** dictionary ko kholke har key-value ko key=value ki tarah function mein bhej deta ha
    
    # # Python isko internally aise padhta hai 👇
    # models.Post(title='Hello', content='World', published=True)

    new_post = models.Post(**posts.dict()) #this will unpack and do the same.
    db.add(new_post) # add this entry to DB
    db.commit() # commit into DB
    db.refresh(new_post) #get back the created post, store it into new_post.

    return {"data": new_post}

@app.get("/posts/{id}")
def get_post(id:int, response:Response, db: Session = Depends(get_db)): 
    '''
    Retrieving Individual Post
    '''
    # without DB
    # for dic in my_posts:
    #     if dic['id'] == id:
    #         return {'post': dic}

    # raise HTTPException(status.HTTP_404_NOT_FOUND, f"post with id {id} is not present.")

    # with DB - Raw SQL
    # cur.execute("""SELECT * FROM posts WHERE id = %s""", (id,)) #it needs tuple and rejects plain string.
    # post = cur.fetchone()
    
    # ORM
    post = db.query(models.Post).filter(models.Post.id == id).first() #filter is same as WHERE
    # we can either do one or first.
    # one -> returns the row if found and if its not found then raises the exception - NoResultFound
    # if multiple found --> raises MultipleResultsFound
    # first -> returns the row if found and if not found then returns NONE.
    # if multiple found --> returns the 1st row
    # There is also one more option here: we can use one_or_none()
    # one_or_none -> returns the row if found and if not found then returns NONE.
    # if multiple found --> raises MultipleResultsFound


    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"post with id {id} is not present.")
    
    return {"post_detail": post}


@app.delete("/del_post/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id:int, response:Response, db: Session = Depends(get_db)):
    '''
    Deleting Individual Post
    '''

    # RAW SQL
    # cur.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (id, ))
    # deleted_post = cur.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id)

    # we need post query now and will perform certain operations later
    # right now, no query has been executed, it is .first or .one which will execute the query.
    if post.first() is None: #will check the very 1st occurence of the received results.
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"No post with id {id} found!!!")

    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# NOTE db - session ki ek apni choti si memory hoti h, jb jb hm DB s koi post laate h, session uski ek copy apne paas rkh leta h post= db.query(models.Post).filter(models.Post.id == 5).first()
# ab hmare ps do jgh post 5 h, i. DB - asli wala, ii. Session ki memory m - copy

# PROBLEM
# Whenever we do 'query.delete', ORM just simply sends DELETE command to DB without conveying this to SESSION and hence uske paas jo copy hoti h usme update hi ni ho pata.

# SYNCHRONIZE_SESSION
# memory ka kya krna h???   ---   delete k baad session ki memory ko update krna h ya ni aur kaise.
# synchronize_session=False  ---> Memory ko chodo, kuch mt kro, very fast
# synchronize_session=evaluate ---> Memory m jo bhi objects h, unpr Python m hi WHERE condition check kro aur matching wale hta do 
# synchronize_session=fetch ---> Pehle DB s pucho kon kon s rows delete hue h and exactly whi session s hta do.
# synchronize_session=auto ---> first try evaluate and then try fetch :::: default in sqlalchemy 2.0

# Here in my case, i have used 'synchronize_session=False' becauze my get_db creates a new session for each request, and will close that session upon request completion.
# We r not reading or using again after runing delete, simply returning. Now even if memory contains wrong info its not of any use.
# It would have been an issue if after deleting, on that request only i am using that post only.


# DELETE - 2 ways
# 1. query s delete -- jo upr kr rhe h
# 2. object s delete 
# post = db.query(models.Post).filter(models.Post.id == id).first()
# db.delete(post) ---> now we r informing session about delete.


@app.put("/post/{id}")
def update_post(id:int, post:PostCreate, db: Session=Depends(get_db)):
    '''
    Updating Post
    '''
    # cur.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, id,))
    # updated_post = cur.fetchone()
    # conn.commit()

    updated_post = db.query(models.Post).filter(models.Post.id == id)

    updated_post_first = updated_post.first()

    if not updated_post_first:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found.")

    # pass items as dictionary
    # updated_post.update({'title': '6th post', 'content': 'This is my 6th post.'}, synchronize_session=False)
    # or
    updated_post.update(post.dict(), synchronize_session=False)

    db.commit()

    # return {'message': 'successfulllll'}
    # or
    return {'message': updated_post.first()}

# just a demo route.
@app.get('/sqlalchemy')
def test_posts(db: Session = Depends(get_db)):
    # will use query method in order to get to the relevant table
    all_posts = db.query(models.Post).all() # as right now it is for test purpose, we need to see whole table (all rows), we'll use all
    return {"data": all_posts}

# NOTE how simple it is  - just get hold of db which knows about creating session, then tap into query method, specify which table/model in terms of python. and then specify the type of action u need to perform.
# This query object just performing SQL. It abstracts all the SQL away.