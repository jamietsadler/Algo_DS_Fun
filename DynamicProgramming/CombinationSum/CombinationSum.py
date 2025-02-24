
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def helper(rem, combination, start):
            if rem < 0:
                return
            if rem == 0:
                res.append(combination[:])
                return
            
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num <= rem:
                    combination.append(num)
                    helper(rem - num, combination, i)
                    combination.pop()
            
            return 
        
        helper(target, [], 0)
        return res