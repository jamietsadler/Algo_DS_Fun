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


class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        m = len(multipliers)
        n = len(nums)

        dp = [0]*(m+1)

        for op in range(m-1, -1, -1):
            for i in range(0, op+1):
                l = dp[i+1] + nums[i]*multipliers[op]
                r = dp[i]+ nums[(n-1)-(op-i)]*multipliers[op]
                dp[i] = max(l, r)

        return dp[0]