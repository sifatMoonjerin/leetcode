def getSum(a, b):
        maxi = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b:
            a, b = (a^b)&mask, ((a&b)<<1)&mask
        
        return a if a<=maxi else ~(a^mask)
        