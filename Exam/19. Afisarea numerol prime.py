"""program pt afisarea numerelor prime mai mici sau egal cu n"""

n = int(input("n="))

for i in range(1, n + 1):
    divizorii = 0
    for j in range(1, i + 1):
        if i % j == 0:
            divizorii += 1
    if divizorii == 2:
        print(i)