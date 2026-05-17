``` ```python
from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_add_feature():
    response = client.post(
        "/api/features",
        json={"name": "Test Feature", "description": "This is a test feature"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Feature"
    assert response.json()["description"] == "This is a test feature"

def test_add_duplicate_feature():
    response = client.post(
        "/api/features",
        json={"name": "Test Feature", "description": "This is a test feature"},
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Feature already exists"

def test_add_feature_with_invalid_data():
    response = client.post(
        "/api/features",
        json={"invalid_key": "Invalid value"},
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "field required"

def test_add_feature_with_empty_name():
    response = client.post(
        "/api/features",
        json={"name": "", "description": "This is a test feature"},
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "ensure this value has at least 1 characters"

def test_add_feature_with_empty_description():
    response = client.post(
        "/api/features",
        json={"name": "Test Feature", "description": ""},
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "ensure this value has at least 1 characters"