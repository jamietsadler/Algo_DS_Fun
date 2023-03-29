from typing import List

# Top down 
class Solution:
    def __init__(self):
        self.memo = {}

    def maxSubArray(self, nums: List[int]) -> int:
        self.max_amount = nums[0]
        self.solve(0, nums)
        return self.max_amount

    def solve(self, i, nums):        
        if i == len(nums): 
            return 0 
        if i in self.memo:
            return self.memo[i]
        
        res = max(nums[i] + self.solve(i+1, nums), nums[i])
        self.max_amount = max(self.max_amount, res)
        self.memo[i] = res
        return res

# Bottom Up O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_num = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i] + dp[i-1], nums[i])
            max_num = max(dp[i], max_num)
        return max_num
    

# Bottom up constant space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = nums[0]
        curr_subarray = nums[0]

        for i in range(1, len(nums)):
            curr_subarray = max(nums[i] + curr_subarray, nums[i])
            max_num = max(curr_subarray, max_num)
        return max_num

# Inplace (Kadanes)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]

        return max(nums)