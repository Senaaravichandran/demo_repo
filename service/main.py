from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.encoders import jsonable_encoder
from services.auth_service import AuthService
from services.payment_service import PaymentService
from services.user_service import UserService
from models import User

app = FastAPI()

class FeatureRequest(BaseModel):
    feature_name: str
    description: str

class ServiceResponse(BaseModel):
    status: str
    message: str

def add_feature(feature_request: FeatureRequest) -> ServiceResponse:
    """
    This function adds a new feature to the system.
    
    Args:
    feature_request (FeatureRequest): The request containing the feature name and description.
    
    Returns:
    ServiceResponse: A response indicating the status of the operation.
    """
    
    # Validate the input
    if not feature_request.feature_name or not feature_request.description:
        raise HTTPException(status_code=400, detail="Invalid request")
    
    try:
        # Add the feature to the database
        # For this example, we'll assume we have a database connection
        # and a function to add a feature
        # add_feature_to_db(feature_request.feature_name, feature_request.description)
        
        # Return a success response
        return ServiceResponse(status="success", message="Feature added successfully")
    
    except Exception as e:
        # Log the error
        print(f"Error adding feature: {str(e)}")
        
        # Return a failure response
        return ServiceResponse(status="failure", message="Failed to add feature")

# Example usage
feature_request = FeatureRequest(feature_name="New Feature", description="This is a new feature")
response = add_feature(feature_request)

print(response)