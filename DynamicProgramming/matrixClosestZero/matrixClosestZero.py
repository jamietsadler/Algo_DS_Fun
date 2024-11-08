
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        results = [row[:] for row in mat]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    min_result = float('inf')
                    if i > 0:
                        min_result = min(results[i-1][j],min_result)
                    if j > 0:
                        min_result = min(results[i][j-1],min_result)
                    results[i][j] = min_result + 1

        for i in range(len(mat)-1, -1, -1):
            for j in range(len(mat[0])-1, -1, -1):
                if mat[i][j] != 0:
                    min_result = float('inf')
                    if i < len(mat)-1:
                        min_result = min(results[i+1][j],min_result)
                    if j < len(mat[0])-1:
                        min_result = min(results[i][j+1],min_result)
                    results[i][j] = min(min_result+1, results[i][j])

        return results

                        
