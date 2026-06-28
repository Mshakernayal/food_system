from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import engine, Base
from app.routes.base import router as base_router
from app.routes.auth import router as auth_router
from app.routes.product import router as product_router
from app.routes.bill import router as bill_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Food System API", version="1.0.0")

app.mount("/images", StaticFiles(directory="app/data/images"), name="images")

app.include_router(base_router)
app.include_router(auth_router)
app.include_router(product_router)
app.include_router(bill_router)
