def romanToInt(s):
        value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        prev = 0
        number = 0
        
        for rom in s:
            cur = value[rom]
            if prev != 0 and prev<cur:
                number += cur - 2*prev
            else:
                prev = cur
                number += cur
                
        return number

print(romanToInt("MCMXCIV"))