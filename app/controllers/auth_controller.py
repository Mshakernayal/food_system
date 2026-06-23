from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserLogin, UserResponse, Token
from app.services.auth_service import AuthService


class AuthController:

    def __init__(self, db: Session):
        self.service = AuthService(db)

    def register(self, user_data: UserCreate) -> UserResponse:
        try:
            user = self.service.register(user_data)
            return UserResponse.model_validate(user)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    def login(self, credentials: UserLogin) -> Token:
        try:
            result = self.service.login(credentials.username, credentials.password)
            return Token(**result)
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
