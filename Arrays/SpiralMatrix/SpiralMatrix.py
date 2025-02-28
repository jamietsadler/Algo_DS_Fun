from typing import List

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        matrix = [[0] * n for _ in range(n)]
        row = 0
        col = 0
        dirs = [(0,1), (1, 0), (0, -1), (-1, 0)]
        diridx = 0

        for num in range(1, (n**2)+1):
            print(row, col)
            matrix[row][col] = num
            i, j = dirs[diridx]

            if row + i >= len(matrix) or row + i < 0 or col + j >= len(matrix[0]) or col + j < 0 or matrix[row + i][col + j] > 0:
                diridx = (diridx + 1) % 4

            i, j = dirs[diridx]
            row, col = row + i, col + j
        
        return matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0]) # Initial possible number of steps
        direction = 1 # Start off going right
        i, j = 0, -1
        output = []
        while m*n > 0:
            for _ in range(n): # move horizontally
                j += direction
                output.append(matrix[i][j])
            m-= 1
            for _ in range(m): # move vertically
                i += direction
                output.append(matrix[i][j])
            n-=1
            direction *= -1 # flip direction
        return output