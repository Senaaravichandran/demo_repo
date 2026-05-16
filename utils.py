``` ```python
from typing import Dict, Any
from pydantic import BaseModel
from datetime import datetime

class PaymentRequest(BaseModel):
    """Payment request model"""
    amount: float
    currency: str
    payment_method: str
    payment_date: datetime

class PaymentResponse(BaseModel):
    """Payment response model"""
    status: str
    transaction_id: str
    payment_date: datetime

def validate_payment_request(request: Dict[str, Any]) -> bool:
    """
    Validate payment request data.

    Args:
    - request (Dict[str, Any]): Payment request data.

    Returns:
    - bool: True if the request is valid, False otherwise.
    """
    required_fields = ["amount", "currency", "payment_method"]
    for field in required_fields:
        if field not in request:
            return False
    return True

def process_payment(request: PaymentRequest) -> PaymentResponse:
    """
    Process payment request.

    Args:
    - request (PaymentRequest): Payment request data.

    Returns:
    - PaymentResponse: Payment response data.
    """
    # Simulate payment processing
    transaction_id = "PAY-1234567890"
    status = "success"
    payment_date = datetime.now()
    return PaymentResponse(status=status, transaction_id=transaction_id, payment_date=payment_date)

def get_payment_status(transaction_id: str) -> str:
    """
    Get payment status by transaction ID.

    Args:
    - transaction_id (str): Transaction ID.

    Returns:
    - str: Payment status.
    """
    # Simulate payment status retrieval
    return "success"