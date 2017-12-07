"""Rezolvarea triunghiului"""
from math import *
from numpy import *
a = input("a=")
b = input("b=")
c = input("c=")
a,b,c=float(a), float(b), float(c)
gama_rad = acos(a**2+b**2-c**2)/(2*a*b)
alfa_rad = asin((a*sin(gama_rad))/c)
beta_rad = asin((b*sin(gama_rad))/c)
gama_deg = (gama_rad * 100)/pi
alfa_deg = (alfa_rad * 100)/pi
beta_deg = (beta_rad * 100)/pi
print("Unghiul alfa este", format(alfa_deg,'.2f'))
print("Unghiul beta este", format(beta_deg,'.2f'))
print("Unghiul gama este", format(gama_deg,'.2f'))
p=(a+b+c)/2
S=sqrt(p*(p-a)*(p-b)*(p-c))
R=(a*b*c)/4*S

