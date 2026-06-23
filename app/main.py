from fastapi import FastAPI

from app.database import engine, Base
from app.routes.base import router as base_router
from app.routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Food System API", version="1.0.0")

app.include_router(base_router)
app.include_router(auth_router)
