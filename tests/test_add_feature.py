``` ```python
from fastapi.testclient import TestClient
from main import app
from services.user_service import UserService
from services.payment_service import PaymentService
from models import User
import pytest

client = TestClient(app)

@pytest.fixture
def premium_user():
    user_data = {
        "id": 1,
        "is_premium": True
    }
    return User(**user_data)

def test_add_feature_for_premium_user(premium_user):
    # Arrange
    user_service = UserService()
    payment_service = PaymentService()

    # Act
    response = client.post(
        "/api/payments/add-feature",
        headers={"Authorization": f"Bearer {premium_user.id}"},
        json={"feature_name": "new_feature"}
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == "Feature added successfully"

def test_add_feature_for_non_premium_user():
    # Arrange
    non_premium_user = User(id=2, is_premium=False)
    user_service = UserService()
    payment_service = PaymentService()

    # Act
    response = client.post(
        "/api/payments/add-feature",
        headers={"Authorization": f"Bearer {non_premium_user.id}"},
        json={"feature_name": "new_feature"}
    )

    # Assert
    assert response.status_code == 403
    assert response.json()["message"] == "Only premium users can add features"

def test_add_feature_with_invalid_input():
    # Arrange
    premium_user = User(id=1, is_premium=True)
    user_service = UserService()
    payment_service = PaymentService()

    # Act
    response = client.post(
        "/api/payments/add-feature",
        headers={"Authorization": f"Bearer {premium_user.id}"},
        json={"invalid_key": "invalid_value"}
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["message"] == "Invalid input"