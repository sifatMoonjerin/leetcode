
def getSum(n):
    sum = 0
    while n:
        sum += (n%10)**2
        n //= 10
    return sum
        
    
def isHappy(n):
    count = {}
    
    while n!=1:
        n = getSum(n)
        if n in count:
            return False
        count[n] = n
    
    return True