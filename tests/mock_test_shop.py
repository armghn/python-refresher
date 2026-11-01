import shop
from unittest.mock import patch


@patch("shop.get_price", return_value=100)
def test_calculate_discount(mock):
    result = shop.calculate_discount()
    assert result == 90