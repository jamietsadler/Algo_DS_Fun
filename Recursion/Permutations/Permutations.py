from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(first = 0):
            if first == len(nums) - 1:
                ans.append(nums[:])
                return
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]

                backtrack(first+1)

                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return ans


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        used = [False]*len(nums)

        def backtrack(combo, res, used):
            if len(combo) == len(nums):
                res.append(combo[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    combo.append(nums[i])
                    used[i] = True
                    backtrack(combo, res, used)
                    used[i] = False
                    combo.pop()

        backtrack([], res, used)
        return res



# unique combinations
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        used = [False]*len(nums)

        def backtrack(combo, res, used):
            if len(combo) == len(nums):
                res.append(combo[:])
                return

            lookup = set()
            for i in range(len(nums)):
                if not used[i] and nums[i] not in lookup:
                    combo.append(nums[i])
                    used[i] = True
                    backtrack(combo, res, used)
                    used[i] = False
                    combo.pop()
                    lookup.add(nums[i])

        backtrack([], res, used)
        return res
