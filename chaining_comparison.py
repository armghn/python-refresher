def comparison(num1, num2, num3):
    return num1 < num2 <= num3


a, b, c = map(int, input("Enter three numbers: ").split())
print(comparison(a, b, c))