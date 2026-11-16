from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:vishal@localhost:5432/postsDb"

# engine is the 1 solely responsible for communicating with DB.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# for actual talking with DB, we need a session
SessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)

Base = declarative_base() #creates a parent class for all your table models.

# dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()