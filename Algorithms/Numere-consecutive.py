"""Numere consecutive"""
start = int (input("Start="))
pasi = int (input("pasi="))
for i in range (0,pasi):
    print(start + i)
start = int (input("Start="))
pasi = int (input("pasi="))
for i in range (start - pasi + 1,start + 1):
    print(i)