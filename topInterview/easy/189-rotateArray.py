def rotate(nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        # for _ in range(k):
        #     nums.insert(0,nums.pop())
        
        n = len(nums)
        nums[:] = nums[n-k:]+nums[:n-k]
        print(nums)

rotate([1,2,3,4],5)