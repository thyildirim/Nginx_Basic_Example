# api2/routers/api2_router.py

from fastapi import APIRouter
from api2_service import get_api2_message

router = APIRouter()

@router.get("/hi")
def read_api2():
    return get_api2_message()
