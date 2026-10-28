def sum_nums(*args):
    if len(args) == 0:
        return 0
    res = 0
    for n in args:
        res += n
    return res


nums = list(map(int, input("Enter numbers separated by space: ").split()))
print(sum_nums(*nums))