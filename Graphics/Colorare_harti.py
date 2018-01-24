"""Colorarea hartilor"""
global st,ams,ev
from numpy import zeros
n=int(input("n="))
a=zeros((n+1,n+1),dtype=int)
st=zeros((n+1),dtype=int)

def init(k,st):
    st[k]=0
def succesor(st,k):
    global ams
    if st[k]<4:
        st[k]=st[k]+1
        ams=True
    else:
        ams=False

def valid (st,k):
    global ev
    ev=True
    for i in range(1,k):
        if (st[i]==st[k]) and (a[i,k]==1 ):
            ev=False

def solutie (k):
    global n
    return k==n
for i in range (2,n+1):
    for j in range (1,i):
        print ('a[',i,',',j,']=')
        a[i,j]=input()
        a[j,i]=a[i,j]
sol =0
k=1
init(k,st)
while k>0:
    while True:
        succesor(st,k)
        if ams:
            valid(st,k)
        if (not ams) or (ams and ev ):
            break
    if ams and ev:
        if solutie(k):
            print (st[1:n+1])
            sol=sol+1
        else:
            k=k+1
            init(k,st)
    else:
        k=k-1
print ('S-au obtinut ',sol,' solutii')
