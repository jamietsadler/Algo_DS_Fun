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