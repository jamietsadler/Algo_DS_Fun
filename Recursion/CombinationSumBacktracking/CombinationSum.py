from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(options, remain, start):
            if remain == 0:
                res.append(list(options))
                return

            elif remain < 0:
                return 
            
            for i in range(start, len(candidates)): # need start to not get repeat combinations
                options.append(candidates[i])

                helper(options, remain - candidates[i], i)

                options.pop()

        helper([], target, 0)

        return res
    
class Solution2(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def helper(rem, combination, start):
            if rem == 0:
                res.append(combination[:])
                return

            if rem < 0:
                return 

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                num = candidates[i]
                if rem - num >= 0:
                    combination.append(num)
                    helper(rem - num, combination, i+1)
                    combination.pop()

            return 

        candidates.sort()
        helper(target, [], 0)
        return res
