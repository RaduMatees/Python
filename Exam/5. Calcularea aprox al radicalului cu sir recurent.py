"""Calcularea aproximativ al radicalului cu sir recurent"""
from math import sqrt
a = float(input("a="))
eps = float(input("eps="))
x = a
y = 1./2 * (x + a / x)
while abs(x - y) >= eps:
    x = y
    y = 1./2 * (x + a / x)
print ("Limita este", format(y, '.10f'))
print ("Verificare cu sqrt", format(sqrt(a), '10f'))