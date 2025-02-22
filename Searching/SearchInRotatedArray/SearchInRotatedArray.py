from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0 
        j = len(nums) - 1

        while i < j:
            if nums[i] > nums[j]:
                i += 1
            else:
                j -=1 
            
        def binary_search(left, right):
            if nums[left] == target:
                return left
            if left >= right:
                return -1 
            if nums[left] < target:
                return binary_search(left+ 1, right)
            else:
                return binary_search(left, right - 1)

        # lhs 
        if (ans := binary_search(0, i)) != -1:
            return ans
        return binary_search(j, len(nums) - 1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high- low) // 2
            if nums[mid] == target:
                return mid            
            if nums[mid] >= nums[low]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target <= nums[high] and target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1