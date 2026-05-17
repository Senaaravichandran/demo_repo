``` ```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection URL
DATABASE_URL = "sqlite:///database.db"

# Create a database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    request_count = Column(Integer, default=0)

# Create all tables in the engine
Base.metadata.create_all(engine)

# Define a function to update the user's request count
def update_request_count(user_id: int):
    # Create a new session
    session = Session()
    
    # Query the user
    user = session.query(User).filter_by(id=user_id).first()
    
    # If the user exists, update their request count
    if user:
        user.request_count += 1
        session.commit()
    else:
        # If the user does not exist, create a new user
        new_user = User(id=user_id)
        session.add(new_user)
        session.commit()
        
    # Close the session
    session.close()

# Example usage:
# update_request_count(1)