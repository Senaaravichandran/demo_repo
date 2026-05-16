from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    email: str
    username: str
    tier: str = "free"
    created_at: datetime
    payment_method: Optional[str] = None
    payment_status: Optional[str] = None
    last_payment_date: Optional[datetime] = None

class Payment(BaseModel):
    id: int
    user_id: int
    amount: float
    currency: str = "USD"
    status: str
    created_at: datetime