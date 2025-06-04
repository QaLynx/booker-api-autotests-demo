import os
import requests
from models.auth import AuthRequest
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

def test_auth():
    auth_data = AuthRequest(
        username="admin",
        password="password123"
    ).model_dump()

    response = requests.post(f"{BASE_URL}/auth", json=auth_data)

    assert response.status_code == 200,  f"Expected status code 200, got {response.status_code}"
    response_json = response.json()
    print(response_json)
    assert "token" in response_json, "Token is missing in the response"
    assert len(response_json["token"]) > 0, "token shold not be empty"