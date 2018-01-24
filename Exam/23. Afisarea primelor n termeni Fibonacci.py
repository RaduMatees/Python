"""Termenul de ordinul n al unui sir Fibonacci"""

def Fibo(a, b, n):
    if n == 0:
        f = a
    else:
        if n == 1:
            f = b
        else:
            f = Fibo(a, b, n-1) + Fibo(a, b, n-2)
    return f

a = float(input("a= "))
b = float(input("b= "))
n = int(input("n= "))

print("Termenul de ordinul ", n, "este", Fibo(a, b, n))
print("Termenii sirului sunt ", end='')

for k in range(0, n+1):
    print(Fibo(a, b, k), end='')