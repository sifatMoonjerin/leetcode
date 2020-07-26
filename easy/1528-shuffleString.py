def restoreString(s, indices):
        output = [None]*len(indices)
        i = 0
        
        for indice in indices:
            output[indice] = s[i]
            i += 1
        
        return ''.join(output)