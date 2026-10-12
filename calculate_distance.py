import math


def calculate_d(c2):
    c1 = (0, 0)
    d = math.sqrt(((c2[0]-c1[0]) ** 2) + (c2[1]-c1[1]) ** 2)
    # distance = √((x₂ - x₁)² + (y₂ - y₁)²)
    return d


c2 = tuple(map(int, input('Enter the coordinates of the point (x y), separated by a space: ').split()))
print(calculate_d(c2))