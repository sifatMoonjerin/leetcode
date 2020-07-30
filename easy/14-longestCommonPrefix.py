def longestCommonPrefix(s):
    prefix = ''
    if not s:
        return prefix
    if len(s) == 1:
        return s[0]
    for i in range(len(s[0])):
        for j in range(1, len(s)):
            if i >= len(s[j]) or s[0][i] != s[j][i]:
                return prefix
        prefix += s[0][i]
    return prefix
