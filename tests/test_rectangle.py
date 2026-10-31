def test_not_equal(rectangle, second_rectangle):
    assert rectangle != second_rectangle


def test_area_rectangle(rectangle):
    assert rectangle.area() == rectangle.length * rectangle.width


def test_perimeter_rectangle(rectangle):
    assert rectangle.perimeter() == (rectangle.length + rectangle.width) * 2
