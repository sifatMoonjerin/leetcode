def hammingWeight(n):
        if not n: return 0
        return 1+hammingWeight(n&(n-1))
        # count = 0
        # while n:
        #     n &= (n-1)
        #     count += 1
        # return count
        # if not n: return 0
        # return (n%2)+hammingWeight(n//2)
        # count = 0
        # while n:
        #     print(n)
        #     if n%2: count += 1
        #     n//=2
        # return count