def calculate_discount(price):
    if price > 50_000:
        price *= 0.8
    elif price > 20_000:
        price *= 0.9

    return price


p = int(input("Enter price: "))
print(calculate_discount(p))