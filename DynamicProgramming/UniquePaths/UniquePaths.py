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



# With obstacles
class Solution:
    
    # here I just changed the formal variable name 
    # from obstacleGrid to obs just for convinience
    
    def uniquePathsWithObstacles(self, obs):
        m, n = len(obs), len(obs[0])
        
        def solve(i , j):
            # base condition for recursion
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n or obs[i][j] == 1:
                return 0
            # the down and right recursive calls respectively
            return solve(i + 1, j) + solve(i, j+1)
        
        return solve(0,0)
    
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp= [1] * m

        for j in range(1, n):
            for i in range(1, m):
                dp[i] += dp[i-1]

        return dp[-1]

        
        
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row        
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.            
        return obstacleGrid[m-1][n-1]