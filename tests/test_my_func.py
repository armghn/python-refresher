import pytest
import time

import reason

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


@pytest.mark.slow
def test_slow():        #Run with pytest -m slow
    time.sleep(5)
    result = f.divide(20, 5)
    assert result == 4


@pytest.mark.skip(reason="This feature is currently broken")
def test_skip():
    assert f.add(2, 3) == 5


@pytest.mark.xfail(
    reason="Division by zero is not handled",
    raises=ZeroDivisionError    # Specify the expected exception so that only ZeroDivisionError is treated as an expected failure.
)
def test_xfail():
    assert f.divide(3, 0)


