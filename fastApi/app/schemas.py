from pydantic import BaseModel, EmailStr
 #creating API schema.

from datetime import datetime

# API schema - class
# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     # rating: Optional[int] = None



# There are various way to create schema class
# 1. schemas for every operation - Create, Update.
# 2. We can also create one base model and then inherit into others.


# hm ise aise isiliey bdl rhe h kyunki ab hm response ko bhi structure and systematic bnaenge isliey hm uska ek seperate model bnaenge and wo base s milta jhulta hoga.



class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None

class PostCreate(PostBase):
    pass
# it simply means that we are inheriting everything from PostBase and have nothing of its own.



# Pydantic Schema model ---> for tackling/controling Response
class PostResponse(PostBase):
    id: int

    # after defining a response schema, we can simply add one param inside route called response model.


    # we dont need to add -     

    # model_config = ConfigDict(from_attributes=True)
    # here because Fastapi jb response model s response validate krta h to khud s from_attributes=True lga deta h 
    # iska kaam kya h ?
    # simply tell Pydantic Model to read the data even if its not a dict., but an ORM model

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    email: EmailStr
    id: int
    created_at: datetime