def isPalindrome(s):
    l = 0
    r = len(s)-1
    while l<r:
        if s[l].isalnum() and s[r].isalnum():
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        elif s[l].isalnum():
            r -= 1
        elif s[r].isalnum():
            l += 1
        else:
            l += 1
            r -= 1
    return True
        
    # newS = ''
    # for ch in s:
    #     if ch.isalnum():
    #         newS += ch.lower()
    
    # return newS == newS[::-1]