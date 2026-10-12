setA = set(map(int, input("Enter numbers separated by space: ").split()))
setB = set(map(int, input("Enter numbers separated by space: ").split()))

union = setA.union(setB)
intersection = setA.intersection(setB)

print(union)
print(intersection)