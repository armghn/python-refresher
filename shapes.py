class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * (self.r ** 2)

    def perimeter(self):
        return 3.14 * self.r * 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.length == other.length and self.width == other.width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
