def calcSumN(n):
    if n == 1:
        return 1
    return n + calcSumN(n-1)

print(calcSumN(5))