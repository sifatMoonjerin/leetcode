def reverseString(s):
        n = len(s)   
        r = int((n/2)//1)
        
        for i in range(r):  
            s[i], s[n-1-i] = s[n-1-i], s[i]

        # single line solution
        # s.reverse()
            
        print(s)

reverseString(['h','e','l','l','o'])

