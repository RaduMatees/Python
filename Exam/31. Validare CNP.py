"""Validare CNP"""
from numpy import zeros

CNP = zeros((13), dtype=int)

print("Introducere CNP: ")

for i in range (0, 13):
    print("CNP[", i, "]= ") #citire CNP
    CNP[i] = input()
print("CNP-ul este ", CNP)

S = 0
sc = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]

for i in range(0, 12):
    S = S + sc[i]* CNP[i]
r = S % 11

if((r == 10) & (CNP[12] == 1))|((r < 10)&(CNP[12] == r)):
    print("CNP corect")
else:
    print("CNP incorect")