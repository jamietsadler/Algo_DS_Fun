from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for r in range(rowIndex + 1):
            row = [1] * (r+1)
            if r == 0:
                triangle.append(row)
            else:
                for i in range(1, len(row) - 1):
                    row[i] = triangle[r-1][i] + triangle[r-1][i-1]
                triangle.append(row)
                
        return triangle[-1]