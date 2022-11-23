from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        curr = 0
        p2 = len(nums) - 1
        
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p1] = nums[p1], nums[curr]
                p1 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
            else:
                curr += 1


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        K = max(nums)
        counts = [0] * (K + 1)
        for elem in nums:
            counts[elem] += 1
        print(counts)
        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count
        print(counts)
        
        sorted_lst = [0] * len(nums)

        for elem in nums:
            sorted_lst[counts[elem]] = elem
            # since we have placed an item in index counts[elem], we need to
            # increment counts[elem] index by 1 so the next duplicate element
            # is placed in appropriate index
            counts[elem] += 1
        print(counts)
        print(sorted_lst)
        for i in range(len(nums)):
            nums[i] = sorted_lst[i]
        