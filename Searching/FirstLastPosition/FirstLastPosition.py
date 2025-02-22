class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        # search low
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        i = left if (left < len(nums) and left >= 0 and nums[left] == target) else -1

        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        j = right if (right < len(nums) and right >= 0 and nums[right]  == target) else -1

        if i <= j:
            return i, j
        else:
            return [-1, -1]
