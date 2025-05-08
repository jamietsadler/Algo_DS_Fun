from typing import List

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        curr_furthest = 0

        for i in range(len(nums)-1):
            curr_furthest = max(curr_furthest, i + nums[i])
            if i == curr_furthest:
                return False
        return True


class Solution:
    def jump(self, nums: List[int]) -> int:

        ans = 0
        curr_furthest = 0
        curr_end = 0

        for i in range(len(nums)-1):
            curr_furthest = max(curr_furthest, i + nums[i])

            if i == curr_end:
                curr_end = curr_furthest
                ans += 1
        return ans