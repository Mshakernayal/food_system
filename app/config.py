import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./food_system.db")
SECRET_KEY = os.getenv("SECRET_KEY", "4a1b9e2f8c3d6e")
ENCODING_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
