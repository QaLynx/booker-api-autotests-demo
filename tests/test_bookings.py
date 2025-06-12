import os
import requests

from logger import logger
from models.headers import Headers
from conftest import BASE_URL



def test_get_everything_in_booking():
    headers = Headers(Accept="application/json").model_dump(exclude_unset=True)
    response = requests.get(url=f"{BASE_URL}/booking", headers=headers)

    logger.debug(f"Request header : {headers}")
    logger.debug(f"Request url : {response.url}")
    data = response.json()

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert isinstance(data, list), "Data format is not a list"
    assert len(data) > 0, "Empty list. No booking ids."

