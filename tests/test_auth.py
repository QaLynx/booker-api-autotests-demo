import os
import requests
from models.auth import AuthRequest
from dotenv import load_dotenv
from logger import logger

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

def test_auth():
    auth_data = AuthRequest(
        username="admin",
        password="password123"
    ).model_dump()

    logger.debug(f"Base url: {BASE_URL}")
    logger.debug(f"Request body: {auth_data}")

    response = requests.post(f"{BASE_URL}/auth", json=auth_data)
    logger.debug(f"Status code: {response.status_code}")
    logger.debug(f"Response body: {response.json()}")



    assert response.status_code == 200,  f"Expected status code 200, got {response.status_code}"
    response_json = response.json()
    token = response_json['token']
    assert "token" in response_json, "Token is missing in the response"
    assert len(token) > 0, "token shold not be empty"
    assert isinstance(token, str), "Token should be a string"