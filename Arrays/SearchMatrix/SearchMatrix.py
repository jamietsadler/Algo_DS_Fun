from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return None
        
        height = len(matrix)
        width = len(matrix[0])
        
        row = 0
        col = len(matrix[0])-1
        
        while col >= 0 and row < height:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False