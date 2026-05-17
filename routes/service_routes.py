``` ```python
from fastapi import APIRouter, HTTPException
from services import auth_service, payment_service, user_service

router = APIRouter()

@router.post("/add-feature")
async def add_feature(feature_name: str):
    """
    Add a new feature to the system.

    Args:
    - feature_name (str): The name of the feature to be added.

    Returns:
    - A success message if the feature is added successfully.
    """
    try:
        # Authenticate the request
        auth_service.authenticate_request()
        
        # Add the feature
        result = user_service.add_feature(feature_name)
        
        # Return the result
        return {"message": f"Feature '{feature_name}' added successfully"}
    
    except Exception as e:
        # Handle any exceptions
        raise HTTPException(status_code=400, detail=str(e))