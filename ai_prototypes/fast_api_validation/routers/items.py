from fastapi import APIRouter
from schemas.items import ItemCreate

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/")
def create_item(item: ItemCreate):
    return {"item": item}
