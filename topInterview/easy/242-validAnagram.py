def isAnagram(s, t):
        if len(s) != len(t):
            return False
        else:
            count = {}
            for ch in s:
                count[ch] = count.get(ch, 0) + 1

            for ch in t:
                if ch in count:
                    count[ch] -= 1
                    if count[ch] < 0:
                        return False
                else:
                    return False

            return True   

print(isAnagram('rat', 'car'))