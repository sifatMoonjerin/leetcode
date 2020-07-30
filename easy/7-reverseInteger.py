def reverse(x):
    negative = False
    if x < 0:
        negative = True
        x *= -1

    rev = 0
    while x:
        rev = rev*10 + (x % 10)
        x //= 10

    if rev >= 2**31 or rev < -2**31:
        return 0

    return -rev if negative else rev
