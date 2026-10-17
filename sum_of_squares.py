def squares(nums):
    num_sqrs = list(map(lambda n: n**2, nums))
    return num_sqrs

def sqrs(nums):
    num_sqrs = [n**2 for n in nums]
    return num_sqrs


nums = list(map(int, input("Enter numbers separated by space: ").split()))

print(sum(squares(nums)))
print(sqrs(nums))