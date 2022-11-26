from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        pivotIdx = int(len(nums)/2)
        left_arr = self.sortArray(nums[:pivotIdx])
        right_arr = self.sortArray(nums[pivotIdx:])
        return self.merge(left_arr, right_arr)
        
    def merge(self, leftArr, rightArr):
        left = 0
        right = 0
        res = []
        while left < len(leftArr) and right < len(rightArr):
            if leftArr[left] < rightArr[right]:
                res.append(leftArr[left])
                left += 1
            else:
                res.append(rightArr[right])
                right += 1
        res.extend(leftArr[left:])
        res.extend(rightArr[right:])
        return res