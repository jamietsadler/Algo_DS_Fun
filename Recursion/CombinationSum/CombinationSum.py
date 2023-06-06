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


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def helper(combo, remain, i, res):
            if remain == 0:
                res.append(list(combo))
                return   

            if remain < 0:
                return          
            
            for j in range(i, len(candidates)):
                if j > i \
                  and candidates[j] == candidates[j-1]:
                    continue

                combo.append(candidates[j])
                helper(combo, remain - candidates[j], j+1, res)
                combo.pop()

        candidates.sort()
        helper([], target, 0, res)
        return res