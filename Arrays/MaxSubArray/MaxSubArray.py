from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        global_max = nums[0]
        
        for num in nums[1:]:
            current_max = max(num, current_max + num)
            global_max = max(current_max, global_max)
            
        return global_max