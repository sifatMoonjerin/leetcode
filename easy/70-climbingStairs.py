memo = {1:1,2:2}

def climbStairs(n):
    # top to bottom
    if n == 1 or n == 2: return n
    return climbStairs(n-1)+climbStairs(n-2)
    # top to bottom memoized
    # if n not in memo:
    #     memo[n] = climbStairs(n-1)+climbStairs(n-2)
    # return memo[n]
    
    # bottom to top 
    # for i in range(3,n+1):
    #     memo[i] = memo[i-1]+memo[i-2]
    # return memo[n]

    # bottom to top constant space
    # if n == 1 or n == 2: return n
    # prev1, prev2 = 2, 1
    # for i in range(2,n):
    #     prev1, prev2 = prev1+prev2, prev1
    # return prev1

print(climbStairs(6))
            