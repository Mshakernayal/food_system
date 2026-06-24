from pydantic import BaseModel


class ProductCreate(BaseModel):
    image: str
    text: str
    description: str
    price: float
    rating: float


class ProductResponse(BaseModel):
    id: int
    image: str
    text: str
    description: str
    price: float
    rating: float

    model_config = {"from_attributes": True}
