"""termenul de ordin n al sirului dat de media armonica cu forma recursiva"""

def med_arm(a, b, n):
    if n == 0:
        med = a
    else :
        if n == 1:
            med = b
        else:
            med = 2 * med_arm(a, b, n-1) * med_arm(a, b, n-2) / (med_arm(a, b, n-1) + med_arm(a, b, n-2))
    return med

a = float(input("a="))
b = float(input("b="))
n = int(input("n="))
print("Termen de ordin n este ", med_arm(a, b, n))