def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def comb(n, k):
    return fact(n)/(fact(k)*(fact(n-k)))


print(comb(5, 3))