class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seenZero = 0
        maxSeq = 0
        point = 0
        prev = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                seenZero = 1
                prev = point
                point = 0
            else:
                point += 1
            
            maxSeq = max(maxSeq, point + prev + seenZero)
        
        return maxSeq