from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')
# telling passlib about default hashing algo - which is bcrypt

def hash(password:str):
    return pwd_context.hash(password)