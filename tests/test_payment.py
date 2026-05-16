import pytest
from services.payment_service import PaymentService

def test_process_payment():
    service = PaymentService()
    payment = service.process_payment(user_id=1, amount=100.0)
    assert payment.amount == 100.0
    assert payment.status == "pending"

def test_get_user_payments():
    service = PaymentService()
    service.process_payment(user_id=1, amount=100.0)
    service.process_payment(user_id=1, amount=50.0)

    payments = service.get_user_payments(user_id=1)

    assert len(payments) == 2