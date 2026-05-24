from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from jose import JWTError
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

SECRET_KEY = "karan"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 40

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password:str, hash_password:str):
    return pwd_context.verify(plain_password, hash_password)

def create_access_token(data:dict):
    encode = data.copy()
    
    expire_time = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    encode.update({"exp":expire_time})

    encoded_jwt= jwt.encode(
        encode,
        SECRET_KEY,
        algorithm= ALGORITHM
    )
    return encoded_jwt


def verify_access_token(token:str):
    try:
        payload= jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        raise HTTPException(status_code= 401, detail="Invalid Token.")

    