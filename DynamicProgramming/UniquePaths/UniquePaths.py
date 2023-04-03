from functools import lru_cache
# Top Down
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache
        def helper(row, col):
            if row >= m or col >= n:
                return 0
            
            if row == m - 1 and col == n - 1:
                return 1
            
            return helper(row + 1, col) + helper(row, col+1)
            
        return helper(0, 0)


# Bottom Up
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[1]*n for _ in range(m)]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[-1][-1]

