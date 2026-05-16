from models import Payment, User
from typing import List
from datetime import datetime

class PaymentService:
    def __init__(self):
        self.payments = []

    def process_payment(self, user_id: int, amount: float) -> Payment:
        """Process a payment for a user."""
        payment = Payment(
            id=len(self.payments) + 1,
            user_id=user_id,
            amount=amount,
            currency="USD",
            status="pending",
            created_at=datetime.utcnow()
        )
        self.payments.append(payment)
        return payment

    def get_user_payments(self, user_id: int) -> List[Payment]:
        """Get all payments for a user."""
        return [p for p in self.payments if p.user_id == user_id]