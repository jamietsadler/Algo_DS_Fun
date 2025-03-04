
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        low, high = 0, len(matrix) - 1

        while low <= high:
            idx = low + (high - low)//2
            row = matrix[idx]
            if target < row[0]:
                high = idx - 1
            elif target > row[-1]:
                low  = idx + 1
            else:
                low, high = 0, len(row) - 1
                while low <= high:
                    idx = low + (high-low)//2
                    if row[idx] == target:
                        return True
                    elif target < row[idx]:
                        high = idx - 1
                    else:
                        low = idx + 1
                return False

        return False