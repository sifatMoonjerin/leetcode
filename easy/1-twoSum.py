def twoSum(nums, target):
    find = {}
    for i in range(len(nums)):
        if target-nums[i] in find:
            return [find[target-nums[i]], i]
        find[nums[i]] = i
