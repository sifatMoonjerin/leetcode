
def getSum(n):
    sum = 0
    while n:
        sum += (n%10)**2
        n //= 10
    return sum
        
    
def isHappy(n):
    slow = n
    fast = n
    
    while True:
        slow = getSum(slow)
        fast = getSum(fast)
        fast = getSum(fast)
        if fast == 1: return True
        if fast == slow: return False
    # count = {}
    
    # while n!=1:
    #     n = getSum(n)
    #     if n in count:
    #         return False
    #     count[n] = n
    
    # return True