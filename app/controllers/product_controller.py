from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.product import ProductCreate, ProductResponse
from app.services.product_service import ProductService


class ProductController:

    def __init__(self, db: Session):
        self.service = ProductService(db)

    def create(self, data: ProductCreate) -> ProductResponse:
        product = self.service.create(data)
        return ProductResponse.model_validate(product)

    def get_all(self) -> list[ProductResponse]:
        products = self.service.get_all()
        return [ProductResponse.model_validate(p) for p in products]

    def get_by_id(self, product_id: int) -> ProductResponse:
        try:
            product = self.service.get_by_id(product_id)
            return ProductResponse.model_validate(product)
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))
