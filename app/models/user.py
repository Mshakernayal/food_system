import enum

from sqlalchemy import Column, Integer, String, CheckConstraint

from app.database import Base


class UserType(str, enum.Enum):
    ADMIN = "admin"
    BUSINESS_OWNER = "business_owner"
    CLIENT = "client"


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    type = Column(String, nullable=False)

    __table_args__ = (
        CheckConstraint(type.in_([t.value for t in UserType]), name="check_user_type"),
    )
