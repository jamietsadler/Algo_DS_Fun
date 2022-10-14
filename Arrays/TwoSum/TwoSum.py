from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in hash_map:
                return hash_map[remainder], i
            hash_map[nums[i]] = i