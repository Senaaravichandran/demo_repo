``` ```python
from fastapi import APIRouter, Depends
from services.database_service import DatabaseService
from models import User
from typing import List

router = APIRouter()

@router.get("/database")
async def get_database_info(database_service: DatabaseService = Depends()):
    users = await database_service.get_users()
    request_count = await database_service.get_request_count()
    subscription_type = await database_service.get_subscription_type()
    return {
        "users": users,
        "request_count": request_count,
        "subscription_type": subscription_type
    }