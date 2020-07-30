def strStr(haystack, needle):
    if not needle:
        return 0
    x, y = len(haystack), len(needle)

    kmp = [0]
    a, b = 0, 1
    while b < y:
        if needle[b] == needle[a]:
            a += 1
            kmp.append(a)
            b += 1
        else:
            if a == 0:
                kmp.append(0)
                b += 1
            else:
                a = kmp[a-1]

    i, j = 0, 0

    while i < x:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == y:
                return i-j
        else:
            if j == 0:
                i += 1
            else:
                j = kmp[j-1]
    return -1
