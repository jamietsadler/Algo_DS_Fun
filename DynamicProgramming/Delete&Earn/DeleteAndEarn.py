from collections import defaultdict
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        points = defaultdict(int)
        max_number = 0
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
        memo = {}
        def recurse(num):
            if num == 0:
                return 0
            if num == 1:
                return points[num]

            if num in memo:
                return memo[num]
            
            ans = max(recurse(num-1), recurse(num-2) + points[num])
            memo[num] = ans
            return ans
        
        return recurse(max_number)
            