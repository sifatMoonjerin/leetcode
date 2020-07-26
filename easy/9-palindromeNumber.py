def isPalindrome(x: int) -> bool:
    # x = list(str(x))
    # l, r = 0, len(x)-1
    # while l < r:
    #     if x[l] != x[r]:
    #         return False
    #     l += 1
    #     r -= 1
    # return True
    if x < 0: return False
    
    prevX, newX = x, 0
    
    while x:
        newX = (x%10) + newX*10
        x //= 10
    
    return prevX == newX

print(isPalindrome(343))