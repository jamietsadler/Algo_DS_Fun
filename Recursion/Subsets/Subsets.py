from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def backtrack(pnt = 0, curr = []):
            if len(curr) == k:  
                ans.append(curr[:])
                return
            for i in range(pnt, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        for k in range(len(nums) + 1):
            backtrack()

        return ans