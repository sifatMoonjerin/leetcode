def detectCapitalUse(word):
    firstCap = word[0].isupper()

    if firstCap:
        for l in range(2, len(word)):
            if word[l].isupper() != word[l-1].isupper():
                return False
    else:
        for l in word:
            if l.isupper():
                return False

    return True
