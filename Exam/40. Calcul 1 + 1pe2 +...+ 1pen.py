def calc(n):
    if n == 1:
        return 1
    return 1.0/n + calc(n-1)


print(calc(3))