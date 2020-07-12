def firstUniqChar(s):
        # n = len(s)
        # for i in range(len(s)):
        #     if s[i] not in s[i+1:] and s[i] not in s[:i]:
        #         return i
        # return -1
        count = {}
        
        for ch in s:
            count[ch] = count.get(ch,0) + 1
        
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        
        return -1