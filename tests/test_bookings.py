import os
import requests

from logger import logger
from models.headers import Headers
from conftest import BASE_URL
from models.responses import AllBookingResponse


def test_get_everything_in_booking():
    """
    Проверяет успешное получение списка всех бронирований.

    1. Отправляет GET-запрос к эндпоинту /booking с заголовком Accept: application/json.
    2. Логирует детали запроса и ответа: заголовки, URL, статус-код, тело ответа.
    3. Валидирует структуру ответа с помощью модели AllBookingResponse.
    4. Убеждается, что:
       - Статус-код 200.
       - Тело ответа — непустой список.
       - Данные соответствуют ожидаемой схеме.

    Тест покрывает базовую доступность и корректность формата данных.
    """
    headers = Headers(Accept="application/json").model_dump(exclude_unset=True)
    response = requests.get(url=f"{BASE_URL}/booking", headers=headers)

    logger.debug(f"Request header : {headers}")
    logger.debug(f"Request url : {response.url}")
    logger.debug(f"Status code: {response.status_code}")
    logger.debug(f"Response body: {response.json()}")

    try:
        booking_list_response = AllBookingResponse(bookings=response.json())
    except Exception as e:
        logger.error(f"Validator error: {e}")
        assert False, f"Validator error: {e}"

    data = booking_list_response.bookings

    assert (
        response.status_code == 200
    ), f"Expected status code 200, got {response.status_code}"
    assert isinstance(data, list), "Data format is not a list"
    assert len(data) > 0, "Empty list. No booking ids."
