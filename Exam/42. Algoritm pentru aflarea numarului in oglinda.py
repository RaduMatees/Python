def oglinda(n):
    revN = 0

    while n != 0:
        r = n % 10
        n = n // 10
        revN = revN * 10 + r

    return revN

    # or like this
    # return int(str(n)[::-1])

print(oglinda(32451))

