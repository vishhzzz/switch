# we will not create a Table, but we will create models which represents Table.

from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Post(Base):
    __tablename__ =  "posts" #Table Name

    # define columns
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    # this line with default = True will not give us what we want, we have to use another param.
    # published = Column(Boolean, default=True)
    # will actually make default to TRUE
    published = Column(Boolean, server_default='TRUE', nullable=False)
    # add timestamp later...
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

