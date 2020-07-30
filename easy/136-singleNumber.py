def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
    return res


print(singleNumber([1, 2, 3, 2, 1]))
