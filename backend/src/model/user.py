from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    fullname: str
    email: EmailStr


class UserRegister(BaseModel):
    fullname: str
    email: EmailStr
    password1: str
    password2: str


class UserLogin(BaseModel):
    id: int
    email: EmailStr
    password: str
