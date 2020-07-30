import math


def mySqrt(x):
    if x == 0:
        return 0
    y = 2**(math.log2(x)/2)
    return math.floor(y)


print(mySqrt(8))
