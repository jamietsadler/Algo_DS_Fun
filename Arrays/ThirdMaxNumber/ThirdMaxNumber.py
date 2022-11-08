class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        firstMax = float('-inf')
        secondMax = float('-inf')        
        thirdMax = float('-inf')
        
        for i in range(len(nums)):
            if nums[i] == firstMax or nums[i] == secondMax or nums[i] == thirdMax:
                continue
            
            if nums[i] >= firstMax:
                thirdMax = secondMax
                secondMax = firstMax
                firstMax = nums[i]
            elif nums[i] >= secondMax:
                thirdMax = secondMax
                secondMax = nums[i]
            elif nums[i] >= thirdMax:
                thirdMax = nums[i]
            
        
        if thirdMax == float('-inf'):
            return max(firstMax, secondMax)
        return thirdMax