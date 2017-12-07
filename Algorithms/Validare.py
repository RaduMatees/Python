"""Validare CNP"""
from numpy import zeros
CNP=zeros((13), dtype=int)
sc=zeros((13),dtype=int)
print("dati cifre CNP-ului")
for i in range(0,13):
    print("CNP[",i,"]=")
    CNP[i]=input()
print("CNP-ul este:",CNP)
S=0
sc[0],sc[1],sc[2],sc[3],sc[4],sc[5]=2,7,9,1,4,6
sc[6],sc[7],sc[8],sc[9],sc[10],sc[11]=3,5,8,2,7,9
for i in range(0,12):
    S=S+sc[i]*CNP[i]
r=S%11
if ((r==10) and (CNP[12]==11)) or ((r<10) and (CNP[12]==r)):
    print("CNP CORECT")
else:
    print("CNP INCORECT")