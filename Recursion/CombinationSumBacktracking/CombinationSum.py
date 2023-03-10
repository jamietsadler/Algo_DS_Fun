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