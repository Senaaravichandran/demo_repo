``` ```python
from fastapi.testclient import TestClient
from main import app
from models import User
from services.auth_service import get_user_type

client = TestClient(app)

def test_free_user_request_limit():
    # Arrange
    user = User(id=1)
    user_type = get_user_type(user)
    
    # Act and Assert
    if user_type == "free":
        response = client.get("/api/payments/")
        assert response.status_code == 200
        response = client.get("/api/payments/")
        assert response.status_code == 429  # Too Many Requests

def test_premium_user_request_limit():
    # Arrange
    user = User(id=2)
    user_type = get_user_type(user)
    
    # Act and Assert
    if user_type == "premium":
        for _ in range(10):
            response = client.get("/api/payments/")
            assert response.status_code == 200