from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.models.product import Product
import os

from app.database import get_db

router = APIRouter(tags=["Root"])

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "..", "templates"))


@router.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(request, "auth.html")


@router.get("/home", response_class=HTMLResponse)
def home(request: Request, username: str = "", user_type: str = "", db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return templates.TemplateResponse(request, "home.html", {"username": username, "user_type": user_type, "products": products})



