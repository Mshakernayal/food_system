from sqlalchemy import Column, Integer, String, Text, Float

from app.database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String, nullable=False)
    text = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    rating = Column(Float, nullable=False)
