from fastapi import APIRouter, HTTPException
from services.payment_service import PaymentService
from models import Payment
from typing import List

router = APIRouter()
payment_service = PaymentService()

@router.post("/", response_model=Payment)
def create_payment(user_id: int, amount: float):
    """Create a new payment."""
    return payment_service.process_payment(user_id, amount)

@router.get("/{user_id}", response_model=List[Payment])
def get_payments(user_id: int):
    """Get all payments for a user."""
    return payment_service.get_user_payments(user_id)