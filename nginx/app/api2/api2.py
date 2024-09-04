# api2/main.py

from fastapi import FastAPI
from api2_router import router as api2_router

app = FastAPI()

app.include_router(api2_router)
