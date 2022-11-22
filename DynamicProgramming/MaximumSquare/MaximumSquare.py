class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        COLS = len(matrix[0])
        ROWS = len(matrix)
        
        dp = [[0]*(COLS+1) for _ in range(ROWS+1)]
        max_num = 0
        
        for i in range(1, ROWS+1):
            for j in range(1, COLS+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    max_num = max(max_num, dp[i][j])
        return max_num**2