def intersect(nums1, nums2):
    # count = {}
    # result = []

    # if len(nums1) > len(nums2):
    # nums1, nums2 = nums2, nums1

    # for num in nums1:
    #     count[num] = count.get(num, 0) + 1

    # for num in nums2:
    #     if num in count and count[num] > 0:
    #         result.append(num)
    #         count[num] -= 1

    # return result

    result = []

    nums1.sort()
    nums2.sort()

    p1 = 0
    p2 = 0

    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            result.append(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] < nums2[p2]:
            p1 += 1
        else:
            p2 += 1

    return result
