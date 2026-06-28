from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.bill import BillCreateRequest, BillResponse
from app.services.bill_service import BillService


class BillController:

    def __init__(self, db: Session):
        self.service = BillService(db)

    def create(self, data: BillCreateRequest) -> BillResponse:
        try:
            items = [{"product_id": i.product_id, "quantity": i.quantity} for i in data.items]
            bill = self.service.create(data.username, items)
            return BillResponse.model_validate(bill)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
