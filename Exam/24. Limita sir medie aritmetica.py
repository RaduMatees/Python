"""Limita unui sir recurent dat de media aritmetica"""

a = float(input("a= "))
b = float(input("b= "))
eps = float(input("eps= "))
x = float(a)
y = float(b)

while abs(x - y) >= eps:
    z = (x+y)/2
    x = y
    y = z
print("Limita este" ,format(x,'.5f'))