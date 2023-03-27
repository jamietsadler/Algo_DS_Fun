from typing import List

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.search(nums, 0, len(nums) - 1)

    def search(self, nums, low, high):
        if low == high:
            return low
        mid = (low + high)//2
        if nums[mid] > nums[mid + 1]:
            return self.search(nums, low, mid)
        else:
            return self.search(nums, mid+1, high)
        
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return 0
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[mid+1]:
                high = mid
            else:
                low = mid + 1
        
        return low

