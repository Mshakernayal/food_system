from datetime import datetime

from pydantic import BaseModel


class BillItemRequest(BaseModel):
    product_id: int
    quantity: int


class BillCreateRequest(BaseModel):
    username: str
    items: list[BillItemRequest]


class BillDetailResponse(BaseModel):
    id: int
    product_id: int
    product_quantity: int
    bill_id: int

    model_config = {"from_attributes": True}


class BillResponse(BaseModel):
    id: int
    date: datetime
    total_price: float
    user_id: int

    model_config = {"from_attributes": True}
