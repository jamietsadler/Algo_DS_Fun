from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            
            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if p1 == len(text1) or p2 == len(text2):
                return 0
            
            # Recursive case 1.
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)
            
            # Recursive case 2.
            else:
                return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))
            
        return memo_solve(0, 0)
    
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp_grid = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for t1 in range(len(text1)-1, -1, -1):
            for t2 in range(len(text2)-1, -1, -1):
                if text1[t1] == text2[t2]:
                    dp_grid[t1][t2] = dp_grid[t1+1][t2+1] + 1
                else:
                    dp_grid[t1][t2] = max(dp_grid[t1+1][t2], dp_grid[t1][t2+1])
        
        return dp_grid[0][0]