def titleToNumber(s):
        output = 0
        n = len(s)-1
        for ch in s:
            output += (ord(ch)-64)*26**(n)
            n -= 1
        
        return output

print(titleToNumber('AB'))