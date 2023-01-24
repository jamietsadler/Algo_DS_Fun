from typing import List
from functools import cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) -1 
        
        @cache
        def dp(i):
            if i == n:
                return True
            
            for j in range(i+1, min(i + nums[i], n) + 1):
                if dp(j):
                    return True
                
            return False
        
        return dp(0)
    
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_pos = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i

        return True if last_pos == 0 else False