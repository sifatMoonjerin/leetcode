def missingNumber(nums):
    n = len(nums)
    sumNums = 0
    sumSeries = n*(n+1)/2

    for num in nums:
        sumNums += num

    return int(sumSeries-sumNums)
