prices = {
    "apple": 2,
    "banana": 1,
    "orange": 3,
    "milk": 4,
    "bread": 2
}


def process_order(**kwargs):
    invalid_items = []
    valid_items = {}
    for k, v in kwargs.items():
        if v <= 0 or k not in prices.keys():   # product is invalid if price <= 0 or name of product not in price list
            invalid_items.append(k)
        else:
            valid_items.update({k: v})

    sum_valid = sum(valid_items.values())

    res = {"Total": sum_valid,
           "valid_items": valid_items,
           "invalid_items": invalid_items
           }

    return res


result = process_order(
    apple=3,
    banana=2,
    milk=1,
    chocolate=4,
    bread=-2,
    orange=2.5
)

print(result)


