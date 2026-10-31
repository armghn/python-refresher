import pytest
import shapes


def test_area(circle):
    assert circle.area() == 3.14 * (circle.r ** 2)


def test_perimeter(circle):
    assert circle.perimeter() == 3.14 * circle.r * 2

