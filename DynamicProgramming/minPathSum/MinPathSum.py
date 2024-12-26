from typing import List

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid) - 1
        n = len(grid[0]) - 1

        memo = {}

        def helper(i, j):
            if i > m or j > n:
                return float('inf')

            if (i, j) in memo:
                return memo[(i, j)]

            if i == m and j == n:
                return grid[i][j]
            
            ans = grid[i][j] + min(helper(i+1, j), helper(i, j+1))

            memo[(i, j)] = ans

            return ans

        return helper(0, 0)


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        
        dp = [[0] * n] * m

        dp[0][0] = grid[0][0]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m - 1 and j != n - 1:
                    dp[i][j] = grid[i][j] + dp[i][j+1]
                elif i != m - 1 and j == n - 1:
                    dp[i][j] = grid[i][j] + dp[i+1][j]
                elif i != m - 1 and j != n - 1:
                    dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
                else:
                    dp[i][j] = grid[i][j]

        return dp[0][0]
