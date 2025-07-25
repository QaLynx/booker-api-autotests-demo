import pytest
from conftest import make_auth_request, fake_username, fake_password


@pytest.mark.parametrize(
    "username, password, expected_status, expected_reason",
    [
        ("admin", "password123", 200, None),
        (fake_username(), "password123", 200, "Bad credentials"),
        ("admin", fake_password(), 200, "Bad credentials"),
        (fake_username(), fake_password(), 200, "Bad credentials"),
        ("", "password123", 200, "Bad credentials"),
        ("admin", "", 200, "Bad credentials"),
        (1, "", 200, "Bad credentials"),
        (10, 1, 200, "Bad credentials"),
    ],
    ids=[
        "Valid credentials",
        "Invalid username",
        "Invalid password",
        "Invalid username and password",
        "Empty username",
        "Empty password",
        "Numeric username",
        "Numeric username and password",
    ],
)
def test_auth(username, password, expected_status, expected_reason):
    """
    Тестирует аутентификацию с различными комбинациями учётных данных.

    Проверяет:
    - Успешный вход при корректных данных (возвращается токен).
    - Ошибки при неверных, пустых или нестандартных (числовых) значениях.
    - Наличие и корректность сообщения 'reason' при ошибках.
    - Отсутствие токена при неудачной аутентификации.

    Параметризованные кейсы охватывают позитивный и негативные сценарии.
    """
    response = make_auth_request(username, password)

    assert (
        response.status_code == expected_status
    ), f"Expected status code {expected_status}, got {response.status_code}"

    response_json = response.json()

    if expected_reason is None:
        assert "token" in response_json, "Token is missing in the response"
        token = response_json["token"]
        assert len(token) > 0, "Token should not be empty"
        assert isinstance(token, str), "Token should be a string"
    else:
        assert "reason" in response_json, f"Reason is missing in the response"
        reason = response_json["reason"]
        assert (
            reason == expected_reason
        ), f"Expected reason '{expected_reason}', got '{reason}'"
        assert (
            "token" not in response_json
        ), "Token should not be present in the response"
