import requests

import service
from unittest.mock import patch, Mock
import pytest


@patch("service.get_user_from_db", return_value="mocked Armaghan")
def test_get_user_from_db(mock):
    result = service.get_user_from_db(1)
    assert result == "mocked Armaghan"
    mock.assert_called_once_with(1)


@patch("requests.get")
def test_get_users(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_get.return_value = mock_response
    data = service.get_users()

    assert data == {"id": 1, "name": "John Doe"}


@patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = Mock()
    mock_response.status_code = 500

    mock_get.return_value = mock_response

    with pytest.raises(requests.HTTPError):
        service.get_users()