def magic(num):
    step = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
            step += 1
            print(num)
        else:
            num = (num * 3) + 1
            step += 1
            print(num)

    return step


n = int(input("Enter a number: "))
steps = magic(n)
print(f"Finished in {steps} step(s)!")