from pydantic import BaseModel, EmailStr

from app.models.user import UserType


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    type: UserType = UserType.CLIENT


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    type: UserType

    model_config = {"from_attributes": True}


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    username: str
    user_type: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
