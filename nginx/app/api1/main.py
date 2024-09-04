# api1/main.py

from fastapi import FastAPI
from api1_router import router as api1_router

app = FastAPI()

app.include_router(api1_router)
