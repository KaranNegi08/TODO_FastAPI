from pydantic import BaseModel, EmailStr,Field

class UserRegister(BaseModel):
    id:int
    user_name:str=Field(... ,min_length= 3, max_length = 60)
    user_email:EmailStr
    user_password:str = Field(... , min_length=6, max_length=50)


class UserLogin(BaseModel):
    user_email:EmailStr
    user_password:str = Field(... , min_length=6)

class TokenResponse(BaseModel):
    access_token:str
    token_type:str