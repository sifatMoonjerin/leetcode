# stupid problem
def removeDuplicates(nums):
    if not nums:
        return 0

    tail = 0

    for num in nums[1:]:
        if num != nums[tail]:
            tail += 1
            nums[tail] = num

    return tail+1
