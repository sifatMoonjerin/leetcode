def majorityElement(nums):
    count = 1
    majEl = nums[0]

    for num in nums[1:]:
        if count == 0:
            majEl = num
            count += 1
        elif majEl == num:
            count += 1
        else:
            count -= 1

    return majEl

    # count = {}
    # test = len(nums)/2

    # for num in nums:
    #     if num in count:
    #         count[num] += 1
    #     else:
    #         count[num] = 1

    #     if count[num] > test:
    #         return num


print(majorityElement([1, 2, 3, 2, 1, 1, 1, 1]))
