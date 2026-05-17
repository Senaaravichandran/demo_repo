from fastapi import FastAPI
from routes import payment_routes, user_routes

app = FastAPI(title="Demo Payment Service")

# Include routers
app.include_router(payment_routes.router, prefix="/api/payments")
app.include_router(user_routes.router, prefix="/api/users")

@app.get("/")
def root():
    return {"message": "Demo Payment Service API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

def add_feature(feature_name: str) -> dict:
    """
    This function adds a new feature to the Demo Payment Service API.
    
    Args:
        feature_name (str): The name of the feature to be added.
    
    Returns:
        dict: A dictionary containing the result of the operation.
    """
    try:
        # Add the feature to the database or any other storage system
        # For demonstration purposes, we will just return a success message
        return {"message": f"Feature '{feature_name}' added successfully"}
    except Exception as e:
        # Handle any exceptions that may occur during the operation
        return {"error": str(e)}

@app.post("/add-feature")
def add_new_feature(feature_name: str):
    """
    This endpoint adds a new feature to the Demo Payment Service API.
    
    Args:
        feature_name (str): The name of the feature to be added.
    
    Returns:
        dict: A dictionary containing the result of the operation.
    """
    return add_feature(feature_name)