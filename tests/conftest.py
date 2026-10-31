import pytest
import shapes

# Define reusable fixtures to provide test objects and manage setup and teardown.


@pytest.fixture
def circle():
    print("Setting Up")
    circle = shapes.Circle(10)

    yield circle

    print("Tearing Down")


@pytest.fixture
def rectangle():
    print("Setting Up")

    rectangle = shapes.Rectangle(4, 6)

    yield rectangle

    print("Cleaning Up")


@pytest.fixture
def second_rectangle():
    print("Setting up")
    second_rectangle = shapes.Rectangle(6, 4)
    yield second_rectangle
    print("Cleaning up")