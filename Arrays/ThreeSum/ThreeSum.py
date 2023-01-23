class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(i, nums, res)
        return res

    
    def twoSum(self, i, nums, res):
        lo = i + 1
        high = len(nums) - 1
        while lo < high:
            if nums[i] + nums[lo] + nums[high] == 0:
                res.append([nums[i], nums[lo], nums[high]])
                lo += 1
                high -= 1
                while lo < high and nums[lo] == nums[lo - 1]:
                    lo += 1
            elif nums[i] + nums[lo] + nums[high] > 0:
                high -= 1

            else:
                lo += 1