import os
import requests
from models.auth import AuthRequest
from dotenv import load_dotenv
from logger import logger
from typing import Any
from faker import Faker

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
fake = Faker()


def make_auth_request(username: Any, password: Any):
    auth_data = AuthRequest(username=username, password=password).model_dump()

    logger.debug(f"Base url: {BASE_URL}")
    logger.debug(f"Request body: {auth_data}")

    response = requests.post(f"{BASE_URL}/auth", json=auth_data)
    logger.debug(f"Response status code: {response.status_code}")
    logger.debug(f"Response body: {response.json()}")

    return response


def fake_username():
    return fake.user_name()


def fake_password():
    return fake.password()
