from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from db import get_db
from models.user_model import User
from schemas.auth_schema import UserRegister,UserLogin, TokenResponse
from controllers.auth import hash_password, verify_password, verify_access_token ,create_access_token

router=APIRouter()

@router.post('/register')
def user_registration(user:UserRegister, db:Session = Depends(get_db)):
    existing_email= db.query(User).filter(user.user_email == User.email).first()

    if existing_email:
        raise HTTPException(status_code=400,detail="Email already exists.")
    existing_id = db.query(User).filter(user.id == User.id).first()

    if existing_id:
        raise HTTPException(status_code=400,detail="User ID already exists")

    new_user= User(
        id= user.id,
        username = user.user_name,
        email= user.user_email,
        hashed_password= hash_password(user.user_password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return JSONResponse(status_code= 200, content={"message":"User registered successfully."})

@router.post('/login')
def user_login(user:UserLogin, db:Session = Depends(get_db)):
    existing_user= db.query(User).filter(user.user_email == User.email ).first()
    if not existing_user:
        raise HTTPException(status_code=400,detail="User does not exists")
    
    valid_password = verify_password(user.user_password,existing_user.hashed_password)
    if not valid_password:
        raise HTTPException(status_code=401,detail="Invalid password.")

    access_token = create_access_token(
        data={"user_id": existing_user.id}
    )
    return {"access_token": access_token,"token_type": "bearer"}
        


    
