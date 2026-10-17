def mul(*args):
    res = 1

    for n in args:
        res *= n

    return res


nums = list(map(int, input("Enter numbers separated by space: ").split()))
print(mul(*nums))


def calculate_bill(**kwargs):
    total = 0
    for key, value in kwargs.items():
        total+=value
    return total

print(calculate_bill(coffee=5, pizza=10, cake=8))