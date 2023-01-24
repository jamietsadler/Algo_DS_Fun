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