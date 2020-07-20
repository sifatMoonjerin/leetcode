import math
def isPowerOfThree(n):
    if n <= 0: return False
    x = math.log10(n)/math.log10(3)
    return x%1 == 0
    # if n <= 0:
    #     return False
    
    # while n%3 == 0:
    #     n /= 3
    
    # return n == 1
print(isPowerOfThree(27))