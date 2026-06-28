from sqlalchemy.orm import Session

from app.models.bill import Bill, BillDetail
from app.models.product import Product
from app.models.user import User


class BillService:

    def __init__(self, db: Session):
        self.db = db

    def create(self, username: str, items: list[dict]) -> Bill:
        user = self.db.query(User).filter(User.username == username).first()
        if not user:
            raise ValueError("User not found")

        total_price = 0.0
        for item in items:
            product = self.db.query(Product).filter(Product.id == item["product_id"]).first()
            if not product:
                raise ValueError(f"Product {item['product_id']} not found")
            total_price += product.price * item["quantity"]

        bill = Bill(total_price=total_price, user_id=user.id)
        self.db.add(bill)
        self.db.flush()

        for item in items:
            detail = BillDetail(
                product_id=item["product_id"],
                product_quantity=item["quantity"],
                bill_id=bill.id,
            )
            self.db.add(detail)

        self.db.commit()
        self.db.refresh(bill)
        return bill
