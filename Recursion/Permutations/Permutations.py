from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(first = 0):
            if first == len(nums) - 1:
                ans.append(nums[:])
                return
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]

                backtrack(first+1)

                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return ans
            
