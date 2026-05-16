from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from services.user_service import UserService
from services.payment_service import PaymentService
from models import User
from typing import List

router = APIRouter()

@router.get("/users/")
async def read_users():
    """Get all users"""
    try:
        users = UserService().get_all_users()
        return JSONResponse(content={"users": users}, media_type="application/json")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/users/{user_id}")
async def read_user(user_id: int):
    """Get user by ID"""
    try:
        user = UserService().get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return JSONResponse(content={"user": user}, media_type="application/json")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/users/")
async def create_user(user: User):
    """Create a new user"""
    try:
        created_user = UserService().create_user(user)
        return JSONResponse(content={"user": created_user}, media_type="application/json", status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    """Update an existing user"""
    try:
        updated_user = UserService().update_user(user_id, user)
        if not updated_user:
            raise HTTPException(status_code=404, detail="User not found")
        return JSONResponse(content={"user": updated_user}, media_type="application/json")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    """Delete a user"""
    try:
        deleted_user = UserService().delete_user(user_id)
        if not deleted_user:
            raise HTTPException(status_code=404, detail="User not found")
        return JSONResponse(content={"message": "User deleted successfully"}, media_type="application/json")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/users/{user_id}/payments")
async def get_user_payments(user_id: int):
    """Get payments for a user"""
    try:
        payments = PaymentService().get_user_payments(user_id)
        return JSONResponse(content={"payments": payments}, media_type="application/json")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/users/{user_id}/payments")
async def create_user_payment(user_id: int, payment_amount: float):
    """Create a new payment for a user"""
    try:
        payment = PaymentService().create_user_payment(user_id, payment_amount)
        return JSONResponse(content={"payment": payment}, media_type="application/json", status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))