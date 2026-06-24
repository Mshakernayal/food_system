from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate


class ProductService:

    def __init__(self, db: Session):
        self.db = db

    def create(self, data: ProductCreate) -> Product:
        product = Product(
            image=data.image,
            text=data.text,
            description=data.description,
        )
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def get_all(self) -> list[Product]:
        return self.db.query(Product).all()

    def get_by_id(self, product_id: int) -> Product:
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise ValueError("Product not found")
        return product
