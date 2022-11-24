class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sumL = 0
        sumR = sum(nums)
        for i in range(len(nums)):
            
            sumR -= nums[i]
            if sumL == sumR:
                return i
            sumL += nums[i]
            
            
        return -1