# api1/routers/api1_router.py

from fastapi import APIRouter
from api1_service import get_api1_message

router = APIRouter()

@router.get("/hi")
def read_api1():
    return get_api1_message()
