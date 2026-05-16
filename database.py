from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Database connection URL
SQLALCHEMY_DATABASE_URL = "sqlite:///payment.db"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

class Payment(Base):
    __tablename__ = "payments"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    payment_method = Column(String, index=True)
    payment_date = Column(DateTime, default=datetime.utcnow)
    amount = Column(Float, index=True)

class PaymentModel(BaseModel):
    id: Optional[int]
    user_id: int
    payment_method: str
    payment_date: Optional[datetime]
    amount: float

    class Config:
        orm_mode = True

# Create all tables in the engine
Base.metadata.create_all(engine)