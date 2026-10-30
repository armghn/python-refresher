def factorial(n: int) -> int:
    if type(n) is not int:
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1

    return n * factorial(n-1)


# print(factorial("Hi"))
# print(factorial(-4))
print(factorial(0))
print(factorial(5))