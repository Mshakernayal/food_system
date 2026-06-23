from fastapi import APIRouter

router = APIRouter(tags=["Root"])


@router.get("/")
def root():
    return {"message": "Food System API is running"}
    