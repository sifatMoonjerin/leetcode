def shuffle(nums, n):
    newL = []
    x, y = 0, n
    for _ in range(0,n):
        newL.append(nums[x])
        newL.append(nums[y])
        x += 1
        y += 1
    return newL