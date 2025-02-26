from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:

        furthest = 0
        end = 0

        answer = 0

        for i in range(len(nums)-1):
            furthest = max(furthest, i + nums[i])

            if i == end:
                answer += 1
                end = furthest
            

        return answer