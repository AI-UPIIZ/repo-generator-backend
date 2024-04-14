from fastapi import APIRouter
from app.api.routes import create

from app.core.config import API_PREFIX

api_router = APIRouter()

api_router.include_router(create.router, tags=['create'], prefix=API_PREFIX)
