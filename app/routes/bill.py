from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers.bill_controller import BillController
from app.database import get_db
from app.schemas.bill import BillCreateRequest, BillResponse

router = APIRouter(prefix="/bills", tags=["Bills"])


@router.post("", response_model=BillResponse)
def create(data: BillCreateRequest, db: Session = Depends(get_db)):
    controller = BillController(db)
    return controller.create(data)
