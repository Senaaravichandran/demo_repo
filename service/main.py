``` ```python
from fastapi import HTTPException
from services.payment_service import PaymentService
from models import User

class PaymentErrorHandler:
    def __init__(self, payment_service: PaymentService):
        self.payment_service = payment_service

    def handle_payment_error(self, user: User, error_message: str):
        """
        Handle payment errors for premium users.

        Args:
        - user (User): The user who encountered the payment error.
        - error_message (str): The error message associated with the payment error.

        Raises:
        - HTTPException: If the user is not a premium user or if the payment error cannot be handled.
        """
        try:
            # Check if the user is a premium user
            if not self.payment_service.is_premium_user(user.id):
                raise HTTPException(status_code=403, detail="Only premium users can use this feature")

            # Log the payment error
            self.payment_service.log_payment_error(user.id, error_message)

            # Send a notification to the user about the payment error
            self.payment_service.send_payment_error_notification(user.id, error_message)

            # Return a success response
            return {"message": "Payment error handled successfully"}
        except Exception as e:
            # Raise an HTTP exception if the payment error cannot be handled
            raise HTTPException(status_code=500, detail=str(e))