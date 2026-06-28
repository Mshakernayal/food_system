from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password, verify_password, create_access_token


class AuthService:

    def __init__(self, db: Session):
        self.db = db

    def register(self, user_data: UserCreate) -> User:
        if self.db.query(User).filter(User.username == user_data.username).first():
            raise ValueError("Username already exists")
        if self.db.query(User).filter(User.email == user_data.email).first():
            raise ValueError("Email already exists")

        user = User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hash_password(user_data.password),
            type=user_data.type.value,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def login(self, username: str, password: str) -> dict:
        user = self.db.query(User).filter(User.username == username).first()
        
        if not user:
            raise ValueError("Username not found")
        if not verify_password(password, user.hashed_password):
            raise ValueError("Incorrect password")

        token = create_access_token(data={"sub": user.username})
        return {"access_token": token, "token_type": "bearer", "username": user.username, "user_type": user.type}
