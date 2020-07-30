def isValid(s):
    if len(s) % 2 != 0:
        return False

    check = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []

    for bracket in s:
        if bracket in check:
            if not stack or stack.pop() != check[bracket]:
                return False
        else:
            stack.append(bracket)

    return not stack
