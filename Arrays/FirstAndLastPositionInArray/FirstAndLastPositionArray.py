class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        
        def searchLow(nums, target):
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (hi + lo)//2
                if nums[mid] >= target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return lo
        
        def searchHigh(nums, target):
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return hi
        
        lo = searchLow(nums, target)
        hi = searchHigh(nums, target)
        if len(nums) >= lo >= 0  and lo <= hi and nums[lo] == target:
            return [lo, hi]
        
        return [-1, -1]