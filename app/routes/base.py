from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session, joinedload
from app.models.product import Product
from app.models.bill import Bill, BillDetail
from app.models.user import User
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


# base client operations

@router.get("/purchases/latest", response_class=HTMLResponse)
def latest_purchases(request: Request, username: str = "", user_type: str = "", db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    bills = []
    if user:
        bills = (db.query(Bill)
                 .options(joinedload(Bill.details).joinedload(BillDetail.product))
                 .filter(Bill.user_id == user.id)
                 .order_by(Bill.date.desc())
                 .all())
    return templates.TemplateResponse(request, "purchases.html", {"bills": bills, "username": username, "user_type": user_type})



