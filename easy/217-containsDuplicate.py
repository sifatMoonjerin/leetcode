def containsDuplicate(nums):
        count = {}
        
        for num in nums:
            if num in count:
                return True
            else:
                count[num] = 1
                
        return False