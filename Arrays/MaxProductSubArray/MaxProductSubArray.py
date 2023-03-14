class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        

        for i in range(1, len(nums)):
            temp_max = max(nums[i], max_so_far*nums[i], min_so_far*nums[i])
            min_so_far = min(nums[i], max_so_far*nums[i], min_so_far*nums[i])
            max_so_far = temp_max
            result = max(max_so_far, result)

        return result
