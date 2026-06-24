from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import os

from app.database import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse
from app.controllers.product_controller import ProductController

router = APIRouter(prefix="/products", tags=["Products"])

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "..", "templates"))


@router.post("", response_model=ProductResponse)
def create(data: ProductCreate, db: Session = Depends(get_db)):
    controller = ProductController(db)
    return controller.create(data)


@router.get("", response_model=list[ProductResponse])
def get_all(db: Session = Depends(get_db)):
    controller = ProductController(db)
    return controller.get_all()


@router.get("/{product_id}", response_model=ProductResponse)
def get_by_id(product_id: int, db: Session = Depends(get_db)):
    controller = ProductController(db)
    return controller.get_by_id(product_id)


@router.get("/{product_id}/detail", response_class=HTMLResponse)
def product_detail(request: Request, product_id: int, username: str = "", user_type: str = "", db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return HTMLResponse("Product not found", status_code=404)
    return templates.TemplateResponse(request, "product_detail.html", {"product": product, "username": username, "user_type": user_type})
