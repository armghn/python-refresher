def divis(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Dividable by 3 and 5"
    elif num % 3 == 0:
        return "Dividable by 3 only"
    elif num % 5 == 0:
        return "Dividable by 5 only"
    else:
        return None


print(divis(15))
print(divis(9))
print(divis(25))
print(divis(16))