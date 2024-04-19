from fastapi import APIRouter
from app.api.routes import create

api_router = APIRouter()

api_router.include_router(create.router, tags=['create'])
