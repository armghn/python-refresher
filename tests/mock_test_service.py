import service
from unittest.mock import patch


@patch("service.get_user_from_db", return_value="mocked Armaghan")
def test_get_user_from_db(mock):
    result = service.get_user_from_db(1)
    assert result == "mocked Armaghan"
    mock.assert_called_once_with(1)