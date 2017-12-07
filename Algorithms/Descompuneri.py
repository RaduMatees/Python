"""Rostogolire"""
def r_dreapta(k):
    global sus,jos,stanga,dreapta,fata,spate
    for i in range (0,k):
        sus,jos,stanga,dreapta = stanga,dreapta,jos,sus
def r_stanga(k):
    global sus,jos,stanga,dreapta,fata,spate
    for i in range (0,k):
        sus,jos,stanga,dreapta = dreapta,stanga,sus,jos
def r_fata(k):
    global sus,jos,stanga,dreapta,fata,spate
    for i in range (0,k):
        sus,jos,fata,spate = spate,fata,sus,jos
def r_spate(k):
    global sus,jos,stanga,dreapta,fata,spate
    for i in range (0,k):
        sus,jos,fata,spate = fata,spate,jos,sus
sus = int(input("Sus="))
fata = int(input("Fata="))
dreapta = int(input("Dreapta="))
spate = 7 - fata
jos = 7 - sus
stanga = 7 - dreapta
c = 1
while c == 1 :
    c = int(input("Introd 1 pentru a continua 0 pentru a va opri: "))
    var = str(input("Introduceti directia: "))
    k = int(input("Introduceti nr de rostogoliri:"))
    if var == 'st':
        r_stanga(k)
    if var == 'dr':
        r_dreapta(k)
    if var == 'fa':
        r_fata(k)
    if var == 'sp':
        r_spate(k)
    print(sus,jos,fata,spate,stanga,dreapta)
