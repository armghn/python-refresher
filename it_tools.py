import itertools as it


nums = [1, 2, 3]
a = it.cycle(nums)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

print(list(it.combinations(nums, 2)))
print(list(it.combinations_with_replacement(nums, 2)))

counter = it.count(3, 10)
print(next(counter))
print('**********')

for n in counter:
    if n > 50:
        break
    print(n)

print(list(it.accumulate(nums)))

print(list(it.permutations(nums, 2)))