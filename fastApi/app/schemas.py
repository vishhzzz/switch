from pydantic import BaseModel #creating API schema.

# API schema - class
# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     # rating: Optional[int] = None



# There are various way to create schema class
# 1. schemas for every operation - Create, Update.
# 2. We can also create one base model and then inherit into others.

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None

class PostCreate(PostBase):
    pass
# it simply means that we are inheriting everything from PostBase and have nothing of its own.