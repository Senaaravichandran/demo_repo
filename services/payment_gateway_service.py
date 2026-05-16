from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PaymentRequest(BaseModel):
    amount: float
    currency: str
    payment_method: str
    user_id: int

class PaymentResponse(BaseModel):
    transaction_id: str
    status: str
    timestamp: datetime

class PaymentGatewayService:
    def __init__(self):
        pass

    def process_payment(self, payment_request: PaymentRequest) -> PaymentResponse:
        """
        Process a payment request and return a payment response.

        Args:
        - payment_request (PaymentRequest): The payment request to process.

        Returns:
        - PaymentResponse: The payment response.
        """
        # Simulate payment processing (replace with actual payment gateway logic)
        transaction_id = f"TXN-{payment_request.user_id}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        status = "success"

        # Return the payment response
        return PaymentResponse(
            transaction_id=transaction_id,
            status=status,
            timestamp=datetime.now()
        )