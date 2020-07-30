def moveZeroes(nums):
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            if i != zero:
                nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
    print(nums)


moveZeroes([0, 1, 4, 0, 2, 3, 0, 3, 0])
