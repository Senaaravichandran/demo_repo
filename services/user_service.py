``` ```python
from typing import List
from models import User
from services.payment_service import get_payment_history

def get_user_payments(user_id: int) -> List[dict]:
    """
    Retrieves payment history for a given user.

    Args:
    - user_id (int): The ID of the user.

    Returns:
    - A list of dictionaries containing payment information.
    """
    # Retrieve the user object
    user = User(id=user_id)

    # Get payment history using the payment service
    payment_history = get_payment_history(user_id)

    return payment_history