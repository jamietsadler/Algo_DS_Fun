from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if not grid:
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.bfs(grid, i, j)
        
        return count
                    
    
    
    def bfs(self, grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        self.bfs(grid, r, c - 1)
        self.bfs(grid, r, c + 1)
        self.bfs(grid, r -1, c)
        self.bfs(grid, r + 1, c)