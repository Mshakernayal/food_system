from datetime import datetime

from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.user import User
from app.models.product import Product


class Bill(Base):
    __tablename__ = "bill"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    total_price = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", backref="bills")
    details = relationship("BillDetail", backref="bill", cascade="all, delete-orphan")


class BillDetail(Base):
    __tablename__ = "bill_detail"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    product_quantity = Column(Integer, nullable=False)
    bill_id = Column(Integer, ForeignKey("bill.id"), nullable=False)

    product = relationship("Product", backref="bill_details")
