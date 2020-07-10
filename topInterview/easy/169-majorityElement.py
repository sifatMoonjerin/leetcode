def majorityElement(nums):
        count = {}
        test = len(nums)/2
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
                
            if count[num] > test:
                return num


print(majorityElement([1,2,3,2,1,1,1,1]))