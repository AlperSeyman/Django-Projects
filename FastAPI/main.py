import os
from dotenv import load_dotenv
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext


load_dotenv()

secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")
access_token_expire = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


fake_db = {
    "tesla":{
        "username":"tesla",
        "full_name": "Nikola Tesla",
        "email":"tesla@gmail.com",
        "hashed_password":"",
        "disabled":False
    }
}

# After a user logs in, the server will return a JWT token
class Token(BaseModel):
    
    access_token :str
    token_type: str

class TokenData(BaseModel):
    
    username: Optional[str] = None


class User(BaseModel):
    
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password:str

# Sets up password hashing using the bcrypt algorithm
# Used to hash new passwords and check existing ones.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Generate a hashed version of the provided password
def get_password_hash(password):
    
    return pwd_context.hash(password)

# Verify if the plain password matches the hashed password
def verify_password(plain_passwrod, hashed_password):
    
    return pwd_context.verify(plain_passwrod, hashed_password)


def get_user(db, username:str):
    
    if username in db:
        user_data = db[username]
        return UserInDB(**user_data)


def authenticate_user(db, username:str, password:str):
    
    user = get_user(fake_db, "tesla")
    if not user:
        return False

    if not verify_password(password, user.hashed_password):
        return False
    
    return user

def created_access_token(data: dict, expires_delta: Optional[timedelta]=None):
    
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm)
    return encoded_jwt

