import pytest
import my_func as f


def test_add():
    result = f.add(1, 4)
    assert result == 5


def test_add_strings():
    result = f.add("I am learning ", "pytest")
    assert result == "I am learning pytest"


def test_divide():
    result = f.divide(8, 2)
    assert result == 4


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        f.divide(10, 0)


