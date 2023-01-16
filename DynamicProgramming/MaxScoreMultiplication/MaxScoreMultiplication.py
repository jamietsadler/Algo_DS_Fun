from typing import List
from functools import cache
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        if not nums:
            return 0
        
        @cache
        def recurse(i, nums_mod):
            if i >= len(multipliers):
                return 0
            
            ans = max(recurse(i+1, nums_mod[1:]) + (nums_mod[0] * multipliers[i]), recurse(i+1, nums_mod[:-1]) + (nums_mod[-1] * multipliers[i]))

            return ans
        
        return recurse(0, tuple(nums))