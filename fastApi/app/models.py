# we will not create a Table, but we will create models which represents Table.

from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Post(Base):
    __tablename__ =  "posts" #Table Name

    # define columns
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)
    # add timestamp later...

    

