from typing import List
from functools import lru_cache

# Recursive (backtracking)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @lru_cache
        def helper(i):
            if i == len(nums) - 1:
                return True

            furthest_jump = min(i + nums[i], len(nums) - 1)

            for j in range(i+1, furthest_jump+1):
                if helper(j):
                    return True
            return False

        return helper(0)
    
# Backtracking
class Solution:
    def canJumpFromPosition(self, position, nums, memo):
        if position in memo:
            return memo[position]
        
        if position == len(nums) - 1:
            memo[position] = True
            return True
        
        if nums[position] == 0:
            memo[position] = False
            return False
        
        maxStep = nums[position]
        for step in range(1, maxStep + 1):
            newPosition = position + step
            if self.canJumpFromPosition(newPosition, nums, memo):
                memo[newPosition] = True
                return True
        
        memo[position] = False
        return False 
    
    def canJump0(self, nums: List[int]) -> bool:
        memo = {}
        memo[len(nums) - 1] = True
        return self.canJumpFromPosition(0, nums, memo)

# Greedy
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