def plusOne(digits):
    index = -1
    n = len(digits)
    while index >= -n:
        temp = digits[index] + 1
        digits[index] = (temp % 10)
        if temp != 10:
            return digits
        index -= 1
    return [1] + digits
